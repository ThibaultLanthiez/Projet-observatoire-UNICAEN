import sqlite3
import csv

conn = sqlite3.connect('data.db')
c= conn.cursor()

with open('naf.csv', newline='') as csvfile:
    csvfile.readline()
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in spamreader :    
        requete = "INSERT INTO naf VALUES(\""
        requete += row[0].replace(".","")+"\",\""+row[4]+"\")"
        c.execute(requete)
        
conn.commit()
conn.close()

