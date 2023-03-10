import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import os

for filename in os.listdir():
    if not(filename.endswith(".csv")):
        continue
    else:
        print(filename)
        month = filename[11]
        date = filename[13:15]
        newdate = month + "/" + date + "/" + "2022"
        df = pd.read_csv(filename)
        df["Date"] = newdate
        df.to_csv(filename, index=False)
        continue

#filename = "covid_data_5_10.csv"


