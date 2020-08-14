import matplotlib.pyplot as plt
import csv
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="who"
)

db_cursor = mydb.cursor()

def populateCountries():
    db_cursor.execute("SELECT COUNTRY_NAME FROM data_who")
    who_data = db_cursor.fetchall()

    temp_country = who_data[0]

    f = open("Countries.txt", "a")
    f.write(str(temp_country) + '\n')

    for x in who_data:
        if x != temp_country:
            f.write(str(x) + '\n')
            temp_country = x

date_list = []

def populateDate():
  date_list = []
  for x in range(2, 5):
    if x == 2:
      for z in range(1, 10):
        date = '2020-'
        date = date + '0' + str(x) + '-0' + str(z)
        date_list.append(date)
      for a in range(10, 30):
        date = '2020-'
        date = date + '0' + str(x) + '-' + str(a)
        date_list.append(date)

    if x == 3:
      for z in range(1, 10):
        date = '2020-'
        date = date + '0' + str(x) + '-0' + str(z)
        date_list.append(date)
      for a in range(10, 32):
        date = '2020-'
        date = date + '0' + str(x) + '-' + str(a)
        date_list.append(date)

    if x == 4:
      for z in range(1, 10):
        date = '2020-'
        date = date + '0' + str(x) + '-0' + str(z)
        date_list.append(date)
      for a in range(10, 31):
        date = '2020-'
        date = date + '0' + str(x) + '-' + str(a)
        date_list.append(date)

  return date_list
          
country_list = []

def displayDeathRate():

  db_cursor.execute("SELECT COUNTRY_NAME, TotalDeath FROM data_who")
  who_data = db_cursor.fetchall()

  total_death_list = []
  total_death = 0
  cntry_cnt = 0

  with open("Countries.txt", "r") as f:
    for line in f:
      cntry_cnt += 1
      # if (cntry_cnt == 71) or (cntry_cnt == 142):
      # plt.subplot(align)
      plt.bar(country_list, total_death_list)

      # else:
      string = line.strip()
      clean_string = string
      clean_string = clean_string.replace("',)", "")
      clean_string = clean_string.replace("('", "")
      for x in who_data:
        if x[0] == clean_string:
          total_death = x[1]

      if total_death >= 2000:
        country_list.append(clean_string)
        total_death_list.append(total_death)

    plt.xticks(rotation=90)
    plt.show()

def caseTimeSeries():
  db_cursor.execute("SELECT COUNTRY_NAME, Date_epicrv, TotalCase FROM data_who")
  who_data = db_cursor.fetchall()

  temp_date = populateDate()
  sql_date = ''

  for line in country_list:
    y_data = []
    for d in who_data:
      sql_country = d[0]
      if sql_country == line:
        for x in temp_date:
          sql_date = d[1]
          sql_date = sql_date.replace('T00:00:00.000Z', '')
          if sql_date == x:
            y_data.append(d[2])
    if len(y_data) == 90:
      print(len(temp_date))
      print(len(y_data))
    else:
      temp_list = []
      for i in range(1, 90 - len(y_data)+1):
        temp_list.append(0)
      y_data = temp_list + y_data
  
    plt.plot(temp_date, y_data, label=line)

  plt.legend()
  plt.xticks(rotation=90)
  plt.show()

displayDeathRate()
caseTimeSeries()