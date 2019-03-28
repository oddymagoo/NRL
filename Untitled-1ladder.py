
import json
import requests

URI = 'https://allsportdb-com.p.rapidapi.com/gamestypes/'

api_key= 'd8b41d0410msha65c763b7239e62p1c3921jsn0881d752172a'


r = requests.get(URI, params={
    'X-RapidAPI-Key': 'default-application_3729153',
    'api_key': api_key,
})

print (r.text)