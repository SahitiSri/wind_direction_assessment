from config import NREL_API_KEY, EMAIL
import requests
import pickle


class Point:
    latitude: float = 23.344315
    longitude: float = 85.296013

    @classmethod
    def wkt(cls) -> str:
        return f"POINT({Point.longitude} {Point.latitude})"


def main():
    base_url = "https://developer.nrel.gov/api/wind-toolkit/v2/wind/india-wind-download.csv"

    attributes_needed = [
        "pressure_40m",
        "temperature_100m",
        "temperature_120m",
        "temperature_40m",
        "temperature_80m",
        "winddirection_100m",
        "winddirection_120m",
        "winddirection_40m",
        "winddirection_80m",
        "windspeed_100m",
        "windspeed_120m",
        "windspeed_40m",
        "windspeed_80m",
        "pressure_100m",
    ]

    wkt = "POINT(23.344315 85.296013)"

    parameters = {
        "api_key": NREL_API_KEY,
        "wkt": wkt,
        "attributes": attributes_needed,
        "names": 2014,
        "email": EMAIL,
    }

    response = requests.get(base_url, params=parameters)

    print(response.url)
    print(response)

    if response.ok:
        with open("./data_2021.csv", "w") as f:
            f.write(response.content)

        with open("./response.pkl", "wb") as file_:
            pickle.dump(response, file_)

main()

