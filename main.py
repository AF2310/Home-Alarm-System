import time
from machine import Pin, PWM
from mqtt import MQTTClient
import keys

pir_sensor = Pin(27, Pin.IN, Pin.PULL_UP)
hall_sensor = Pin(16, Pin.IN)
buzzer = PWM(Pin(14))
buzzer.duty_u16(0)

alarm_enabled = True

client = MQTTClient("alarm-device", keys.AIO_SERVER, keys.AIO_PORT, keys.AIO_USER, keys.AIO_KEY)

def sub_cb(topic, msg):
    global alarm_enabled
    print("MQTT IN:", topic, msg)
    if topic.decode() == keys.AIO_BUZZER_FEED:
        if msg == b"ON":
            alarm_enabled = True
            print("Alarm ENABLED remotely")
            #send_feed(keys.AIO_ALARM_FEED, "1")
        elif msg == b"OFF":
            alarm_enabled = False
            buzzer.duty_u16(0)
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

pir_prev = 0
hall_prev = 1
prev_alarm = None

while True:
    try:
        client.check_msg()

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
                send_feed(keys.AIO_HALL_FEED, "TRIGGERED")
            else:
                print("magnet cleared")
                send_feed(keys.AIO_HALL_FEED, "CLEAR")

        if alarm_enabled:
            if pir_state == 1 or hall_state == 0:
                buzzer.freq(2000)
                buzzer.duty_u16(3000)
                #send_feed(keys.AIO_ALARM_FEED, "1")
                alarm_state = "1"
            else:
                buzzer.duty_u16(0)
                #send_feed(keys.AIO_ALARM_FEED, "0")
                alarm_state = "0"
        else:
            buzzer.duty_u16(0)
            alarm_state = "0"
        if alarm_state != prev_alarm :
            send_feed(keys.AIO_ALARM_FEED, alarm_state)
            prev_alarm = alarm_state

    except Exception as e:
        print("Loop error:", e)

    time.sleep(0.2)
