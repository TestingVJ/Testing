import requests
from datetime import datetime

def get_corona_report():
    url = "https://api.covid19api.com/summary"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        global_data = data['Global']
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report = (
            f"Corona Report as of {date}\n"
            f"New Confirmed: {global_data['NewConfirmed']}\n"
            f"Total Confirmed: {global_data['TotalConfirmed']}\n"
            f"New Deaths: {global_data['NewDeaths']}\n"
            f"Total Deaths: {global_data['TotalDeaths']}\n"
            f"New Recovered: {global_data['NewRecovered']}\n"
            f"Total Recovered: {global_data['TotalRecovered']}\n"
        )
        print(report)
    else:
        print("Failed to retrieve data")

if __name__ == "__main__":
    get_corona_report()
