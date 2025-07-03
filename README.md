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



| Image | Item | Description | Cost |
| --- | --- | --- | --- |
| <img src="https://www.electrokit.com/cache/ba/700x700-product_41019_41019114_PICO-WH-HERO.jpg" alt="Raspberry Pi Pico W" width="100"> | [Raspberry Pi Pico W](https://www.electrokit.com/en/raspberry-pi-pico-wh) | The core microcontroller for managing system operations. | 99 SEK |
| <img src="https://www.electrokit.com/upload/product/41015/41015509/41015509.jpg" alt="PIR motion sensor HC-SR501" width="100"> | [PIR motion sensor HC-SR501](https://www.electrokit.com/en/pir-rorelsedetektor-hc-sr501) | Detects any movement within the monitored area. | 49 SEK |
| <img src="https://www.electrokit.com/resource/uC96/9pI/fLkXATsC8m/product/41016/41016226/41016226.webp" alt="Passive piezo buzzer 3.8 kHz" width="100"> | [Passive piezo buzzer 3.8 kHz](https://www.electrokit.com/piezoelement-12x8.5mm-passiv) | Passive buzzer that acts as a sound alarm | 12 SEK |
| <img src="https://www.electrokit.com/cache/b9/700x700-product_41012_41012686_41012686.jpg" alt="Jumper wires" width="100"> | [Jumper wires](https://www.electrokit.com/en/labbsladd-40-pin-30cm-hona/hane) | They are used to connect components on the breadboard and microcontroller. | 55 SEK |
| <img src="https://www.electrokit.com/upload/product/10160/10160840/10160840.jpg" alt="Breadboard" width="100"> | [Breadboard](https://www.electrokit.com/en/kopplingsdack-840-anslutningar) | A board for making solderfree experiment circuits for prototyping. | 69 SEK |
| <img src="https://www.electrokit.com/cache/4c/700x700-product_40810_40810310_40810310.png" alt="Resistor carbon film 0.25W 1kohm (1k)" width="100"> | [Resistor carbon film 0.25W 1kohm (1k)](https://www.electrokit.com/en/motstand-kolfilm-0.25w-1kohm-1k) | Resistors to limit current and divide voltages. | 1 SEK |
| <img src="https://www.electrokit.com/upload/product/41018/41018852/41018852.jpg" alt="" width="100"> | [Tilt switch](https://www.electrokit.com/tiltswitch-5vdc-vertikal) | Tilt switch sensor that detects changes in orientation or inclination. |18.50 SEK|
| <img src="https://www.electrokit.com/upload/product/41015/41015730/41015730.jpg" alt="" width="100"> | [Hall effect sensor digital](https://www.electrokit.com/tiltswitch-5vdc-vertikal) | Hall effect sensor that detects magnetic changes | 39 SEK |
 <img src="https://www.electrokit.com/upload/quick/36/bf/5f05_41015493.jpg" alt="" width="100"> | [USB cable A male - micro B male 5m](https://www.electrokit.com/tiltswitch-5vdc-vertikal) | Cable that will be used for data transfer | 39 SEK |







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
* Then navigate to main.py file

***






