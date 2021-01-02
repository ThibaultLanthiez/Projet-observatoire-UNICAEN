import csv
f = open('Leaflet_master.html', 'r+')
f.write('''<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.4.0/dist/leaflet.css"/>
        <script type="text/javascript" src="https://unpkg.com/leaflet@1.4.0/dist/leaflet.js"></script>
        <script type="text/javascript" src="leaflet-color-markers"></script>
    </head>
 
    <body onload="initialize()">
    <div id="map" style="width:100%; height:100%"></div>

        
<script>
    function initialize() {
        var map = L.map('map').setView([48.833, 2.333], 6);
 
        var osmLayer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
            attribution: '© <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            maxZoom: 19
        });
        map.addLayer(osmLayer);
''')
with open('jointure_MASTER.csv', newline = '') as csvfile:
    csvfile.readline()
    spamreader = csv.reader(csvfile, delimiter='|', quotechar='"')
    for row in spamreader:
        if row[12] == "1":
            f.write('L.marker(['+row[10]+','+row[9]+']).addTo(map).bindPopup('"\"<b>"+row[3]+'</b>,<br>'+row[12]+' étudiant'+"\""');' "\n")
        else : 
            f.write('L.marker(['+row[10]+','+row[9]+']).addTo(map).bindPopup('"\"<b>"+row[3]+'</b>,<br>'+row[12]+' étudiants'+"\""');' "\n")

f.write('''
    } 
</script>    
</body>
</html>
''')
f.close()
