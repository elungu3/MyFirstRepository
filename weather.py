import requests
import smtplib
from email.message import EmailMessage

API_KEY = "2c5566e8c5767f91b868700fa899885e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city1 = "Bucharest"
city2 = "Timisoara"
city3 = "Helsinki"

request_url1 = f"{BASE_URL}?appid={API_KEY}&q={city1}"
request_url2 = f"{BASE_URL}?appid={API_KEY}&q={city2}"
request_url3 = f"{BASE_URL}?appid={API_KEY}&q={city3}"

response1 = requests.get(request_url1)
response2 = requests.get(request_url2)
response3 = requests.get(request_url3)


def weather_fct():
    if response1.status_code == 200 and response2.status_code == 200 and response3.status_code == 200:
        data1 = response1.json()
        data2 = response2.json()
        data3 = response3.json()

        weather1 = data1['weather'][0]['description']
        weather2 = data2['weather'][0]['description']
        weather3 = data3['weather'][0]['description']

        temperature1 = int(data1['main']['temp'] - 273.15)
        temperature2 = int(data2['main']['temp'] - 273.15)
        temperature3 = int(data3['main']['temp'] - 273.15)

        country1 = data1['sys']['country']
        country2 = data2['sys']['country']
        country3 = data3['sys']['country']

        city11 = "Weather in {} is: {}.".format(city1, weather1)
        city12 = "Temperature in {} is: {} celcius".format(city1, temperature1)
        city13 = "Country: {}".format(country1)

        city21 = "Weather in {} is: {}.".format(city2, weather2)
        city22 = "Temperature in {} is: {} celcius".format(city2, temperature2)
        city23 = "Country: {}".format(country2)

        city31 = "Weather in {} is: {}.".format(city3, weather3)
        city32 = "Temperature in {} is: {} celcius".format(city3, temperature3)
        city33 = "Country: {}".format(country3)

        forcity1 = "{}\n{}\n{}".format(city11, city12, city13)
        forcity2 = "{}\n{}\n{}".format(city21, city22, city23)
        forcity3 = "{}\n{}\n{}".format(city31, city32, city33)
        msg = EmailMessage()
        msg.set_content('{}\n\n{}\n\n{}'.format(forcity1, forcity2, forcity3))
        msg['Subject'] = 'Your weather notification'
        msg['From'] = "notificationstoyou@gmail.com"
        msg['To'] = "andreeatarantus@yahoo.com"
        # print(msg.set_content)
        # Send the message via our own SMTP server.
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("notificationstoyou@gmail.com", "p0pcornparola!")
        server.send_message(msg)
        server.quit()

    else:
        print("There was an error")


weather_fct()
