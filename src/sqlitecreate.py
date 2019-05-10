#!/usr/local/bin/python
# coding: UTF-8
import sqlite3
import json
import os
import glob

conn = sqlite3.connect('dublinbikes.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS dublinbikes
	(
	dublinbike_id INTEGER PRIMARY KEY AUTOINCREMENT,
	status TEXT,
	contract_name TEXT,
	name TEXT PrimaryKey,
	bonus BOOLEAN,
	bike_stands INTEGER,
	number INTEGER,
	last_update INTEGER,
	available_bike_stands INTEGER,
	banking BOOLEAN,
	available_bikes INTEGER,
	address TEXT,
	position_lat REAL,
	position_long REAL)''')

source = 'c:/Bikedata1/'
json_pattern = os.path.join(source,'*.json')
filenames = glob.glob(json_pattern)
for file in filenames:
	with open(file) as data_file:
		data = json.load(data_file)
		print("Done!")

	try:
		data_row = data[0]
		for data_row in data:
			c.execute("INSERT INTO dublinbikes (status, contract_name, name, bonus, bike_stands, number, last_update, available_bike_stands, banking, available_bikes, address, position_lat, position_long) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
				[data_row.get("status"),
				data_row.get("contract_name"),
				data_row.get("name"),
				data_row.get("bonus"),
				data_row.get("bike_stands"),
				data_row.get("number"),
				data_row.get("last_update"),
				data_row.get("available_bike_stands"),
				data_row.get("banking"),
				data_row.get("available_bikes"),
				data_row.get("address"),
				data_row.get("position").get("lat"),
				data_row.get("position").get("lng")])
	except sqlite3.IntegrityError:
		print("Error")

conn.commit()

def total_rows(c, table_name, print_out=False):
	'''Function that returns the total number of rows in the database'''
	c.execute('SELECT COUNT(*) FROM {}'.format(table_name))
	count = c.fetchall()
	if print_out:
		print('\nTotal rows: {}'.format(count[0][0]))
	return count[0][0]
print('total_rows', total_rows(c, 'dublinbikes', print_out=False))

def table_col_info(c, table_name, print_out=False):
	'''Returns a list of tuples with column information'''

	c.execute('PRAGMA TABLE_INFO({})'.format(table_name))
	info = c.fetchall()
	if print_out:
		print('\nColumn info:\ID, Name, Type, NotNull, DefaultVal, PrimaryKey')
		for col in info:
			print(col)
	return info
table_col_info(c, 'dublinbikes', print_out=True)