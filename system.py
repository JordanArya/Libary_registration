from json import load,dump
def load_ticket_data():
	with open(ticket_table_path, "r") as ticketFile:
		data = load(ticketFile)
	return data
def load_user_data():
	with open (user_table_path,"r") as userFile:
		data = load(userFile)
	return data


error = False
ticket_table_path = "data/data_penumpang.json"
user_table_path = "data/data_user.json"

tickets = {}
users = {}

def pesan_tiket():
	
#LIBARY STRING

main_menu = """
Aplikasi tiket pesawat agensi luar biasa

[1] pesan/booking pesawat
[2] cari pesawat
[3] edit tiket pesawat
[4] Batalkan/ Hapus Tiket Pesawat
[5] Cetak PDF tiket 
[6] Cetak QR tiket pesawat
[7] Tentang Aplikasi
"""

