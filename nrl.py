from bs4 import BeautifulSoup
import json
import requests
#from requests_html import HTMLSession
from pprint import pprint
import time

future_time = time.time() + 604800

h = open('output.html','w')

#if using requests_html:
#session = HTMLSession()
#r = session.get(superCoachStatsURL)
#r.html.render()

#arrTeamInfo format
    # 0 Team Abbreviation     abbrName
    # 1 Full Name             teamName
    # 2 Total Price           totalPrice
    # 3 3 Round Avg           threeRdAvg
    # 4 Odds Average          oddsAvg
    # 5 Ladder Position       ldrPos
    # 6 Points For/Against    ptsDiff
    #

arrTeamInfo = [
    ['BRO', 'Brisbane Broncos', 0, 0, 0, 1, 12],
    ['BUL', 'Canterbury Bulldogs', 0, 0, 0, 0, 0],
    ['CBR', 'Canberra Raiders', 0, 0, 0, 0, 0],
    ['GCT', 'Gold Coast Titans', 0, 0, 0, 0, 0],
    ['MEL', 'Melbourne Storm', 0, 0, 0, 0, 0],
    ['MNL', 'Manly Warringah Sea Eagles', 0, 0, 0, 0, 0],
    ['NEW', 'Newcastle Knights', 0, 0, 0, 0, 0],
    ['NQC', 'North Queensland Cowboys', 0, 0, 0, 0, 0],
    ['NZL', 'New Zealand Warriors', 0, 0, 0, 0, 0],
    ['PAR', 'Parramatta Eels', 0, 0, 0, 0, 0],
    ['PTH', 'Penrith Panthers', 0, 0, 0, 0, 0],
    ['SHA', 'Cronulla Sutherland Sharks', 0, 0, 0, 0, 0],
    ['STG', 'St George Illawarra Dragons', 0, 0, 0, 0, 0],
    ['STH', 'South Sydney Rabbitohs', 0, 0, 0, 0, 0],
    ['WST', 'Wests Tigers', 0, 0, 0, 0, 0],
    ['SYD', 'Sydney Roosters', 0, 0, 0, 0, 0]
]

arrTeam = ['BRO','BUL','CBR','GCT','MEL','MNL','NEW','NQC','NZL','PAR','PTH','SHA','STG','STH','WST','SYD']
arrTeamFull = ['Brisbane Broncos','Canterbury Bulldogs','Canberra Raiders','Gold Coast Titans','Melbourne Storm','Manly Warringah Sea Eagles','Newcastle Knights','North Queensland Cowboys','New Zealand Warriors','Parramatta Eels','Penrith Panthers','Cronulla Sutherland Sharks','St George Illawarra Dragons','South Sydney Rabbitohs','Wests Tigers','Sydney Roosters']
arrTotalWorth = []
arrThreeRdAvg = []

weeklyGames = []

def superCoachStats(abbrName):
    # non-totals 
    superCoachStatsURL = 'https://www.nrlsupercoachstats.com/2019stats.php?grid_id=list1&_search=true&nd=1552277748383&rows=25&jqgrid_page=1&sidx=Name&sord=asc&filters=%7B%22groupOp%22%3A%22AND%22%2C%22rules%22%3A%5B%7B%22field%22%3A%22Team%22%2C%22op%22%3A%22eq%22%2C%22data%22%3A%22' + abbrName + '%22%7D%5D%7D'
    #superCoachStatsURL = 'https://www.nrlsupercoachstats.com/2019stats.php?grid_id=list1&_search=true&nd=1552278621899&rows=25&jqgrid_page=1&sidx=Name&sord=asc&filters=%7B%22groupOp%22%3A%22AND%22%2C%22rules%22%3A%5B%7B%22field%22%3A%22Team%22%2C%22op%22%3A%22eq%22%2C%22data%22%3A%22' + abbrName + '%22%7D%2C%7B%22field%22%3A%22Rd%22%2C%22op%22%3A%22eq%22%2C%22data%22%3A%22Totals%22%7D%5D%7D'
    #print (abbrName)
    r = requests.get(superCoachStatsURL)
    stats = r.json()
    totalWorth = 0
    players = 0
    threeRdAvg = 0
    for player in stats['rows']:
        players += 1
        totalWorth += int(player['Price'])
        threeRdAvg += int(player['ThreeRdAvg'])
        #print (player['Name2'] + '\t ' + player['Posn1'] + '\t ' + player['Price'] + '\t ' + player['ThreeRdAvg'])
    #print('Total team value: ' + str(totalWorth) + '\t Total 3-Rd Avg: ' + str(threeRdAvg))
    arrTotalWorth.append(totalWorth)
    arrThreeRdAvg.append(threeRdAvg)
    return ((totalWorth/players), threeRdAvg)

