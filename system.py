from json import load,dump
from datetime import datetime 
from Modul import member, user
import time
import getpass
import os
import random
import view

def del_books_data(datas):
	with open(book_table_path,"w") as WriteDatas:
		dump(datas,WriteDatas)
def load_mod_data():
	with open(mod_table_path, "r") as modFile:
		data = load(modFile)
	return data
def load_member_data():
	with open(member_table_path, "r") as ticketFile:
		data = load(ticketFile)
	return data
def load_book_data():
	with open (book_table_path,"r") as userFile:
		data = load(userFile)
	return data
def write_member_data(data):
	datas = load_member_data()
	datas.update(data)
	with open(member_table_path,"w") as WriteData:
		dump(datas,WriteData)
def write_book_data(book):
	books = load_book_data()
	books.update(book)
	with open(book_table_path,"w") as WriteDatas:
		dump(books,WriteDatas)
def write_member_datas(data):
	with open(member_table_path,"w") as WriteData:
		dump(data,WriteData)
def load_absen():
	with open(absen_table_path,"r") as absenData:
		data = load(absenData)
	return data
def write_Absen(data):
	absens = load_absen()
	absens.update(data)
	with open(absen_table_path,"w") as WriteDatas:
		dump(absens,WriteDatas)
#module 
error = False
member_delet_path = "data/deleted_account.json"
member_table_path = "data/data_peserta.json"
book_table_path = "data/data_buku.json"
mod_table_path ="data/mod.json"
absen_table_path = "data/absen.json"
mod = None
members = None
book= None
absen =None
#modul lain-lainnya
def absenn(user_name):
	global tahun,hari,bulan
	code =f"{tahun}-{bulan}-{hari}"
	try:
		n = len(absen[code])
	except KeyError:
		n = 0
	n = str(n+1)
	
	data =  {code:{n:user_name}}
	write_Absen(data)
def sure():
	sure = input("press Y if you sure : ")
	sure = sure.title()
	if sure == "Y":
		return True
	else:
		return False 
def heading(msg):
	print(msg)
def date_generator():
	time = datetime.now()
	tahun = time.year
	bulan = time.month
	hari = time.day
	menit = time.minute
	detik = time.second
	return tahun,bulan,hari,menit,detik
def check():
	Eroor = False
	user_option = input("your option : ")
	if user_option == "1":
		os.system('cls')
		heading('menu SignIn')
		view.member_main_menu()
	elif user_option == "2":
		os.system('cls')
		heading('Menu SignUp')
		sign_up()
	elif user_option == "3":
		check_moderator()
	
	
		
def check_member():
	user_name = sign_in()	
	Eroor = False
	while not Eroor :
		os.system("cls")
		print(main_menu_member)
		user_option = input('your option : ')
		if user_option == '1':
			borrow_book(user_name)
		elif user_option == '2':
			member.book_search_with_title(book)
		elif user_option == '3':
			member.search_with_filter(book)
		elif user_option == '4':
			donate(user_name)	
		elif user_option == '5':
			return_book(user_name)
		elif user_option == '6':
			del_acount()
		elif user_option == '7':
			break
def check_moderator():
	user_name = sign_in_mod()	
	Eroor = False
	while not Eroor :
		os.system("cls")
		print(Moderator_menu)
		user_option = input('your option : ')
		if user_option == '1':
			del_acount_mod()
		elif user_option == '2':
			user.view_member(View_mod_menu,members)
		elif user_option == '3':
			user.view_absen(absen)
		elif user_option == '4':
			Add_book()

# module member
def code_generator(users):
	tahun,bulan,hari,menit,detik = date_generator()
	id_member = str("%4d%02d-%s%02d" % (tahun,bulan,users[0],hari))
	return id_member
def vertivication():
	code = ['A','B','C','D','F','G','a','b','d','e']
	codes = random.choice(code) + str(random.randint(0,20))
	while len(codes) < 6:
		codes = codes + random.choice(code) + str(random.randint(0,20))
		
	else:
		print(codes)
	input_peserta = input("Write your vertivication code : ")
	return codes,input_peserta
