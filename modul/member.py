import getpass
import time
def del_id(member,user_name):
	input_user = input("username : ")
	password_input = getpass.getpass("password : ")
	if input_user in user_name and password_input in member[input_user]["password"]:
		return input_user
	else :
		print("your pass is wrong")
		time.sleep(2)		


def book_search_with_title(book):
	books = []
	n = 1
	book_search = input('what title of book do you want to search : ')
	for every_book in book:
		books.append(every_book)
	if book_search in books:
		print(f"[{n}] Judul : {book_search}")
		print(f"    genre : {book[book_search]['genre']}")
		input("press Enter to coninue : ")
	else:
		print("the book aren't add")
		input("press Enter to continue : ")
def search_with_filter(book):
	n = 1
	filters = input('what title of book do you want to search : ')
	for every_book in book:
		if book[every_book]['genre'] ==  filters:
			print(f"[{n}] Judul : {every_book}")
			print(f"    genre : {filters}")
			n += 1
	if book[every_book]['genre'] !=  filters:
		print("the book aren't add")
	input("press enter to continue : ")

def return_book(member):
	book_borrowed = []
	book_title = input("what book title do you want return : ")
	for every_book in member:
		for every_title in member[every_book]['borrow_status']:
			book_borrowed.append(every_title)
	if book_title in book_borrowed:
		return book_title
