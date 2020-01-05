im
port json

data = '[{ "nama" : "Choco", "alamat" : "Kepunduhan" },'\
       '{ "nama" : "Iqbaal", "alamat" : "Tegal" }]'

result = json.loads(data)

for x in result:
    print(x['nama'])