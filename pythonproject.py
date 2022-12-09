

'''Expeditious Weather Project

    Final Python Project

    Author: Ariel Johnston
    
<johnston.ariel2004@gmail.com>'''


#Packages
import requests
import turtle


#Introduction

#implement while loop :)

w = 5

Introduction = "Hello, Welcome to Expeditious Weather!"

while w > 0:
    
    print(w)
    print()
    w = w - 1
    
print(Introduction.center(75, '~'))

print()
print()
print()

#OpenWeatherMap API

api_key = "475954306fae6bc32d36d9674b2f507c"

root_url = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter your city: ")

url = f"{root_url}appid={api_key}&q={city}&units=imperial"

r = requests.get(url)

#data from OpenWeather

print(r.json())

data = r.json()

#formatting
print()
print()
print()

#base data for input city 
if data['cod'] == 200:
    
    temp = data['main']['temp']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    descr = data['weather'][0]['description']
    wind = data['wind']['speed']
    
    print(f"City Name: {city}")
    print()
    print(f"The weather condition is {descr}")
    print()
    print(f"The temperature is {temp} degrees")
    print()
    print(f"The pressure is {pressure}hPa")
    print()
    print(f"The humidity is {humidity}%")
    print()

else:
    print("Oh no! An Error Occured.")
    
print()


#Temperature
temp = data['main']['temp']

feels_like = data['main']['feels_like']

max_temp = data['main']['temp_max']

min_temp = data['main']['temp_min']

pressure = data['main']['pressure']

humidity = data['main']['humidity']

descr = data['weather'][0]['description']

#wind
wind = data['wind']['speed']

degree = data['wind']['deg']

visibility = data['visibility']


#Location
timezone = data['timezone']

country = data['sys']['country']

lat = data['coord']['lat']

long = data['coord']['lon']

coordinates = data['coord']

        


def commands():
    '''prints command functions available'''
    print()
    print('new_city')
    print()
    print('city_name')
    print()
    print('country')
    print()
    print('condition')
    print()
    print('temperature')
    print()
    print('temp_descr')
    print()
    print('real_feel')
    print()
    print('temp_and_real_feel')
    print()
    print('humidity')
    print()
    print('description')
    print()
    print('max_temp')
    print()
    print('min_temp')
    print()
    print('min_and_max')
    print()
    print('wind_speed')
    print()
    print('wind_gust')
    print()
    print('wind_degree')
    print()
    print('wind_direction')
    print()
    print('all_wind')
    print()
    print('wind_compass')
    print()
    print('pressure')
    print()
    print('visibility')
    print()
    print('is_raining')
    print()
    print('is_snowing')
    print()
    print('is_cloudy')
    print()
    print('is_clear')
    print()
    print('timezone')
    print()
    print('latitude')
    print()
    print('longitude')
    print()
    print('coordinates')
    print()
    print('This completes the list')

    
question = input("Would you like to see the commands? y/n: ")
if question == 'y':
    print(commands())
else:
    print()
    print("Enjoy!")
    print()
    print("you can enter your commands below :)")
    print()

    
print()
print()


def new_city():
    '''changes city'''
    
    api_key = "475954306fae6bc32d36d9674b2f507c"

    root_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    print()
    city = input("Enter your city: ")
    print()

    url = f"{root_url}appid={api_key}&q={city}&units=imperial"

    r = requests.get(url)

    print(r.json())

    data = r.json()

    print()
    print()
    print()

        
def city_name():
    '''returns name of city in proper form'''
    name = data['name']
    return name.title()


def condition():
    '''prints weather condition of input city'''
    descr = data['weather'][0]['description']
    print(f'The weather condition of {city} is {descr}.')
    


class Temperature(object):
    '''temperature class'''

    def __init__(self, temperature, real_feel, max_temp, min_temp):
        '''initializes temperatures'''
        self.temperature = temperature
        self.real_feel = real_feel
        self.max_temp = max_temp
        self.min_temp = min_temp

    def __str__(self):
        string = "Temperature: "+str(self.temperature)+", Real feel: "+str(self.real_feel)+", Max Temp: "+str(self.max_temp)+", Min Temp: "+str(self.min_temp)
        return string

    def high_low(self):
        '''high and low temps'''
        high_low = self.max_temp + "/" + self.min_temp
        return high_low
        

