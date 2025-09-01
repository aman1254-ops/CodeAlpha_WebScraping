import requests
from bs4 import BeautifulSoup
import csv

# URL of the website
url = "https://www.timeanddate.com/weather/india/delhi"

# Send a request to fetch the content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract weather details
location = soup.find("h1").text.strip()
temperature = soup.find("div", class_="h2").text.strip()
condition = soup.find("p").text.strip()

# Save data into CSV
with open("weather_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Location", "Temperature", "Condition"])
    writer.writerow([location, temperature, condition])

print("Weather data saved to weather_data.csv")
