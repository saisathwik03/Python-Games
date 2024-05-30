import random

def temperature():
    return random.randint(-16, 47)

def humidity_random():
    return random.randint(20, 70)

def weather():
    l = ['sunny day', 'rainy day', 'cloudy day']
    return random.choice(l)

def daily_forecasts():
    days=int(input("Enter no of days to forecast: "))
    forecasts=[]
    for i in range(1,days+1):
        T=temperature()
        H=humidity_random()
        W=weather()

        result={'Day':i,'temperature':T,'Humidity':H,'Weather':W}
        forecasts.append(result)
    return forecasts

def statistical_forecast():
    days=int(input("Enter no of days to forecast: "))
    forecasts=[]
    for i in range(1,days+1):
        T=temperature()
        H=humidity_random()
        W=weather()

        result={'Day':i,'temperature':T,'Humidity':H,'Weather':W}
        forecasts.append(result)
    
    temperatures=[]
    for temp in forecasts:
        temperatures.append(temp['temperature'])
    
    humidity=[]
    for humid in forecasts:
        humidity.append(humid['Humidity'])
    
    max_temp=max(temperatures)
    min_temp=min(temperatures)
    max_humid=max(humidity)
    min_humid=min(humidity)
    avg_temp=sum(temperatures)/len(temperatures)
    avg_humid=sum(humidity)/len(humidity)

    print("\nStatistical Summary:")
    print("Maximum Temperature: " + str(max_temp) + "°C")
    print("Minimum Temperature: " + str(min_temp) + "°C")
    print("Average Temperature: " + str(avg_temp) + "°C")
    print("Maximum Humidity: " + str(max_humid) + "%")
    print("Minimum Humidity: " + str(min_humid) + "%")
    print("Average Humidity: " + str(avg_humid) + "%")

def forecast_menu():
    while True:
        print('\nMenu:')
        print('1. Show daily forecast')
        print('2. Show Statistical summary')
        print('3. Exit')

        choice=input("Enter Choice 1/2/3: ")

        if choice=='1':
            forecasts = daily_forecasts()
            for forecast in forecasts:
                print(forecast)
        elif choice=='2':
            statistical_forecast()
        elif choice=='3':
            print('Exiting the PyWeather Sim!!!')
            break
        else:
            print("Inavalid choice!!")

forecast_menu()  