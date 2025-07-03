****
# HOME ALARM SYSTEM

****



****

## **Project Description**
****


For this tutorial we are creating a security alarm device that through various ways detects motion when activated remotely or by a tilt switch and triggers an alarm and notifies the house owner of the detected inruder via a message. 

The device utilizes a bread board, a pico w microcontroller several complementary sensors such as a PIR sensor,hall effect digital sensor , a passive buzzer and a tilt switch. 

Furthermore for data visualization Adafruit will be used and to publish data to Adafruit the arduino MQTT libray will be used. 

Finally for connectivity wifi will be used and for notifying the house owner via Adafruit actions using a webhook the application known as discord will be used.

Also the IDE known as thonny will be utilized and the scource code with be in micropython.

Estimated time: 20-25 hours if all materials are already available and no prior iot experience.

****
## **Objective**
****

The main motivation behind this project is testing and combining various easily available sensors as well as creating a home utility device.

Through remote activation i can set up the alarm device for my flat room or the main entrance to the building and be notified via discord message of any intrusion and call the police in time.

In case iam able to further incorporate the arducam OV7675 in this project i may be able to capture images of any dected home intrusion as well.
****
## **Purpose and insights**
****
The following tutorial will include various hardware components that will be outlined in detail and a step by step process of setting up the required IDE and other software as well as the pin locations on the breadboard for connecting the jumping wires to the required pins.

It will also include code snippets from important fucntions written in micropython.

Hopefully by the end the reader will have gained knowledge on how a micro controller can interact with micropython operations and affect the various connected sensors as well gaining knowledge on how to set up wifi connectivity and establish MQTT clients for the micro controller.





****
## **Materials**
****

* The materials table below shows the individual materials from the elektrokit with the official prices the author of this tutorial however bought used materials from kits from other people that were at lower price.
* In total the author of the tutorial spent around 300 to 400 sek.

