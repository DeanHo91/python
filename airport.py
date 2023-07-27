import random
import time

time_str = '00:00'
airlines = ['Lufthansa', 'British Airways', 'Ryanair', 'Easyjet']
flightboard = []

for i in range(10):
    airline = random.choice(airlines)
    flight_number = random.randint(1000, 9999)
    departure_time = time.strftime('%H:%M', time.localtime(random.randint(36000, 54000)))
    arrival_time = time.strftime('%H:%M', time.localtime(random.randint(57600, 72000)))
    status = random.choice(['On time', 'Delayed', 'Cancelled'])
    flightboard.append([airline, flight_number, departure_time, arrival_time, status])

print(flightboard)
