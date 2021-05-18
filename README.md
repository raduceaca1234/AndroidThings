# solo-project-raduceaca1234
solo-project-raduceaca1234 created by GitHub Classroom


# Project Description
## Distance Measurement
### This project calculates the distance between the sensor and the reflecting object, using the well-known HC-SR04 Ultrasonic sensor. Ultrasonic sensors are designed to sense object proximity or range using ultrasound reflection, similar to radar, to calculate the time it takes to reflect ultrasound waves between the sensor and a solid object. The sensor that I chose to use for this project has four pins: ground (GND), Echo Pulse Output (ECHO), Trigger Pulse Input (TRIG), and 5V Supply (Vcc). 

### I power the module using Vcc, ground it using GND, and use our Raspberry Pi to send an input signal to TRIG, which triggers the sensor to send an ultrasonic pulse. The pulse waves bounce off any nearby objects and some are reflected back to the sensor. The sensor detects these return waves and measures the time between the trigger and returned pulse, and then sends a 5V signal on the ECHO pin.

# Schematics
![alt text](https://github.com/at-cs-ubbcluj-ro/solo-project-raduceaca1234/blob/main/Schematics.png)

# Rre-requisites

- Firebase project with Database and Storage (https://console.firebase.google.com)
- The following individual components:
    - [jumper wires](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiz_IrR-JfwAhUKr7IKHfkbBLwYABAHGgJscg&ohost=www.google.com&cid=CAESQOD2MxlXIIoq2Pdw1OnHdCPVRDsKEia1sP7HUGZR4Gp-x5Nrju381uFim3BbtTa5_ylv6OjE3Sxl5XkMNy0wroE&sig=AOD64_31qts5BNgvWc6-BIxAy-OfmYVVDg&ctype=5&q=&ved=2ahUKEwif_IHR-JfwAhW2hf0HHRsKCdEQ9aACegQIAhBl&adurl=) (MIKROE-512)
    - [1 breadboard](https://ro.rsdelivers.com/product/rs-pro/kh102/breadboard-prototyping-board-80-x-60-x-10mm/1029147?cm_mmc=RO-PLA-DS3A-_-google-_-CSS_RO_EN_ESD_Control_Cleanroom_%26_PCB_Prototyping_Whoop-_-(RO:Whoop!)+Breadboards-_-&matchtype=&pla-335110594459&s_kwcid=AL!7457!3!511788004018!!!g!335110594459!&gclid=CjwKCAjwg4-EBhBwEiwAzYAlsnvnfzhdsCaSYhoDkc_5KUM8NI2bd0uiNsep7nbJ5S2u55ZitjYQohoC6EYQAvD_BwE&gclsrc=aw.ds) (102-9147)
    - [Raspberry Pi 4](https://www.robofun.ro/placa-raspberry-pi-4-model-b-8gb.html?gclid=CjwKCAjwg4-EBhBwEiwAzYAlstFE-S-O7XfHFv6lf_oHk-KUx62dVO2LerPotMlTqfNI-DfVnpSB2xoCzcQQAvD_BwE) (RAS-219)
    - [Ultrasonic Range Sensor](https://www.optimusdigital.ro/en/ultrasonic-sensors/9-hc-sr04-ultrasonic-sensor.html) (HC-SR04)

# Setup and Build
- Create a Firebase project
- Access Project Settings in the console
- Access Service Account menu -> Database Secrets from the left menu
- Copy the Database Secret and paste it in the "apiKey" line from the Raspberry Pi project
- Go to General in Poject Setiings, copy the Project ID and paste it in the "authDomain" line
- Go to Realtime Database menu, copy the url in the page and paste it in the "storageBucket" line
- Go to Storage menu copy the url in the page and paste it in the "storageBucket" line
- Ensure the security rules for your Firebase project allow public read/write access
- Put the following conde in Firebase->Database->Rules
```
  {
    "rules": {
      ".read": true,
      ".write": true
    }
  }
 ```
- And the following code in Firebase->Storage->Rules
```
service firebase.storage {
    match /b/{bucket}/o {
      match /{allPaths=**} {
        allow read, write;
      }
    }
  }
```

# Running
- To run the app on the Raspberry Pi:
    - Connect the Ultrasonic Range Sensor to breadboard and the breadboard to the Raspberry according to the schematics above
    - Deploy and run the raspberry pi file
    - Record the distance between the sensor and the object
    - Access the Firebase Console -> Realtime Database and see that the data is stored live

# Demo
[(Watch the demo on YouTube)](https://youtu.be/2Z7NMXnj7Kk)

![demo](https://github.com/at-cs-ubbcluj-ro/solo-project-raduceaca1234/blob/main/ezgif.com-gif-maker.gif)