| Image | Item | Description | Cost |
| --- | --- | --- | --- |
| <img src="https://www.electrokit.com/cache/ba/700x700-product_41019_41019114_PICO-WH-HERO.jpg" alt="Raspberry Pi Pico W" width="100"> | [Raspberry Pi Pico W](https://www.electrokit.com/en/raspberry-pi-pico-wh) | The microcontroller for managing  operations. | 99 SEK |
| <img src="https://www.electrokit.com/upload/product/41015/41015509/41015509.jpg" alt="PIR motion sensor HC-SR501" width="100"> | [PIR motion sensor HC-SR501](https://www.electrokit.com/en/pir-rorelsedetektor-hc-sr501) | Detects movement within an area through motion and temperature. | 49 SEK |
| <img src="https://www.electrokit.com/resource/uC96/9pI/fLkXATsC8m/product/41016/41016226/41016226.webp" alt="Passive piezo buzzer 3.8 kHz" width="100"> | [Passive piezo buzzer 3.8 kHz](https://www.electrokit.com/piezoelement-12x8.5mm-passiv) | Passive buzzer that acts as a sound alarm | 12 SEK |
| <img src="https://www.electrokit.com/cache/b9/700x700-product_41012_41012686_41012686.jpg" alt="Jumper wires" width="100"> | [Jumper wires](https://www.electrokit.com/en/labbsladd-40-pin-30cm-hona/hane) | They are used to connect components on the breadboard and microcontroller. | 55 SEK |
| <img src="https://www.electrokit.com/upload/product/10160/10160840/10160840.jpg" alt="Breadboard" width="100"> | [Breadboard](https://www.electrokit.com/en/kopplingsdack-840-anslutningar) | A board for making circuits. | 69 SEK |
| <img src="https://www.electrokit.com/cache/4c/700x700-product_40810_40810310_40810310.png" alt="Resistor carbon film 0.25W 1kohm (1k)" width="100"> | [Resistor carbon film 0.25W 1kohm (1k)](https://www.electrokit.com/en/motstand-kolfilm-0.25w-1kohm-1k) | Resistors to limit current and divide voltages. | 1 SEK |
| <img src="https://www.electrokit.com/upload/product/41018/41018852/41018852.jpg" alt="" width="100"> | [Tilt switch](https://www.electrokit.com/tiltswitch-5vdc-vertikal) | Tilt switch sensor that detects changes in orientation or inclination. |18.50 SEK|
| <img src="https://www.electrokit.com/upload/product/41015/41015730/41015730.jpg" alt="" width="100"> | [Hall effect sensor digital](https://www.electrokit.com/tiltswitch-5vdc-vertikal) | Hall effect sensor that detects magnetic changes | 39 SEK |
 <img src="https://www.electrokit.com/upload/quick/36/bf/5f05_41015493.jpg" alt="" width="100"> | [USB cable A male - micro B male 5m](https://www.electrokit.com/tiltswitch-5vdc-vertikal) | Cable that will be used for data transfer | 59 SEK |







****


## **Einvironment Setup**

****
For the environment i initially  used Vscode as i have used it for other projects however i found issues in oppening and re oppening the folders and files in the Pico W using Vscode and Pymakr.

As such i opted for a much simpler IDE named thonny that only required downloading and choosing the device when connecting.
***
### Step 1: Installing the IDE 
***

* Download python from the official python website 

* Install Node js (needed for the plugin)


* Download and and try Thonny

* Have your Raspberry Pi Pico board ready and remove the sponge

* Have a USB cable
***
### Step 2: Installing and updating firmware
***
* Download the Raspberry Pi Pico W / RP2040 micropython firmware

* Connect the micro usb the end of your cable to the pico.


* While holding the BOOTSEL key button connect the usb type A to 
your computer .

* After you have done so release the button .

* You will see a new drive open with a specific RPI related name .Which is the pico storage .

* **Once that happens,** copy paste the firm ware file in that storage. Wait for the board to automatically disconnect from the computer .

* To test that everything is okay, unplag and plug back the usb cable.
***

### Step 3: Testing Pico W responsiveness in Thonny

***

* After you have recconected the Pico thonny then from the bottom side of the terminal make sure you choose the appropriate device ![image](https://hackmd.io/_uploads/HyXG-WGSgx.png)

* Then navigate to open files and folder choose the Pico W device instead of computer and open main.py.Also depicted in the above image.

* Once there you can test the picos on board led responsiveness by using the following code sample:

        from machine import Pin # import Pin definitions
        import time # import timer library

        define GP25 as output pin
        redLED = Pin(25, Pin.OUT)

        start loop
        while True:    
            redLED.on() # turn on red LED
            time.sleep(0.3) # wait 0.3 seconds
            redLED.off() # turn off red LED
            time.sleep(0.8) # wait 0.8 second
* If succesfull congrats its time to go to the next step of establishing connectivity



***

### Step 4: Wifi Connectivity

***

* Navigate to keys.py in the Pico files and fill in the SSID and wifi password 

* Afterwards navigate to boot.py and import keys , the network library and import sleep from time.

* Next create a connect() function which uses the network library to create a WLAN object in station mode .Meaning the pico will connect to an access point 
* Following this use the object to enable the wifi interface,set the power mode and connect using your credeintilas after already checking for an existing connection.
* The function then should get and print the IP adress
* To accomodate the connect() function create also create an httpget() function.Which takes a url adress as an argument.
* It then should split the url to components such as host or path or http using the in built .split method.
* It shen should open a socket and connect it to the IPs adress
* Finally it should send an http get request to the host with a specific path.
* Here is a working example of what the boot.py file should look like:
* 
        import keys
        import network
        from time import sleep

        def connect():
            wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode
            if not wlan.isconnected():                  # Check if already connected
                print('connecting to network...')
                wlan.active(True)                       # Activate network interface
                # set power mode to get WiFi power-saving off (if needed)
                wlan.config(pm = 0xa11140)
                wlan.connect(keys.WIFI_SSID, keys.WIFI_PASS)  # Your WiFi Credential
                print('Waiting for connection...', end='')
                # Check if it is connected otherwise wait
                while not wlan.isconnected() and wlan.status() >= 0:
                    print('.', end='')
                    sleep(1)
            # Print the IP assigned by router
            ip = wlan.ifconfig()[0]
            print('\nConnected on {}'.format(ip))
            return ip

        def http_get(url = 'http://detectportal.firefox.com/'):
            import socket                           # Used by HTML get request
            import time                             # Used for delay
            _, _, host, path = url.split('/', 3)    # Separate URL request
            addr = socket.getaddrinfo(host, 80)[0][-1]  # Get IP address of host
            s = socket.socket()                     # Initialise the socket
            s.connect(addr)                         # Try connecting to host address
            # Send HTTP request to the host with specific path
            s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))    
            time.sleep(1)                           # Sleep for a second
            rec_bytes = s.recv(10000)               # Receve response
            print(rec_bytes)                        # Print the response
            s.close()                               # Close connection

        # WiFi Connection
        try:
            ip = connect()
        except KeyboardInterrupt:
            print("Keyboard interrupt")

        # HTTP request
        try:
            http_get()
        except (Exception, KeyboardInterrupt) as err:
            print("No Internet", err)




****

***

### Step 5: Adafruit 

***





* Then navigate to open files and folder choose the Pico W device instead of computer and open main.py.Also depicted in the above image.

* Once there you can test the picos on board led responsiveness by using the following code sample:

        from machine import Pin # import Pin definitions
        import time # import timer library

        define GP25 as output pin
        redLED = Pin(25, Pin.OUT)

        start loop
        while True:    
            redLED.on() # turn on red LED
            time.sleep(0.3) # wait 0.3 seconds
            redLED.off() # turn off red LED
            time.sleep(0.8) # wait 0.8 second
* If succesfull congrats its time to go to the next step of establishing connectivity



***

### Step 4: Wifi Connectivity

***

* Navigate to keys.py in the Pico files and fill in the SSID and wifi password 

* Afterwards navigate to boot.py and import keys , the network library and import sleep from time.

* Next create a connect() function which uses the network library to create a WLAN object in station mode .Meaning the pico will connect to an access point 
* Following this use the object to enable the wifi interface,set the power mode and connect using your credeintilas after already checking for an existing connection.
* The function then should get and print the IP adress
* To accomodate the connect() function create also create an httpget() function.Which takes a url adress as an argument.
* It then should split the url to components such as host or path or http using the in built .split method.
* It shen should open a socket and connect it to the IPs adress
* Finally it should send an http get request to the host with a specific path.
* Here is a working example of what the boot.py file should look like:
* 
        import keys
        import network
        from time import sleep

        def connect():
            wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode
            if not wlan.isconnected():                  # Check if already connected
                print('connecting to network...')
                wlan.active(True)                       # Activate network interface
                # set power mode to get WiFi power-saving off (if needed)
                wlan.config(pm = 0xa11140)
                wlan.connect(keys.WIFI_SSID, keys.WIFI_PASS)  # Your WiFi Credential
                print('Waiting for connection...', end='')
                # Check if it is connected otherwise wait
                while not wlan.isconnected() and wlan.status() >= 0:
                    print('.', end='')
                    sleep(1)
            # Print the IP assigned by router
            ip = wlan.ifconfig()[0]
            print('\nConnected on {}'.format(ip))
            return ip

        def http_get(url = 'http://detectportal.firefox.com/'):
            import socket                           # Used by HTML get request
            import time                             # Used for delay
            _, _, host, path = url.split('/', 3)    # Separate URL request
            addr = socket.getaddrinfo(host, 80)[0][-1]  # Get IP address of host
            s = socket.socket()                     # Initialise the socket
            s.connect(addr)                         # Try connecting to host address
            # Send HTTP request to the host with specific path
            s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))    
            time.sleep(1)                           # Sleep for a second
            rec_bytes = s.recv(10000)               # Receve response
            print(rec_bytes)                        # Print the response
            s.close()                               # Close connection

        # WiFi Connection
        try:
            ip = connect()
        except KeyboardInterrupt:
            print("Keyboard interrupt")

        # HTTP request
        try:
            http_get()
        except (Exception, KeyboardInterrupt) as err:
            print("No Internet", err)




****

***

### Step 5:Setting up Adafruit 

***
* Go to the adafruit [webpage](https://www.adafruit.com/?srsltid=AfmBOopOkW1-62JmBLmc8JdtTLbPksxHIvHh7icX8H-pJiojWBXWAKuu) and create an account 
* After you have created an account and logged in go to the IO section and the feed section![image](https://hackmd.io/_uploads/rJEjCmXrge.png)
* Then click create new feed In this case we will follow up on our previous example so create a feed for the Led lights.
* Then navigate to the keys.py and fill in the feedsinfo information and aio key that is in the above key icon ![image](https://hackmd.io/_uploads/HkCLwNQBeg.png)
 * Copy the relevant key information in this code sample and post it in the existing keys.py file: 

        import ubinascii              # Conversions between binary data and various encodings
        import machine                # To Generate a unique id from processor

        # Wireless network
        WIFI_SSID =  "Your_WiFi_Name"
        WIFI_PASS = "Your_WiFi_Password" # No this is not our regular password. :)

        # Adafruit IO (AIO) configuration
        AIO_SERVER = "io.adafruit.com"
        AIO_PORT = 1883
        AIO_USER = "Your_Adafruit_User_Name"
        AIO_KEY = "Your_Adafruit_Application_Key"
        AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
        AIO_LIGHTS_FEED = "Your_lights_Feed_Address"
        AIO_RANDOMS_FEED = "Your_randoms_Feed_Address"
* Then navigate to main.py file once there create a function that publishes results or sends messages to adafruit by importing the mqtt.py file from the existing firmware and the keys.py file 
* A code sample for doing this that includes a function that publishes results for random numbers is demonstrated below:

        import time                   # Allows use of time.sleep() for delays
        from mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO
        import machine                # Interfaces with hardware components
        import micropython            # Needed to run any MicroPython code
        import random                 # Random number generator
        from machine import Pin       # Define pin
        import keys                   # Contain all keys used here
        import wifiConnection         # Contains functions to connect/disconnect from WiFi 


        # BEGIN SETTINGS
        # These need to be change to suit your environment
        RANDOMS_INTERVAL = 20000    # milliseconds
        last_random_sent_ticks = 0  # milliseconds
        led = Pin("LED", Pin.OUT)   # led pin initialization for Raspberry Pi Pico W


        # Callback Function to respond to messages from Adafruit IO
        def sub_cb(topic, msg):          # sub_cb means "callback subroutine"
            print((topic, msg))          # Outputs the message that was received. Debugging use.
            if msg == b"ON":             # If message says "ON" ...
                led.on()                 # ... then LED on
            elif msg == b"OFF":          # If message says "OFF" ...
                led.off()                # ... then LED off
            else:                        # If any other message is received ...
                print("Unknown message") # ... do nothing but output that it happened.

        # Function to generate a random number between 0 and the upper_bound
        def random_integer(upper_bound):
            return random.getrandbits(32) % upper_bound

        # Function to publish random number to Adafruit IO MQTT server at fixed interval
        def send_random():
            global last_random_sent_ticks
            global RANDOMS_INTERVAL

            if ((time.ticks_ms() - last_random_sent_ticks) < RANDOMS_INTERVAL):
                return; # Too soon since last one sent.

            some_number = random_integer(100)
            print("Publishing: {0} to {1} ... ".format(some_number, keys.AIO_RANDOMS_FEED), end='')
            try:
                client.publish(topic=keys.AIO_RANDOMS_FEED, msg=str(some_number))
                print("DONE")
            except Exception as e:
                print("FAILED")
            finally:
                last_random_sent_ticks = time.ticks_ms()


        # Try WiFi Connection
        try:
            ip = wifiConnection.connect()
        except KeyboardInterrupt:
            print("Keyboard interrupt")

        # Use the MQTT protocol to connect to Adafruit IO
        client = MQTTClient(keys.AIO_CLIENT_ID, keys.AIO_SERVER, keys.AIO_PORT, keys.AIO_USER, keys.AIO_KEY)

        # Subscribed messages will be delivered to this callback
        client.set_callback(sub_cb)
        client.connect()
        client.subscribe(keys.AIO_LIGHTS_FEED)
        print("Connected to %s, subscribed to %s topic" % (keys.AIO_SERVER, keys.AIO_LIGHTS_FEED))



        try:                      # Code between try: and finally: may cause an error
                                  # so ensure the client disconnects the server if
                                  # that happens.
            while 1:              # Repeat this loop forever
                client.check_msg()# Action a message if one is received. Non-blocking.
                send_random()     # Send a random number to Adafruit IO if it's time.
        finally:                  # If an exception is thrown ...
            client.disconnect()   # ... disconnect the client and clean up.
            client = None
            wifiConnection.disconnect()
            print("Disconnected from Adafruit IO.")
* Once you have done this navigate back to Adafruit to dashboard and add the feeds you have created press create new block and choose the appropriate visualization for the feeds.

* After this run the program on main.py .If everything has turned out well the results should shown un in the visualization blocks.




***


****
## **Project implementation**
****
* Now that the einvironment has been set up and tested its time to create implement the home alarm system.
* Here is a pin placement chart that will help connecting the various sensors : <img src="https://mischianti.org/wp-content/uploads/2022/09/Raspberry-Pi-Pico-W-rp2040-WiFi-pinout-mischianti-1024x786.jpg" alt="" width="800">
* PLACE THE FOLLOWING SENSORS LIKE SO :
* Hall effect sensor signal GP16 or pin 21 ,Ground or GND pin 28 ,vcc pin 26 or GP 20
* PIR sensor signal GP 27,GND pin 28, vcc pin 36
* Buzzer signal GP 14 ,GND or groun pin 38
* Tilt switch signal GP 27 or alternatively GP 15 , GND pin 38 , vcc pin 36
* Navigate to main.py the initialization of the pins should look like : 

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
* Then navigate to adafruit  create feeds for the sensors use the sensors feeds to fill in the feed keys in keys.py .In the end keys.py and the feeds should look like the following :
![image](https://hackmd.io/_uploads/B1ovCj7Sle.png)

        import ubinascii
        import machine
        WIFI_SSID = ""
        WIFI_PASS = ""
        AIO_SERVER = "io.adafruit.com"
        AIO_PORT = 1883
        AIO_USER = ""
        AIO_KEY = ""
        AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
        AIO_BUZZER_FEED = ""
        AIO_PIR_FEED = ""
        AIO_HALL_FEED = ""
        AIO_ALARM_FEED = ""
* After you have done this go on to modify the send feed function to be able to accomodate alarm states and the send cb function to incorporate the enabled and disabled states.That will be modified remotely from the dashborad or by the tilt switch: 

        def sub_cb(topic, msg):
            global alarm_enabled , prev_alarm
            print("MQTT IN:", topic, msg) # Shows incoming message
            if topic.decode() == keys.AIO_BUZZER_FEED:    # Checks if message is for controlling the buzzer
                if msg == b"ON": # byte message to turn on alarm
                    alarm_enabled = True
                    prev_alarm = None     # resets alarm state so it updates
                    print("Alarm ENABLED remotely")
                    #send_feed(keys.AIO_ALARM_FEED, "1")
                elif msg == b"OFF":
                    alarm_enabled = False
                    buzzer.duty_u16(0)
                    prev_alarm = None 
                    print("Alarm DISABLED remotely")
                    #send_feed(keys.AIO_ALARM_FEED, "0")

        def send_feed(feed, value):
            try:
                client.publish(feed, str(value))    #sends message to MQTT
            except Exception as e:    # error handling for exceptions prints error
                print(f"MQTT error on {feed}:", e)
                
* After you have done this make sure to set the call back function for incoming messages and connect to the MQTT broker.

        client.set_callback(sub_cb)        # set to handle incoming messages
        client.connect()                   # connects to MQTT broker
        client.subscribe(keys.AIO_BUZZER_FEED)        # Subscribe to feed/topic
        print("MQTT connected and subscribed.")
        
* Finally create an Alarm function that initializes most of the alarm states and handes the state logic based on the sensor readings


* First def alarm() and initilize the states:


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
* Secondly create the while loop for re sending menssages and enabling and desabling the alarm state Inside the loop check the messages from client and allow the tilt switch to affect the enabled and disabled state : 


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
                            
* Afterwards in the next code block inside the loop send the PIR and hall effect feeds based on the sensor states : 


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
* Finally ensure that the alarm state is sent by the send feed function only if the alarm state is enabled and the other sensor conidtions have been met:

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
* Then run the program after creating a new dashboard with the feed selecting the related blocks and the results should look like this:

* ![image](https://hackmd.io/_uploads/rkzgG0XSlg.png)








