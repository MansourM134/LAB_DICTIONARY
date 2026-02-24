weather_dict = {}
def input_weather():
    city = input("please input city name:")
    date = input("please input weather date:")
    temperature = int(input("please input temperature:"))
    humidity = int(input("please input humidity:"))
    weather_condition = input("please input weather condition:")

    if city not in weather_dict:
        weather_dict[city] = {}

    weather_dict[city][date] = {"temperature":temperature,"humidity":humidity,
                          "weather_condition":weather_condition}

def weather_query():
    city = input("input city name:")
    if city in weather_dict:
        print(weather_dict[city])
    else :
        print("city not found")


def update_weather():
        city = input("please input city name:")
        if city not in weather_dict:
            print("city not found")
            return
        
        date = input("please input weather date:")
        if date not in weather_dict[city]:
            print("date not found")
            return
        
        new_temperature = int(input("please input temperature:"))
        new_humidity = int(input("please input humidity:"))
        new_weather_condition = input("please input weather condition:")

        weather_dict[city][date] = {"temperature":new_temperature,"humidity":new_humidity,
                          "weather_condition":new_weather_condition}

def delete_weather():
        city = input("please input city name:")
        if city not in weather_dict:
            print("city not found")
            return
        
        date = input("please input weather date:")
        if date not in weather_dict[city]:
            print("date not found")
            return
        else:
            del weather_dict[city][date]
            print("date has been deleted")



def interface():
    while True:
        user_input = input("choose " \
        "1 to see weather in your city," \
        "\n2 to add a city," \
        "\n3 to update weather"
        "\n4 to delete weather: ")
        if user_input == "1":
            weather_query()
        elif user_input == "2":
            input_weather()
        elif user_input =="3":
            update_weather()
        elif user_input =="4":
            delete_weather()
        else :
            print("invalid input try again")






interface()

