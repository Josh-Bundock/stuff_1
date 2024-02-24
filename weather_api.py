import requests

def get_weather(city):
    api_key = '0a037f84722cbe767d1e03de5bbfce62'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Failed to fetch weather data.')
        return None

def display_weather(data):
    if data:
        city = data['name']
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        
        print(f'Weather in {city}:')
        print(f'Description: {weather_desc}')
        print(f'Temperature: {temp}°C')
        print(f'Humidity: {humidity}%')
    else:
        print('No weather data available.')


while True:
    city_choice = input('Enter a city or [q] to quit: ')
    if city_choice == 'q':
        quit()
    weather_data = get_weather(city_choice)
    display_weather(weather_data)


