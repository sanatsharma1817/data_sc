import requests
import pandas as pd

API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "bd5e378503939ddaee76f12ad7a97608"

#  we wil  fetch weather data frm api here using params as city and api and unit for degree
def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(API_URL, params=params, timeout=15)
    response.raise_for_status()
    return response.json()

# converting json itno dat a
def weather_to_dataframe(data):
    weather_data = {
        "city": [data.get("name")],
        "weather": [data.get("weather", [{}])[0].get("description")],
        "temperature": [data.get("main", {}).get("temp")],
        "feels_like": [data.get("main", {}).get("feels_like")],
        "humidity": [data.get("main", {}).get("humidity")],
        "pressure": [data.get("main", {}).get("pressure")],
        "wind_speed": [data.get("wind", {}).get("speed")]
    }

    df = pd.DataFrame(weather_data)
    return df

def main():
    print("----API Project---- ")
    city = input("Enter city name : ")
    try:
        # here we call the api and api wil fetch the details foru us okah
        data = fetch_weather(city)
        print("\nweather api response fetched successfully")

        print("\njson response keys")
        print(list(data.keys()))

        # convertinng  to datafrme
        weather_df = weather_to_dataframe(data)

        print("\nweather data in table format")
        print(weather_df.to_string(index=False))

        # req info of data a
        print("\napi request details")

        request_df = pd.DataFrame([{
            "method": "GET",
            "city": city,
            "status": "success"
        }])

        print(request_df.to_string(index=False))

    except requests.exceptions.HTTPError as e:
        print("\nhttp error :", e)

    except requests.exceptions.RequestException as e:
        print("\nrequest error :", e)

    except Exception as e:
        print("\nunexpected error :", e)


if __name__ == "__main__":
    main()