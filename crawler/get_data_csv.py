import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

# Chép đường dẫn vào biến url
url = 'https://www.worldometers.info/coronavirus/'

# Tạo object page
page = requests.get(url)

# Thu thập thông tin từ trang web
soup = BeautifulSoup(page.text, 'lxml')

# Lưu thông tin từ tag <table> vào biến table1
table1 = soup.find('table', id='main_table_countries_today')

# Lưu các tên cột có tag <th> vào mảng headers
headers = []
for i in table1.find_all('th'):
    title = i.text
    headers.append(title)

# Vì dòng 13 có chứa kí tự /n nên ta gán lại để loại nó đi
headers[13] = 'Tests/1M pop'

#Vì dòng 10 có chứa kí tự /xa0 nên ta gán lại để loại nó đi
headers[10] = 'Tot Cases/1M pop'

# Khởi tạo dataframe
mydata = pd.DataFrame(columns = headers)
mydata = mydata.rename(columns={'Country,Other':'Country'})

# Chạy vòng lặp để nhập thông tin theo từng dòng vào dataframe
for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row

# Loại bỏ các dòng không cần thiết
mydata.drop(mydata.index[0:8], inplace=True)
mydata.drop(mydata.index[-8:], inplace=True)
mydata.reset_index(inplace=True, drop=True)

# Loại bỏ cột '#'
mydata.drop('#', inplace=True, axis=1)

currentDay = datetime.datetime.now().day
currentMonth = datetime.datetime.now().month

# Xuất dữ liệu thành file .csv
mydata.to_csv('covid_data_'+str(currentMonth)+'_'+str(currentDay)+'.csv', index=False)
