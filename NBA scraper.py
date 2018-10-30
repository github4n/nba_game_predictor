import numpy as np
import json
import nba_py
import pandas as pd
import requests

dates = pd.date_range(start='10/17/2017', end='6/17/2018', freq='D')
for i in range(2):
	# date is a TimeStamp object in the form of MM-DD-YYYY HH:MM:SS
	# and has a function date() which gets rid of the HH:MM:SS info
	# formatted_date = str(date.date()).replace('-','/')
	# print(formatted_date)

	url = 'https://stats.nba.com/stats/scoreboard/?GameDate={}&LeagueID=00&DayOffset=0'.format(formatted_date)

	with open("sampleJSON.json", 'r') as data:

		data = json.load(data)
		# Grabs a list of lists of nba game information
		# Each sublist representing one game
		result_row_sets = np.array(data['resultSets'][1].get('rowSet'))

		# Grabs the game id's from result_row_sets
		game_ids = result_row_sets[:,2].astype(np.int64)

		print(game_ids)


