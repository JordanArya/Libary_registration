#location : project_tiketpesawat
from datetime import datetime
#module sendiri
import system
import view

system.members = system.load_member_data()
system.book = system.load_book_data()
system.mod = system.load_mod_data()
system.absen = system.load_absen()
while not system.error:
	view.main_menu()
	break
	