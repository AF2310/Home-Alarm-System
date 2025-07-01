import ubinascii
import machine
WIFI_SSID = ""
WIFI_PASS = ""
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "aferat"
AIO_KEY = "aio_"
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
AIO_BUZZER_FEED = "aferat/feeds/alarm-setting"
AIO_PIR_FEED = "aferat/feeds/motion-detection"
AIO_HALL_FEED = "aferat/feeds/hall-detection"
AIO_ALARM_FEED = "aferat/feeds/alarm-status"
