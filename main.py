## @package main
#Biblioteki zawierające potrzebne klasy, metody funkcje do działania czujników i wyświetlacza
#
#W tym pliku następuje inicjalizacja czujników. Znajduje się tu także nieskończona pętla w #której szczytywane są z nich informacje.
#
import adafruit_blinka
import gpiozero
import costam


TempSensor.DHT11Init()
PressSensor.BMP108Init()
RainSensor.YL83Init()
Scr.NX4832Init()
Wind.anemometerInit()
DBInit()


while True;
	TempSensor.readDHT11Temperature()
	TempSensor.readDHT11Humidity()
	Photos.readPhotoresistor()
	PresSensor.readBMP180Preasure()
	RainSensor.readYL83RainLevel()
	Wind.readAnemometerWind()
	Scr.NX4832UpdateData()
	Scr.NX4832Refresh()
	connectToDB()
	sendDataToDB()
	readDataFromDB()
