from bs4 import BeautifulSoup
import json
import requests
from requests_html import HTMLSession

session = HTMLSession()
#r = session.get(superCoachStatsURL)
#r.html.render()

#arrTeam = ['BRO','BUL','CBR','GCT','MEL','MNL','NEW','NQC','NZL','PAR','PTH','SHA','STG','STH','WST','SYD']
arrTeam = ['BRO']

def superCoachStats(teamName):
    # non-totals 
    superCoachStatsURL = 'https://www.nrlsupercoachstats.com/2019stats.php?grid_id=list1&_search=true&nd=1552277748383&rows=25&jqgrid_page=1&sidx=Name&sord=asc&filters=%7B%22groupOp%22%3A%22AND%22%2C%22rules%22%3A%5B%7B%22field%22%3A%22Team%22%2C%22op%22%3A%22eq%22%2C%22data%22%3A%22' + teamName + '%22%7D%5D%7D'
    #superCoachStatsURL = 'https://www.nrlsupercoachstats.com/2019stats.php?grid_id=list1&_search=true&nd=1552278621899&rows=25&jqgrid_page=1&sidx=Name&sord=asc&filters=%7B%22groupOp%22%3A%22AND%22%2C%22rules%22%3A%5B%7B%22field%22%3A%22Team%22%2C%22op%22%3A%22eq%22%2C%22data%22%3A%22' + teamName + '%22%7D%2C%7B%22field%22%3A%22Rd%22%2C%22op%22%3A%22eq%22%2C%22data%22%3A%22Totals%22%7D%5D%7D'
    r = requests.get(superCoachStatsURL)
    stats = r.json()
    #f = open(teamName + '.txt','w')
    #f.write (str(stats))
    #f.close
    #print (stats)
    totalWorth = 0
    threeRdAvg = 0
    for player in stats['rows']:
        totalWorth += int(player['Price'])
        threeRdAvg += int(player['ThreeRdAvg'])
        print (player['Name2'] + '\t ' + player['Posn1'] + '\t ' + player['Price'] + '\t ' + player['ThreeRdAvg'])
    print('Total team value: ' + str(totalWorth) + '\t Total 3-Rd Avg: ' + str(threeRdAvg))


def getOdds(teamName):
	oddsURL = 'https://www.odds.com.au/sport/rugby-league/nrl/matches/'
	r = session.get(oddsURL)
	r.html.render()
	r.html.search('Melbourne Storm')
	#print (r.html.html)



def getLadder():
	ladderURL = 'https://www.nrl.com/ladder/'
	print(ladderURL)

def main():
	for team in arrTeam:
		print ('*** ' + team + ' ***')
    	#superCoachStats(team)
		getOdds(team)


main()

