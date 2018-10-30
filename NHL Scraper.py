import requests
import csv
from bs4 import BeautifulSoup
import datetime as dt
import pandas as pd
import collections

date = dt.date.today()

url = 'https://statsapi.web.nhl.com/api/v1/schedule?startDate={}&endDate={}'.format('2018-10-07', '2018-10-07') # date will go here once im done testing
data = requests.get(url).json()

download_dir = "todays_games_team_stats.csv"
csv = open(download_dir, "w")

columnTitleRow = "Today's Games, {}, ptPctg, goalsPerGame, goalsAgainstPerGame, stat4, etc.\n\n".format(date)
csv.write(columnTitleRow)


# HERE IS WHERE YOU FILTER THE JSON STUFF
dates = data.get('dates')
# print(dates)

for date in dates:
	games = date.get('games')
	# print(date['date'])
	for game in games:
		teams = game.get('teams')
		home_id = teams['home']['team']['id']
		away_id = teams['away']['team']['id']
		home_team_name = teams['home']['team']['name']
		away_team_name = teams['away']['team']['name']
		home_url = 'https://statsapi.web.nhl.com/api/v1/teams/{}/stats'.format(home_id)
		# print(home_url)
		away_url = 'https://statsapi.web.nhl.com/api/v1/teams/{}/stats'.format(away_id)
		data_home = requests.get(home_url).json()
		data_away = requests.get(away_url).json()
		# print(home_url)
		# print(away_url)
		# print(away_team_name)
		# print(home_team_name + '\n')
		home_singleSeasonStats = data_home['stats'][0]['splits'][0]['stat']
		away_singleSeasonStats = data_away['stats'][0]['splits'][0]['stat']
		# print(away_singleSeasonStats)
		# print(home_singleSeasonStats)

		home_regSeasonRankings = data_home['stats'][1]['splits'][0]['stat']
		away_regSeasonRankings = data_away['stats'][1]['splits'][0]['stat']
		# print(away_regSeasonRankings)
		# print(home_regSeasonRankings)


		# print(home_regSeasonRankings.keys())
		
# SET HOME TEAM STATS
		ptPctg_home = home_singleSeasonStats['ptPctg']
		ptPctg_rank_home = home_regSeasonRankings['ptPctg']

		gpg_home = str(home_singleSeasonStats['goalsPerGame'])
		gpg_rank_home = home_regSeasonRankings['goalsPerGame']

		gag_home = str(home_singleSeasonStats['goalsAgainstPerGame'])
		gag_rank_home = home_regSeasonRankings['goalsAgainstPerGame']
		# print(gag_home, gag_rank_home)



# SET AWAY TEAM STATS
		ptPctg_away = away_singleSeasonStats['ptPctg']
		ptPctg_rank_away = away_regSeasonRankings['ptPctg']

		gpg_away = str(away_singleSeasonStats['goalsPerGame'])
		gpg_rank_away = away_regSeasonRankings['goalsPerGame']

		gag_away = str(away_singleSeasonStats['goalsAgainstPerGame'])
		gag_rank_away = away_regSeasonRankings['goalsAgainstPerGame']
		# print(gag_away, gag_rank_away)

		# ADD ALLLLLL THE STATS



# PRINT EVERYTHING TO THE CSV FILE
		away_row = away_team_name + ',,' + ptPctg_away + '%,' + gpg_away + ',' + gag_away + '\n ,,' + ptPctg_rank_away + ',' + gpg_rank_away + ',' + gag_rank_away + '\n'
		home_row = home_team_name + ',,' + ptPctg_home + '%,' + gpg_home + ',' + gag_home + '\n ,,' + ptPctg_rank_home + ',' + gpg_rank_home + ',' + gag_rank_home + '\n'
		csv.write(away_row + home_row + '\n\n')





















