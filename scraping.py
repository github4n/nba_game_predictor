import requests
import numpy as np 
import pandas as pd 
import json
import nba_py

# scrape game id's for all NBA season games /
# from 1989-1990 season to 2017-2018 season
# url for getting your user agent: https://stackoverflow.com/questions/46781563/how-to-obtain-a-json-response-from-the-stats-nba-com-api

# query to get game id from each row
def getIds(row):
	return row['resultSets'][1]['rowSet'][0][2]

# range of dates
dates = pd.date_range(start='11/03/1989', end='11/12/1989', freq='D').strftime('%m/%d/%y')

json_data = []
for date in dates:
	try:
		headers = {'User-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36'}
		# headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
		request = requests.get("https://stats.nba.com/stats/scoreboard/", 
					params={'GameDate':date, 'LeagueID':'00', 'DayOffset':'0'}, 
					headers=headers)

		# check status code for OK response
		print("Getting " + date)
		print(request.status_code)

		# build list of jsons for each date
		json_data.append(request.json())

	except requests.exceptions.ReadTimeout:
		print("=(")

# create numpy array out of json list
json_array = np.array(json_data)

# apply custom function on each row
id_vect = np.vectorize(getIds)
game_ids = id_vect(json_array)
print(game_ids)

# save ids in csv
np.savetxt('game_ids.csv', game_ids, fmt='%s', delimiter=',')




