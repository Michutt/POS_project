## @package costam
# Plik zawierający definicje funkcji
#
#

class TempSens:
	
	def __init__(self):
		self.temp=0
		self.hum=0
	def DHT11Init():
		self.sensor=True
	def readDHT11Temperature():
		self.temp=temperatura
	def readDHT11Humidity():
		self.hum=humidity
class PressSens:
	def __init__(self):
		self.press=0
	def BMP108Init()
		self.sensor=True	
	def readBMP180Pressure():
		self.press=pressure	

class PhotoRes:
	def __init__(self):
		self.light=0
	def readPhotoresistor():
		self.light=lig

class RainSens:
	def __init__(self):
		self.rain=0
	def YL83Init():
		self.sensor=True
	def readYL83RainLevel():
		self.rain=meas

class Screen:
	def NX4832Init():
		self.screen=True
	def NX4832UpdateData():
		self.output=data		
	def NX4832Refresh():
		sendData()


class WindSens:
	def __init__(self):
		self.wind=0
		self.direct="None"
	def anemometerInit():
		self.sensor=True
	def readAnemometerWind():
		self.wind=measWind
		self.direct=windDir
		
		
def DBInit():
def connectToDB():
def sendDataToDB():
def readDataFromDB():



