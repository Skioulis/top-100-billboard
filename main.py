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



def get_the_list(input_date):
    # gets the list form billboard
    date = input_date

    billboard_parameters = {
        "date": date.strftime("%Y-%m-%d")
    }

    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

    response = requests.get(url=f"{URL}{billboard_parameters["date"]}", headers=header)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    billboard_100 = soup.select(selector="li ul li h3")

    return [song.getText().strip() for song in billboard_100]


desired_date = get_input_from_user()

# to be deleted --------------------------------------



# UP TO HERE --------------------------------------------
songs_list = get_the_list(desired_date)
year = desired_date.strftime("%Y")
sp = log.logintospotipy(clientid=os.environ['CLIENTID'], clientsecret=os.environ['CLIENTSECRET'])
user_id = sp.current_user()['id']

song_uris = []

for song in songs_list:
    result = sp.search(q=f"track: {song} year: {year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{desired_date.strftime('%Y-%m-%d')} Billboard 100", public=False)



sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


