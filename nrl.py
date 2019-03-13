#from bs4 import BeautifulSoup
import json
import requests
#from requests_html import HTMLSession

#if using requests_html:
#session = HTMLSession()
#r = session.get(superCoachStatsURL)
#r.html.render()

#arrTeamInfo format
    # Team Abbreviation     abbrName
    # Full Name             teamName
    # Total Price           totalPrice
    # Odds Average          oddsAvg

arrTeamInfo = [
    ['BRO', 'Brisbane Broncos', 0, 0],
    ['BUL', 'Canterbury Bulldogs', 0, 0],
    ['CBR', 'Canberra Raiders', 0, 0],
    ['GCT', 'Gold Coast Titans', 0, 0],
    ['MEL', 'Melbourne Storm', 0, 0],
    ['MNL', 'Manly Warringah Sea Eagles', 0, 0],
    ['NEW', 'Newcastle Knights', 0, 0],
    ['NQC', 'North Queensland Cowboys', 0, 0],
    ['NZL', 'New Zealand Warriors', 0, 0],
    ['PAR', 'Parramatta Eels', 0, 0],
    ['PTH', 'Penrith Panthers', 0, 0],
    ['SHA', 'Cronulla Sutherland Sharks', 0, 0],
    ['STG', 'St George Illawarra Dragons', 0, 0],
    ['STH', 'South Sydney Rabbitohs', 0, 0],
    ['WST', 'Wests Tigers', 0, 0],
    ['SYD', 'Sydney Roosters', 0, 0]
]

arrTeam = ['BRO','BUL','CBR','GCT','MEL','MNL','NEW','NQC','NZL','PAR','PTH','SHA','STG','STH','WST','SYD']
arrTeamFull = ['Brisbane Broncos','Canterbury Bulldogs','Canberra Raiders','Gold Coast Titans','Melbourne Storm','Manly Warringah Sea Eagles','Newcastle Knights','North Queensland Cowboys','New Zealand Warriors','Parramatta Eels','Penrith Panthers','Cronulla Sutherland Sharks','St George Illawarra Dragons','South Sydney Rabbitohs','Wests Tigers','Sydney Roosters']
arrTotalWorth = []
arrThreeRdAvg = []

def superCoachStats(abbrName):
    # non-totals 
    superCoachStatsURL = 'https://www.nrlsupercoachstats.com/2019stats.php?grid_id=list1&_search=true&nd=1552277748383&rows=25&jqgrid_page=1&sidx=Name&sord=asc&filters=%7B%22groupOp%22%3A%22AND%22%2C%22rules%22%3A%5B%7B%22field%22%3A%22Team%22%2C%22op%22%3A%22eq%22%2C%22data%22%3A%22' + abbrName + '%22%7D%5D%7D'
    #superCoachStatsURL = 'https://www.nrlsupercoachstats.com/2019stats.php?grid_id=list1&_search=true&nd=1552278621899&rows=25&jqgrid_page=1&sidx=Name&sord=asc&filters=%7B%22groupOp%22%3A%22AND%22%2C%22rules%22%3A%5B%7B%22field%22%3A%22Team%22%2C%22op%22%3A%22eq%22%2C%22data%22%3A%22' + abbrName + '%22%7D%2C%7B%22field%22%3A%22Rd%22%2C%22op%22%3A%22eq%22%2C%22data%22%3A%22Totals%22%7D%5D%7D'
    print (abbrName)
    r = requests.get(superCoachStatsURL)
    stats = r.json()
    totalWorth = 0
    threeRdAvg = 0
    for player in stats['rows']:
        totalWorth += int(player['Price'])
        threeRdAvg += int(player['ThreeRdAvg'])
        #print (player['Name2'] + '\t ' + player['Posn1'] + '\t ' + player['Price'] + '\t ' + player['ThreeRdAvg'])
    print('Total team value: ' + str(totalWorth) + '\t Total 3-Rd Avg: ' + str(threeRdAvg))
    arrTotalWorth.append(totalWorth)
    arrThreeRdAvg.append(threeRdAvg)


def getOdds(teamName):
    api_key = 'bad01aed73a13af7ead252b4a4c1d743'
    sport_key = 'rugbyleague_nrl'
    param = { 'api_key': api_key, 'sport': sport_key, 'region': 'au', 'mkt': 'h2h' }
    
    ## use this for live:
    odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params=param)
    odds_json = json.loads(odds_response.text)

    if not odds_json['success']:
        print ('issues getting odds')
    else: 
        for event in odds_json['data']:
            print (str(event['teams']) + ' odds: ' + str(event['sites'][0]['odds']['h2h']))
            #extract teams & odds, search
            arrTeamInfo[1]
            # 


def getLadder():
	ladderURL = 'https://www.nrl.com/ladder/'
	print(ladderURL)
	

def main():
    for team in arrTeamInfo:
        print ('*** ' + team[1] + ' ***')
        superCoachStats(team[0])

    #getOdds(team[1])
    

main()