def getLadder():
    ladderURL = 'https://'
    r = requests.get(ladderURL)
    soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup.find_all('td'))
    #print(ladderURL)

def getOdds(teamName):
    api_key = 'bad01aed73a13af7ead252b4a4c1d743'
    sport_key = 'rugbyleague_nrl'
    param = { 'api_key': api_key, 'sport': sport_key, 'region': 'au', 'mkt': 'h2h' }

    odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params=param)
    odds_json = json.loads(odds_response.text)

    if not odds_json['success']:
        print ('issues getting odds')
    else: 
        for event in odds_json['data']:
            oddA = 0
            oddB = 0
            #print (str(event['teams']) + ' odds: ' + str(event['sites'][0]['odds']['h2h']))
            #extract teams & odds, search
            #arrTeamInfo[1]
            teamA = str(event['teams'][0])
            teamB = str(event['teams'][1])
            numSites = (len(event['sites']))
            #print (numSites)
            for oddSites in (event['sites']):
                oddA += oddSites['odds']['h2h'][0]
                oddB += oddSites['odds']['h2h'][1]
            oddA = round(oddA / numSites, 2)
            oddB = round(oddB / numSites, 2)
            # match teamA/B with array and append to element 4
            for match in arrTeamInfo:
                #print (match[1])
                if match[1] == teamA:
                    match[4] = oddA
                    avPlayer1 = match[2]
                    #print (teamA + ' odds: ' + str(oddA))
                elif match[1] == teamB:
                    match[4] = oddB
                    avPlayer2 = match[2]
                    #print (teamB + ' odds: ' + str(oddB))
                else:
                    pass
            print ('-----')
            print ('A: ' + teamA + '\t\t' + str(oddA) + '\t' + str(avPlayer1))
            print ('B: ' + teamB + '\t\t' + str(oddB) + '\t' + str(avPlayer2))
            print ('kickoff: ' + str(event['commence_time']) + ' formatted: ' + time.ctime(event['commence_time']))
            
            kickoff_time = event['commence_time']
            if (future_time > int(kickoff_time)):
                h.write('<tr><td>' + teamA + '</td><td>' + str(oddA) + '</td><td>' + str(avPlayer1) + '</td><td></td><td></td></tr>')
                h.write('<tr><td>' + teamB + '</td><td>' + str(oddB) + '</td><td>' + str(avPlayer2) + '</td><td></td><td></td></tr>')



def main():
    for team in arrTeamInfo:
        #print ('*** ' + team[1] + ' ***')
        totalWorth,threeRdAvg = superCoachStats(team[0])
        ## Problem is here
        #arrTeamInfo[team].append(totalWorth)
        #arrTeamInfo[team].append(threeRdAvg)
        team[2] = int(totalWorth)
        team[3] = threeRdAvg
        #team[4] = avgOdd
    #getLadder()
    h.write ('<html><style> tr:nth-child(2n+1) {background: #CCC} </style><table>')
    h.write ('<tr><th>Team</th><th>Odds</th><th>APV</th><th>Pos</th><th>F/A</th><th></th>')
    print ('Team \t\tOdds \tAPV \tLdr \tF/A')
    getOdds(team[1])   
    #pprint (arrTeamInfo)
    #pprint(weeklyGames)
    #doCalcs()
    h.write ('</table></html>')
    h.close()

main()

