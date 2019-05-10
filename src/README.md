#DublinBikes Map Project
#Aoife Whelan, Elayne Ruane, Eóin Scanlon
#========================================

This project contains the files listed below which are used to create a webpage which displays occupancy information for the DublinBikes scheme in Dublin city.

###bikescraper.py

Python file to query JC Decaux API and extract a JSON file every 5 minutes. Ideally this should be run on a web server to avoid downtime.

###sqlitecreate.py

Python programme to create an SQLite database. Requires the Python package sqlite3.

###sqlitetest.py

Python programme to print the contents of the dublinbikes.sqlite database as verification.

###Occupancy_Data.ipynb

Jupyter Notebook with code to perform data analysis on DublinBikes occupancy data. Produces bar graphs of weekly occupancy data.

###line_charts.ipynb

Jupyter Notebook to produce line graphs of occupancy data across each day of the week.

##app.py

Flask app to query database, will then be used in the webpage. The app makes an SQL query to the database created using sqlitecreate.py.

###static folder

Contains CSS folder and images.

###templates folder 

Contains .html file for webpage.

###Dublin.json

Example of one result from an API request.

###dublinbikes.sqlite

Database created by sqlitecreate.py.

###testfile.txt

Example output from bikescraper.py after a number of API requests.