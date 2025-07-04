import time
from machine import Pin, PWM
from mqtt import MQTTClient
import keys

pir_sensor = Pin(27, Pin.IN, Pin.PULL_UP)
hall_sensor = Pin(16, Pin.IN)
tilt_switch = Pin(27, Pin.IN, Pin.PULL_UP)
buzzer = PWM(Pin(14))
buzzer.duty_u16(0)
prev_tilt = tilt_switch.value()
tilt_triggered = False
alarm_enabled = True
prev_alarm = None

I_PICO = 0.050
I_WIFI_IDLE = 0.090
I_WIFI_ACTIVE = 0.100
I_PIR_IDLE = 0.00005
I_PIR_ACTIVE = 0.065
I_HALL = 0.005
I_BUZZER = 0.040
VOLTAGE = 5

idle_seconds = 0
triggered_seconds = 0

client = MQTTClient("alarm-device", keys.AIO_SERVER, keys.AIO_PORT, keys.AIO_USER, keys.AIO_KEY)

def sub_cb(topic, msg):
    global alarm_enabled , prev_alarm
    print("MQTT IN:", topic, msg)
    if topic.decode() == keys.AIO_BUZZER_FEED:
        if msg == b"ON":
            alarm_enabled = True
            prev_alarm = None
            #send_feed(keys.AIO_ALARM_FEED, "0")
            print("Alarm ENABLED remotely")
            #send_feed(keys.AIO_ALARM_FEED, "1")
        elif msg == b"OFF":
            alarm_enabled = False
            buzzer.duty_u16(0)
            prev_alarm = None
            #send_feed(keys.AIO_ALARM_FEED, "0")
            print("Alarm DISABLED remotely")
            #send_feed(keys.AIO_ALARM_FEED, "0")

def send_feed(feed, value):
    try:
        client.publish(feed, str(value))
    except Exception as e:
        print(f"MQTT error on {feed}:", e)
        
def calculate_power_usage():
    idle_hours = idle_seconds / 3600
    triggered_hours = triggered_seconds / 3600
    
    power_pico = VOLTAGE * I_PICO
    power_wifi_idle = VOLTAGE * I_WIFI_IDLE
    power_wifi_active = VOLTAGE * I_WIFI_ACTIVE
    power_pir_idle = VOLTAGE * I_PIR_IDLE
    power_pir_active = VOLTAGE * I_PIR_ACTIVE
    power_hall = VOLTAGE * I_HALL
    power_buzzer = VOLTAGE * I_BUZZER
    
    avg_power_wifi = (power_wifi_idle * idle_seconds + power_wifi_active * triggered_seconds) / (idle_seconds + triggered_seconds + 1e-6)
    avg_power_pir = (power_pir_idle * idle_seconds + power_pir_active * triggered_seconds) / (idle_seconds + triggered_seconds + 1e-6)
    avg_power_hall = power_hall * (triggered_seconds / (idle_seconds + triggered_seconds + 1e-6))
    avg_power_buzzer = power_buzzer * (triggered_seconds / (idle_seconds + triggered_seconds + 1e-6))
    
    total_power = power_pico + avg_power_wifi + avg_power_pir + avg_power_hall + avg_power_buzzer
    
    total_power_max = power_pico + power_wifi_active + power_pir_active + power_hall + power_buzzer
    
    
    energy_pico = power_pico * (idle_hours + triggered_hours)
    energy_wifi = (power_wifi_idle * idle_hours) + (power_wifi_active * triggered_hours)
    energy_pir = (power_pir_idle * idle_hours) + (power_pir_active * triggered_hours)
    energy_hall = power_hall * triggered_hours
    energy_buzzer = power_buzzer * triggered_hours
    
    
    
    total_energy = energy_pico + energy_wifi + energy_pir + energy_hall + energy_buzzer
    
    
    print(f"Pico power:      {power_pico:.3f} W")
    print(f"Wifi idle power: {power_wifi_idle:.3f} W")
    print(f"Wifi active:     {power_wifi_active:.3f} W")
    print(f"PIR idle:        {power_pir_idle:.5f} W")
    print(f"PIR active:      {power_pir_active:.3f} W")
    print(f"Hall:     {power_hall:.3f} W")
    print(f"Buzzer:          {power_buzzer:.3f} W")
    print(f"Total average Power:    {total_power:.3f} W")
    print(f"Total Power Max:{total_power_max:.3f} W")
    
    print(f"Idle time:      {idle_hours:.2f} h")
    print(f"Triggered time: {triggered_hours:.2f} h\n")
    print(f"Pico:       {energy_pico:.2f} Wh")
    print(f"Wifi:           {energy_wifi:.2f} Wh")
    print(f"PIR:     {energy_pir:.2f} Wh")
    print(f"Hall:    {energy_hall:.2f} Wh")
    print(f"Buzzer:         {energy_buzzer:.2f} Wh")
    
    print(f"Total:          {total_energy:.2f} Wh")
    
    send_feed(keys.AIO_POWER_PICO_FEED, round(energy_pico, 3))
    send_feed(keys.AIO_POWER_WIFI_FEED, round(energy_wifi, 3))
    send_feed(keys.AIO_POWER_PIR_FEED, round(energy_pir, 3))
    send_feed(keys.AIO_POWER_HALL_FEED, round(energy_hall, 3))
    send_feed(keys.AIO_POWER_BUZZER_FEED, round(energy_buzzer, 3))
    send_feed(keys.AIO_POWER_TOTAL_FEED, round(total_energy, 3))