#temperature
    
def temperature():
    '''prints current temperature in city'''
    temp = data['main']['temp']
    print(f"The current temperature in {city} is {round(temp)} degrees")
    
                  
def real_feel():
    '''retrieves the real feel temperature of city'''
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    
    if feels_like == temp:
        print(f"The real feel temperature is the same as the actual temperature.")
        print(f"{round(feels_like)} degrees fahrenheit")
        
    elif feels_like > temp:
        print(f"The real feel temperature is warmer than the actual temperature.")
        print(f"{round(feels_like)} degrees fahrenheit")
        
    else:
        print(f"The real feel temperature is cooler than the actual temperature.")
        print(f"{round(feels_like)} degrees fahrenheit")


def humidity():
    '''prints humidty of input city'''
    humidity = data['main']['humidity']
    print(f"The humidity is {humidity}%")

    
def description():
    '''prints weather description'''
    descr = data['weather'][0]['description']
    print(f"The weather condition is {descr}")

    
def temp_and_real_feel():
    ''' prints the temperature and the feel like temperature'''
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    
    print(f"The actual temperature in {city} is {round(temp)} degrees fahrenheit")
    
    if feels_like == temp:
        print(f"The real feel temperature is the same as the actual temperature.")
        print(f"{round(feels_like)} degrees fahrenheit")
        
    elif feels_like > temp:
        print(f"The real feel temperature is warmer than the actual temperature.")
        print(f"{round(feels_like)} degrees fahrenheit")
        
    else:
        print(f"The real feel temperature is cooler than the actual temperature.")
        print(f"{round(feels_like)} degrees fahrenheit")
    
    
def max_temp():
    '''prints the maximum temperature of the city'''
    max_temp = data['main']['temp_max']
    print(f"The maximum temperature in {city} is {round(max_temp)} degrees fahrenheit.")


def min_temp():
    '''prints the minimum temperature of the city'''
    min_temp = data['main']['temp_min']
    print(f"The minimum temperature in {city} is {round(min_temp)} degrees fahrenheit.")


def min_and_max():
    '''prints the minimum and the maxiumum temperature of input city'''
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    print(f"{round(min_temp)}"+"/"+f"{round(max_temp)}")

#wind
def wind_speed():
    '''retrieves current wind speed of city'''
    wind = data['wind']['speed']
    print(f"The wind speed in {city} is {round(wind)} mph")


def wind_degree():
    '''prints the degree wind is going'''
    degree = data['wind']['deg']
    print(f"The wind degree in {city} is {degree}.")


def wind_direction():
    wind_degree = data['wind']['deg']
    
    if wind_degree == 0:
        print("The wind is going due North")
        
    elif wind_degree == 90:
        print("The wind is going due East")
        
    elif wind_degree == 180:
        print("The wind is going due South")
        
    elif wind_degree == 270:
        print("The wind is going due West")
        
    elif wind_degree > 0 and wind_degree < 90:
        print("The wind is going NorthEast")
        
    elif wind_degree > 90 and wind_degree < 180:
        print("The wind is going SouthEast")
        
    elif wind_degree > 180 and wind_degree < 270:
        print("The wind is going SouthWest")
        
    elif wind_degree > 270 and wind_degree < 364:
        print("The wind is going NorthWest")
        
    else:
        print("No information at this time")

def wind_compass():
    deg = data['wind']['deg']
    screen = turtle.Screen()
    screen.setup(750, 750)
    compass = turtle.Turtle()
    compass.shape("arrow")
    compass.pencolor("white")
    compass.pensize(10)
    screen.addshape("image.gif")
    compass.shape("image.gif")
    compass.penup()
    compass.rt(deg + 90)
    compass.pendown()
    compass.forward(300)
    
    

