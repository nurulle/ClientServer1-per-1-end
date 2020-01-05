import json

mahasiswa = []

choco = {"nama": "Choco", "alamat": "Kepunduhan"}
nur = {"nama": "Nur", "alamat": "Tegal"}
zulaikha = {"nama": "Zulaikha", "alamat": "Bulakamba"}

mahasiswa.append(choco)
mahasiswa.append(nur)
mahasiswa.append(zulaikha)

json_str = json.dumps(mahasiswa)
print(json_str)