client.set_callback(sub_cb)
client.connect()
client.subscribe(keys.AIO_BUZZER_FEED)
print("MQTT connected and subscribed.")

def alarm_loop():
    global alarm_enabled, prev_alarm , idle_seconds, triggered_seconds
    pir_prev = 0
    hall_prev = 1
    #prev_alarm = None
    buzz_timer = 0
    buzz_interval = 30
    alarm_state = "0"

    prev_tilt = tilt_switch.value()
    last_tilt_change = time.ticks_ms()
    tilt_debounce_ms = 300
    last_time = time.time() 

    while True:
        try:
            client.check_msg()
            
            tilt_state = tilt_switch.value()
            now = time.ticks_ms()
            if tilt_state != prev_tilt and time.ticks_diff(now, last_tilt_change) > tilt_debounce_ms:
                prev_tilt = tilt_state
                last_tilt_change = now
                alarm_enabled = not alarm_enabled
                if alarm_enabled:
                    print("ENABLED by tilt switch")
                else:
                    print("DISABLED by tilt switch")
                    
                    

            pir_state = pir_sensor.value()
            if pir_state != pir_prev:
                pir_prev = pir_state
                if pir_state:
                    print("motion detected")
                    send_feed(keys.AIO_PIR_FEED, "1")
                else:
                    print("no motion detected")
                    send_feed(keys.AIO_PIR_FEED, "0")

            hall_state = hall_sensor.value()
            
            if hall_state != hall_prev:
                hall_prev = hall_state
                if hall_state == 0:
                    print("magnet detected (TRIGGERED)")
                    send_feed(keys.AIO_HALL_FEED, "1")
                else:
                    print("magnet cleared")
                    send_feed(keys.AIO_HALL_FEED, "0")

            if alarm_enabled:
                if pir_state == 1 or hall_state == 0:
                    buzzer.freq(2000)
                    buzzer.duty_u16(3000)
                    alarm_state = "1"
                    buzz_timer += 1
                    triggered_seconds += 0.2
                    if buzz_timer >= buzz_interval:
                        send_feed(keys.AIO_ALARM_FEED, alarm_state)
                        buzz_timer = 0
                else:
                    buzzer.duty_u16(0)
                    alarm_state = "0"
                    buzz_timer = 0
                    idle_seconds += 0.2
            else:
                buzzer.duty_u16(0)
                alarm_state = "0"
                buzz_timer = 0
                idle_seconds += 0.2

            if alarm_state != prev_alarm :
                send_feed(keys.AIO_ALARM_FEED, alarm_state)
                prev_alarm = alarm_state
            
            if time.time() - last_time >= 30:
                calculate_power_usage()
                last_time = time.time()

        except Exception as e:
            print("Loop error:", e)

        time.sleep(0.2)

alarm_loop()