def all_wind():
    '''prints wind speed, wind gusts, and wind direction'''
    wind = data['wind']['speed']
    wind_degree = data['wind']['deg']
    print(f"The wind speed is {round(wind)} mph")
    return wind_direction()


def wind_list():
    '''wind list'''
    wind_list = [ ]
    wind_list.append(wind_speed())
    wind_list.append(wind_degree())
    wind_list.append(wind_direction())
    return wind_list



def pressure():
    '''prints pressure in city in inHg'''
    pressure = data['main']['pressure']
    print(f"The pressure in {city} is {round(pressure)}")


def temp_descr():
    while temp > 70:
        print(f"It is warm in {city} at {round(temp)} degrees.")
    print(f"It is not too warm in {city} at {round(temp)} degrees.")

    
def weather_list(t):
    '''prints list with given parameters'''
    return t


def is_raining():
    rain = data['weather'][0]['main']
    if rain == 'Rain':
        return True
    else:
        print(f"No, the condition is {rain}.")


def visibility():
    '''visibility in city'''
    visibility = data['visibility']
    print(f'The visibility in {city} is {visibility}.')
    

def country():
    '''prints the country which city is located'''
    country = data['sys']['country']
    print(f"{city} is located in {country}")

    
def timezone():
    '''prints timezone of city'''
    timezone = data['timezone']
    
    if timezone == -18000:
        print(f"{city} timezone is EST")
        
    elif timezone == -21600:
        print(f"{city} timezone is CST")
        
    elif timezone == 0:
        print(f"{city} timezone is UTC")
        
    elif timezone == +10800:
        print(f"{city} timezone is EAT")
        
    elif timezone == +3600:
        print(f"{city} timezone is CET or WAT")
        
    elif timezone == +7200:
        print(f"{city} timezone is CAT or EET")
        
    elif timezone == -36000:
        print(f"{city} timezone is HST")
        
    elif timezone == -14400:
        print(f"{city} timezone is AST")
        
    elif timezone == -32400:
        print(f"{city} timezone is AKST")
        
    elif timezone == -25200:
        print(f"{city} timezone is MST")
        
    elif timezone == -12600:
        print(f"{city} timezone is NST")
        
    elif timezone == -28800:
        print(f"{city} timezone is PST")
        
    elif timezone == +39600:
        print(f"{city} timezone is AEDT")
        
    elif timezone == +46800:
        print(f"{city} timezone is NZDT")
        
    elif timezone == +28800:
        print(f"{city} timezone is HKT, AWST or CST")
        
    elif timezone == +25200:
        print(f"{city} timezone is WIB")
        
    elif timezone == +32400:
        print(f"{city} timezone is WIT, JST, or KST")
        
    elif timezone == +7200:
        print(f"{city} timezone is IST")
        
    elif timezone == +18000:
        print(f"{city} timezone is PKT")
        
    elif timezone == +37800:
        print(f"{city} timezone is ACDT")
        
    elif timezone == +36000:
        print(f"{city} timezone is AEST, ChST")
        
    elif timezone == +34200:
        print(f"{city} timezone is ACST")
        
    elif timezone == -39600:
        print(f"{city} timezone is SST")
        
    else:
        print("Sorry, no data at this time.")
        

def is_snowing():
    '''returns if snowing'''
    snow = data['weather'][0]['main']
    if snow == 'Snow':
        return True
    else:
        print(f"No, the condition is {snow}.")
    
    

    
def latitude():
    '''returns latitude '''
    lat = data['coord']['lat']
    return lat

    
def longitude():
    '''returns longitude of city'''
    long = data['coord']['lon']
    return long


def coordinates():
    '''returns coordinates'''
    coordinates = data['coord']
    return coordinates


def is_cloudy():
    '''returns if it is cloudy'''
    cloudy = data['weather'][0]['main']
    if cloudy == 'Clouds':
        return True
    else:
        print(f"No, it is {cloudy}.")

def is_clear():
    '''returns if there are no clouds'''
    clear = data['weather'][0]['main']
    if clear == 'Clear':
        return True
    else:
        print(f"No, it is {clear}.")
    
    
    
    

    






























































