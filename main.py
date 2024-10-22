import requests
import datetime
import os
import login_to_spotipy as log


from bs4 import BeautifulSoup


def get_input_from_user():
    # get the input from a user
    input_year = int(input("Which year you want to travel? YYYY format: ") )
    input_month = int(input("Which month? MM format: "))
    input_day = int(input("Which day? DD format: "))
    return datetime.datetime(input_year,input_month,input_day)

def default_input():
    # geting the same input for faster execution
    input_year = 2004
    input_month = 3
    input_day= 12
    return datetime.datetime(input_year, input_month, input_day)

URL="https://www.billboard.com/charts/hot-100/"



def get_the_list():
    # gets the list form billboard
    date = default_input()

    billboard_parameters = {
        "date": date.strftime("%Y-%m-%d")
    }

    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

    response = requests.get(url=f"{URL}{billboard_parameters["date"]}", headers=header)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    billboard_100 = soup.select(selector="li ul li h3")

    return [song.getText().strip() for song in billboard_100]

# songs_list = get_the_list()

sp = log.logintospotipy(clientid=os.environ['CLIENTID'], clientsecret=os.environ['CLIENTSECRET'])

print(sp.current_user())