def date_vertivication():
	tahun,bulan,hari,menit,detik = date_generator()
	tahun = int(tahun)
	i = True
	while i:
		try:
			day,month,year = input("input your date birth (example : 23/11/2010) : ").split("/")
			day,month,year = int(day),int(month),int(year)
			i = False

		except ValueError:
			print("tolong masukan angka yang benar")
	while day > 31  or month > 12  or year > tahun or year < 1890:
		if day > 31 :
			day = int(input("your day input is wrong please input again : "))
		if month > 12 :
			month = int(input("your month input is wrong please input again : "))
		if year > tahun or year < 1980:
			year = int(input("your year input is wrong : "))
	
	if day < 31 or month < 12 or year < tahun and tahun > 1890:
		member_age = tahun-year
		return day,month,year,member_age
def sign_up():
	member_title = input("your title name : ")
	member_front_name = input("your front name : ")
	member_last_name = input("your last name : ")
	member_adress = input("your adress : ")
	member_email= input("your email : ")
	number_telephone = input("your telephone number : ")
	user_name = input("what UserName do you want to make : ")
	password = getpass.getpass("what is the password : ")
	verify_pass = getpass.getpass("input your password again : ")
	while verify_pass != password:
		verify_pass = getpass.getpass("your verify pass is wrong : ")
	else:
		code = code_generator(member_front_name)
		day,month,year,age = date_vertivication()
		vertivication_code,input_vertivication = vertivication() 
		data = {user_name : {
				"codes" : code,
				"member_name" : {
					"title" : member_title ,
					"Front_name" : member_front_name,
					"last_name" : member_last_name
					},
			"member_information" : {
				"Adress" : member_adress,
				"telephone_number" : number_telephone,
				"Email" : member_email
			},
				"date_of_birth" : {
					"date": day,
					"month" : month,
					"year" : year,
					"age" : age
			},
			"borrow_status" : {
				
			},
			"borrow_history"  : {
			},
			'password' : password

		}}
		
		while input_vertivication != vertivication_code:
			vertivication_code,input_vertivication = vertivication()
		if input_vertivication == vertivication_code:
			write_member_data(data)
			print("your data already been update")
			time.sleep(2)
def borrow_book(users_name):
	global tahun,bulan,hari
	Eroor = False
	n= len(members[users_name]["borrow_history"])
	n =int(n) +1
	l =len(members[users_name]['borrow_status'])
	l =int(l)+1
	books= []
	print_book()
	book_choice = input('your book title choice : ')
	for every_book in book:
		books.append(every_book)
	if book_choice in books:
		sure = input("press Y if you sure you want to borrow it : ")
		sure = sure.title()             
		if sure == 'Y':
			members[users_name]["borrow_history"][n] = {"title" :book_choice}
			members[users_name]['borrow_status'][book_choice] =  {'Borrowed at' : f"{tahun}/{bulan}/{hari}", "deadline" : f"{tahun}/{bulan}/{hari+3}"}
			del book[book_choice]["status"]
			book[book_choice]["status"]= "Borrowed"
			write_member_data(members)	
			del_books_data(book)
		else:
			print('borrow canceled')
			time.sleep(2)
	elif book_choice not in books:
		print('maaf buku belum teserdia')
	input('tekan enter bila ingin lanjut')
def sign_in():
	a = False
	user_name = []
	username_input = input("your user name : ")
	password_input = getpass.getpass("your password : ")
	for every_member in members:
		user_name.append(every_member)
	while not a: 
		if username_input not in user_name or password_input not in members[username_input]["password"]:
			print('your username is not at the system')
			username_input = input("your user name : ")
			password_input = getpass.getpass('your password : ')
			if username_input in user_name and password_input in members[username_input]["password"]:
				absenn(username_input)
				return username_input
			elif username_input not in user_name or password_input not in members[username_input]["password"]:
				choice = input("if you dont have an account you can go to sign up mode with press 1 : ")
				if choice == '1':
					os.system('cls')
					sign_up()
					a = True
		elif username_input in user_name and password_input in members[username_input]["password"]:
			print(username_input)
			absenn(username_input)
			return username_input
