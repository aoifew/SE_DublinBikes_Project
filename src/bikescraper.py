#Software Engineering Project
#Aoife, Elayne & Eoin
#Scrape JSON files from JCDecaux website

# Import necessary packages
import requests
import time
from time import sleep, strftime, gmtime
import json


#JCDecaux URL with API Key
JC_URL = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=734d41507f01569b257148e24bfbfcbd67de0876"

sampletime = 300 #5 minutes between samples

def getStationInfo():
    '''Function to query API'''
    
    station_info = requests.get(JC_URL) #issue get requests
    return station_info.json()          #JSON output

if __name__ == "__main__":
    while True: #Keep running!
        file_name = "datafile_{}.json".format(strftime("%Y%m%d%H%M%S", gmtime()), 'a')
        with open(file_name, 'w') as outfile:
            json.dump(getStationInfo(), outfile)     
        print("\n\nScraping at " + strftime("%Y%m%d%H%M%S", gmtime()))
        print("Suspending for five minutes")
        sleep(sampletime) #Suspend the loop for 5 minutes
