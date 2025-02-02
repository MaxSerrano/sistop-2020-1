import random
from time import sleep
# from aicm.airplane import Airplane
from aicm.landing_track import LandingTrack,LandingPriority
from aicm.operator import Operator
from aicm.passenger import Passenger, PassengerType
from aicm.bus import Bus 
from aicm.scooter import Scooter

origin_cities = ["BUD","WSW","PRH","KRW"]
airlines = ["AeroMexico","AirCanada","Lufthansa"]
numbers = ["001","244","981","987","763","124"]
percentages = [10,20,50,60,75,80]
names = ["Juan","Ramiro","Jose","Ana","Lolita","Lourdes","Ramon","Paola"]
ages = [5,8,10,12,16,18,25,34,40,54,65,70,78,90]

class AirportGenerator():	

	def __init__(self):
		pass

	def generate_planes(self,n):
		global origin_cities,airlines,numbers,percentages
		planes = []
		for i in range(n):
			c = random.randint(0,len(origin_cities)-1)
			a = random.randint(0,len(airlines)-1)
			n = random.randint(0,len(numbers)-1)
			p = random.randint(0,len(percentages)-1)
			origin = origin_cities[c]
			destination = "CDMX"
			airline = airlines[a]
			no = numbers[n]
			percentage = percentages[p]
			passengers = self.generate_passengers(origin,destination)
			p = Airplane(i+1,origin=origin,destination=destination,airline=airline,flight_no=no,fuel_percentage=percentage,passengers=passengers,priority=LandingPriority.normal)
			planes.append(p)
		return planes

	def generate_operators(self,n):
		ops = []
		for i in range(n):
			operator = Operator(i+1)
			ops.append(operator)
		return ops 

	def generate_passengers(self,origin,destination):
		global names,ages
		num = random.randint(1,10)
		passengers = []
		for i in range(num):
			n = random.randint(0,len(names)-1)
			a = random.randint(0,len(ages)-1)
			name = names[n]
			age = ages[a]
			p_type = self.determine_type(age)
			passengers.append(Passenger(name=name,age=age,origin=origin,destiny=destination,passenger_type=p_type))
		return passengers

	def determine_type(self,age):
		if age < 17:
			return PassengerType.child 
		elif age >= 17 and age < 65:
			return PassengerType.adult
		else:
			return PassengerType.old

	def generate_landing_tracks(self,n):
		tracks = []
		for i in range(n):
			t = LandingTrack(id=i)
			t.start()
			tracks.append(t)
		return tracks 

	def generate_buses(self,n):
		buses = []
		for i in range(n):
			b = Bus(id=i)
			b.start()
			buses.append(b)
		return buses 

	def generate_scooters(self,n):
		scooters = []
		for i in range(n):
			s = Scooter(id=i)
			scooters.append(s)
			sleep(1)
			s.start()
		return scooters 

	def generate_origin(self):
		global origin_cities 
		return origin_cities[random.randint(0,len(origin_cities)-1)]

	def generate_fuel_percentage(self):
		global percentages
		return percentages[random.randint(0,len(origin_cities)-1)]
