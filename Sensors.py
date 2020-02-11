from sense_hat import SenseHat
import datetime
import subprocess
sense = SenseHat()
pressure=sense.get_pressure()
temp=sense.get_temperature()
humidity=sense.get_humidity()
temp_hum=sense.get_temperature_from_humidity()
temp_press=sense.get_temperature_from_pressure()
CurrentTime=datetime.datetime.now()
cpu_temp=float(subprocess.check_output("cat /sys/class/thermal/thermal_zone*/temp", shell=True))/1000
print([CurrentTime, temp, pressure, temp_press, humidity, temp_hum, cpu_temp])
with open('file.txt','a') as f:
    print([CurrentTime, temp, pressure, temp_press, humidity, temp_hum, cpu_temp], file=f)
