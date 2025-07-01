# HOME ALARM SYSTEM

af224dz

****
**Project Description**
****


For this tutorial we are creating a security alarm device that through various ways detects motion when activated remotely or by a tilt switch and triggers an alarm and notifies the house owner of the detected inruder via a message. 

The device utilizes a bread board, a pico w microcontroller several complementary sensors such as a PIR sensor,hall effect digital sensor , a passive buzzer and a tilt switch. 

Furthermore for data visualization Adafruit will be used and to publish data to Adafruit the arduino MQTT libray will be used. 

Finally for connectivity wifi will be used and for notifying the house owner via Adafruit actions using a webhook the application known as discord will be used.

Also the IDE known as thonny will be utilized and the scource code with be in micropython.

Estimated time: 20-25 hours if all materials are already available and no prior iot experience.

****
**Objective**
****

The main motivation behind this project is testing and combining various easily available sensors as well as creating a home utility device.

Through remote activation i can set up the alarm device for my flat room or the main entrance to the building and be notified via discord message of any intrusion and call the police in time.

In case iam able to further incorporate the arducam OV7675 in this project i may be able to capture images of any dected home intrusion as well.
****
**Purpose and insights**
****
The following tutorial will include various hardware components that will be outlined in detail and a step by step process of setting up the required IDE and other software as well as the pin locations on the breadboard for connecting the jumping wires to the required pins.

It will also include code snippets from important fucntions written in micropython.

Hopefully by the end the reader will have gained knowledge on how a micro controller can interact with micropython operations and affect the various connected sensors as well gaining knowledge on how to set up wifi connectivity and establish MQTT clients for the micro controller.





****
**Materials**
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