def print_book():
	n = 1
	l = 0
	for every_book in book:
		if book[every_book]["status"] == "Not Borrowed":
			print(f"[{n}] Judul : {every_book}")
			print(f"    genre : {book[every_book]['genre']}")
			n+=1
def donate(user_name):
	books = input('what title of book do you want to input : ')
	print(genre_choice)
	genre = input("what genre of book it's ")
	sures  = sure()
	if sures == True:
		n = len(book)
		n =int(n) +1
		book[books] = {"genre" : genre, "status" : "Not Borrowed"}
		members[user_name]["donate book"] = {"title" : books}
		write_book_data(book)
		write_member_data(members)
		input('thank you for supporting us')
def del_acount():
	heading("Del account")
	user_name = []
	for every_member in members:
		user_name.append(every_member)
	user_names = member.del_id(members,user_name)
	print(user_names)
	if user_names != None:
		sures = sure()
		vertivication_code,input_peserta =vertivication()
		if sures == True and input_peserta == vertivication_code:
			del members[user_names]
			print(members)
			write_member_datas(members)
			input("data telah dihapus")
 # mod module
def return_book(user_name):
	book_title = member.return_book(members)
	if book_title != None:
		del members[user_name]["borrow_status"][book_title]
		del book[book_title]["status"]
		book[book_title]["status"]= "Not Borrowed"
		write_member_datas(members)
		del_books_data(book)
		input('buku sudah dikembalikan')

# modul mod
def sign_in_mod():
	a = False
	mod_name = []
	username_input = input("your user name : ")
	password_input = getpass.getpass("your password : ")
	for every_member in mod:
		mod_name.append(every_member)
	while not a: 
		if username_input not in mod_name or password_input not in mod[username_input]["password"]:
			print('your username is not at the system')
			username_input = input("your user name : ")
			password_input = getpass.getpass('your password : ')
			if username_input in mod_name and password_input in mod[username_input]["password"]:
				return username_input
		elif username_input in mod_name and password_input in mod[username_input]["password"]:
			return username_input
def del_acount_mod():
	heading("Del account")
	user_name = []
	for every_member in members:
		user_name.append(every_member)
	user_names = user.del_id(user_name)
	if user_names != None:
		sures = sure()
		if sures == True :
			del members[user_names]
			print(members)
			write_member_datas(members)
			input("data telah dihapus")
def Add_book():
	books,genre = user.Add_book(genre_choice)
	sures = sure()
	if sures == True:
		n = len(book)
		n =int(n) +1
		book[books] = {"genre" : genre, "status" : "Not Borrowed"}
		write_book_data(book)
		input('book already added')



#LIBARY STRING
tahun,bulan,hari,menit,detik = date_generator()
main_menu =f""" Masuk ke Perpusatakaan                            { str("%4d/%02d/%02d" % (tahun,bulan,hari))}				

[1] Sign In
[2] Sign Up
[3] Developer Sign In
"""

main_menu_member = f""" Member                            { str("%4d/%02d/%02d" % (tahun,bulan,hari))}				

[1] Borrow book
[2] Search book with title
[3] search book with genre
[4] Donate book
[5] Return book
[6] Delete account
[7] Quit
"""
genre_choice = """
[1] Horror
[2] Drama
[3] Edukatif
[4] fantasy
[5] Misteri
"""

Moderator_menu = f"""Developer mode                           { str("%4d/%02d/%02d" % (tahun,bulan,hari))}
[1] Delete member
[2] View member
[3] View absen
[4] Add book
"""
View_mod_menu = """
[1] UserName
[2] All status
[3] Search UserName
"""