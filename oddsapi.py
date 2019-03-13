import json
import requests

# An api key is emailed to you when you sign up to a plan
api_key = 'bad01aed73a13af7ead252b4a4c1d743'

# To get odds for a sepcific sport, use the sport key from the last request
#   or set sport to "upcoming" to see live and upcoming across all sports
sport_key = 'rugbyleague_nrl'

odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params={
    'api_key': api_key,
    'sport': sport_key,
    'region': 'au', # uk | us | au
    'mkt': 'h2h' # h2h | spreads | totals
})



#
# json from web
odds_json = json.loads(odds_response.text)
if not odds_json['success']:
    print(
        'There was a problem with the odds request:',
        odds_json['msg']
    )

else:
    # odds_json['data'] contains a list of live and 
    #   upcoming events and odds for different bookmakers.
    # Events are ordered by start time (live events are first)
    print()
    
    for event in odds_json['data']:
        print (event)
        #json.dump(event, f)
        #print(odds_json['data'][0])
        
    # Check your usage
    print()
    print('Remaining requests', odds_response.headers['x-requests-remaining'])
    print('Used requests', odds_response.headers['x-requests-used'])
