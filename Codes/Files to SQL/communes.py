import sqlite3
import csv

conn = sqlite3.connect('data.db')
c= conn.cursor()

with open('villes_france.csv', newline='') as csvfile:
    csvfile.readline()
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
    for row in spamreader :
        requete = "INSERT INTO communes VALUES("
        requete+="\""+row[10]+"\",\""+row[1]+"\",\""+row[3]+"\",\""+row[19]+"\",\""+row[20]+"\")"
        c.execute(requete)
        
conn.commit()
conn.close()
