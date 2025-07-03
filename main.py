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

client.set_callback(sub_cb)
client.connect()
client.subscribe(keys.AIO_BUZZER_FEED)
print("MQTT connected and subscribed.")

def alarm_loop():
    global alarm_enabled, prev_alarm
    pir_prev = 0
    hall_prev = 1
    #prev_alarm = None
    buzz_timer = 0
    buzz_interval = 30
    alarm_state = "0"

    prev_tilt = tilt_switch.value()
    last_tilt_change = time.ticks_ms()
    tilt_debounce_ms = 300

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
                    if buzz_timer >= buzz_interval:
                        send_feed(keys.AIO_ALARM_FEED, alarm_state)
                        buzz_timer = 0
                else:
                    buzzer.duty_u16(0)
                    alarm_state = "0"
                    buzz_timer = 0
            else:
                buzzer.duty_u16(0)
                alarm_state = "0"
                buzz_timer = 0
            if alarm_state != prev_alarm :
                send_feed(keys.AIO_ALARM_FEED, alarm_state)
                prev_alarm = alarm_state

        except Exception as e:
            print("Loop error:", e)

        time.sleep(0.2)

alarm_loop()
