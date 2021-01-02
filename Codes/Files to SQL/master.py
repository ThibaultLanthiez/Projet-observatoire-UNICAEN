import sqlite3
import csv

conn = sqlite3.connect('data.db')
c= conn.cursor()

with open('dataBrutes_MASTER.csv', newline='') as csvfile:
    csvfile.readline()
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='\"')
    for row in spamreader :
        requete = "INSERT INTO MASTER VALUES("
        requete += "\""+row[0]+"\",\""+row[1]+"\",\""+row[2]+"\",\""+row[3]+"\",\""+row[4]+"\",\""+row[5]+"\",\""+row[6].upper()+"\",\""+row[7].upper()+"\")"
        c.execute(requete)
        
conn.commit()
conn.close()

