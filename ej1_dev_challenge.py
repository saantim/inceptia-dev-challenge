import requests
      
class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
    LIMIT_TEMP = 28

    @classmethod
    def is_hot_in_pehuajo(cls):
        try:
            response = requests.get(cls.URL)
            curr_temp = response.json()["main"]["temp"]
            return curr_temp > cls.LIMIT_TEMP

        except (requests.exceptions.RequestException, KeyError):
            return False

if __name__ == "__main__":
    print(GeoAPI.is_hot_in_pehuajo())
