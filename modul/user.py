import time
def Add_book(genre_choice):
	books = input('what title of book do you want to input : ')
	print(genre_choice)
	genre = input("what genre of book it's ")
	return books,genre

def view_member(msg,member):
	print(msg)
	opsi = input("what menu do you want to choice : ")
	if opsi == '1':
		for every_name in member:
			print(every_name)
			input()
	elif opsi == '2':
		print(member)
		input()
	elif opsi == '3':
		name= []
		search_user_name = input("what username do you want to search : ") 
		for every_name in member:
			name.append(every_name)
		if search_user_name in name:
			user_id = member[search_user_name]["codes"]
			title = member[search_user_name]["member_name"]["title"]
			Front_name = member[search_user_name]["member_name"]["Front_name"]
			last_name = member[search_user_name]["member_name"]["last_name"]
			Adress = member[search_user_name]["member_information"]["Adress"]
			Email =  member[search_user_name]["member_information"]["Email"]
			telephone_number =  member[search_user_name]["member_information"]["telephone_number"]
			date = member[search_user_name]["date_of_birth"]["date"]
			month = member[search_user_name]["date_of_birth"]["month"]
			year = member[search_user_name]["date_of_birth"]["year"]
			age = member[search_user_name]["date_of_birth"]["age"]
			borrow_status = member[search_user_name]['borrow_status']
			borrow_history = member[search_user_name]['borrow_history']
			donate_book = member[search_user_name]["donate_book"]
			print(f"""search_user_name : 
				user_id : {user_id} 
				title": {title} 
				Front_name : {Front_name} 
				last_name : {last_name} 
				Adress : {Adress} 
				telephone_number : {telephone_number} 
				Email : {Email} 
				date_of_birth : ("date": {date} "month": {month} "year": {year} "age": {age}
				borrow_status : {borrow_status}
				borrow_history : 
					{borrow_history} 
				"donate_book": {donate_book}
				""")
			input("press enter to continue")
		else:
			input("sorry we can't find that member name")
def del_id(user_name):
	input_user = input("username : ")
	if input_user in user_name:
		return input_user
	else :
		print("we can't find it")
		time.sleep(2)	

def view_absen(absen):
	print(absen)
	input()


