import time
import adafruit_dht
import board
from datetime import date

sensor1file = open("DHTsensor1.txt", "a")
sensor2file = open("DHTsensor2.txt", "a")
finalfile = open("AveragedDate.txt", "a")

dht_device = adafruit_dht.DHT22(board.D22)
dht2_device = adafruit_dht.DHT22(board.D21)

while True:
    try:
        #DHT Sensor 1
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        hum = dht_device.humidity

        #DHT Sensor 2
        temperature_c2 = dht2_device.temperature
        temperature_f2 = temperature_c2 * (9 / 5) + 32
        hum2 = dht2_device.humidity

        #Averaging the two
        finaltemp_c = (temperature_c2 + temperature_c) / 2
        finaltemp_f = (temperature_f + temperature_f2) / 2
        finalhum = (hum + hum2) / 2

        #Time and date
        current_time = time.strftime("%H:%M:%S")
        today = date.today()

        #Adding to Files
        sensor1file.write(f"{current_time} , {today} , {temperature_c} , {temperature_f} , {hum} \n")
        sensor2file.write(f"{current_time} , {today} , {temperature_c} , {temperature_f} , {hum} \n")
        finalfile.write(f"{current_time} , {today} , {finaltemp_c} , {finaltemp_f} , {finalhum} \n")

        #file.write("{current_time}{today}{:.1f} {:.1f} \n {}.format")
        #file.write("{current_time}{today}{:.1f} {:.1f} \n {}".format(temperature_c, temperature_f, humidity))

        #right before Temp:{:.1f} then {:.1f} F \n Humidty: {}%"

        #Temp:{:.1f} c / {:.1f} F \n Humidty: {}%".format(temperature_c, temperature_f, humidity)
    except RuntimeError as err:
        print(err.args[0])
    time.sleep(300)

sensor1file.close
sensor2file.close
finalfile.close