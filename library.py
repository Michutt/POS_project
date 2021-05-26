## @package library
# Plik zawierający definicje klas i funkcji
#
#

##Klasa czujnika temperatury i wilgotności
class TempSens:
	##Konstruktor
	def __init__(self):
		##Temperatura 
		temp=0
		##Wilgotność
		hum=0
	def DHT11Init():
		##Właczenie czujnika
		sensor=True
	def readDHT11Temperature():
		##Odczytanie temperatury na wejsciu i przypisanie 			do zmiennej
		temp=temperatura
	def readDHT11Humidity():
		##Odczytanie wilgotnosci na wejsciu i przypisanie 			do zmiennej
		hum=humidity

##Klasa czujnika ciśnienia
class PressSens:
	##Konstruktor
	def __init__(self):
		##Cisnienie podczas inicjalizacji
		press=0
	def BMP108Init()
		##Włączenie czujnika
		sensor=True	
	def readBMP180Pressure():
		##Odczytanie wartosci cisnienia i przypisanie do 			zmiennej
		press=pressure	

##Klasa fotorezystora
class PhotoRes:
	##Konstruktor
	def __init__(self):
		##Natezenie swiatla
		light=0
	def readPhotoresistor():
		##Odczytanie napiecia na fotorezystorze i 			przekształcenie tego na natęzenie 
		light=formula*V

##Klasa czujnika opadów
class RainSens:
	##Konstruktor
	def __init__(self):
		##Ilosc opadow
		rain=0
	def YL83Init():
		##Włączenie czujnika
		sensor=True
	def readYL83RainLevel():
		##Odczytanie wartości z czujnika i przypisanie do 			zmiennej
		rain=meas

##Klasa wyświetlacza
class Screen:
	##Konstruktor
	def __init__(self):
		##Dane na czujnikow podczas inicjalizacji
		output=""
	def NX4832Init():
		##Włączenie ekranu
		screen=True
	def NX4832UpdateData():
		##Odczyt danych z czujnikow i przygotowanie do 		wysłania na wyswietlacz
		output=data		
	def NX4832Refresh():
		##Wyslanie danych na wyswietlacz
		sendData()


##Klasa czujnika wiatru
class WindSens:
	
	##Konstruktor
	def __init__(self):
		##Predkosc wiatru
		wind=0
		##Kierunek wiatru
		direct="None"
	def anemometerInit():
		##Właczenie czujnika
		sensor=True
	def readAnemometerWind():
		##Odczytanie predkosci wiatru i przypisanie do 		zmiennej	
		wind=measWind
		##Odczytanie kierunku wiatru i przypisanie do 		zmiennej
		direct=windDir
		
##Inicjalizacja bazy danych
def DBInit():
##Połączenie z bazą danych
def connectToDB():
##Wysłanie danych do bazy
def sendDataToDB():
##Odczytanie danych z bazy
def readDataFromDB():



