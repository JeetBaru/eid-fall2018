Name:
Jeet Baru

Install Instructions:
Application requires QT5 installed with python3. The application also requires Adafruit_DHT library installed.
monitorv3.py has the class for dialog, the ui and logic for button presses. temphum.py has the instantiation of ui
Run the code with the command:
python3 temphum.py

Project Work:
This Application is a GUI that monitots temperature and humidity sensed using Adafruit DHT22 and Raspberry Pi3.
The data pin of the sensor is connected to GPIO pin 4. The GUI displays recorded temperature and humidity. It also
displays timestamp of last time the temp and humidity were refreshed. The application also handels sensor not being
connected by displaying the status of the sensor.

Project Additions:
Additional Features implemented:
1. The application calculates average continuously and displays it
2. Graph button displays the recorded values against time. It also plots the average value in the plot.
3. Alerts have been implemented when the temp or humidity on exceeds either the lower or upper limit set for
   temperature or humidity, an alert is displayed on the GUI. User also can select its limits for alerts
4. Humidity and Temperature are displayed graphically showing the values as a percentage of the limit values set
