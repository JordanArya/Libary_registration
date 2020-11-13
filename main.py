#location : project_tiketpesawat
from datetime import datetime
#module sendiri
from modul import ticket, user
import system
import view
import save_choice

system.tickets = system.load_ticket_data()
system.users = system.load_user_data()

while not system.error:
	view.main_menu()
	