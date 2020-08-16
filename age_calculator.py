from datetime import datetime

def check_birthdate(year, month, day):
	today = datetime.today()
	birthday = datetime(year, month, day)
	diff = today - birthday
	if (diff.days <= 0):
		return False
	else:
		return True

def calculate_age(year, month, day):
	today = datetime.today()
	birthday = datetime(year, month, day)
	age = today - birthday
	print ("You are %s years old." %(int(age.days/365)))


def main():
	year = input("Enter year of birth: ")
	month = input("Enter month of birth: ")
	day = input("Enter day of birth: ")

	if check_birthdate(int(year), int(month), int(day)) == True :
		calculate_age(int(year), int(month), int(day))
	else:
		print("birthdate entered is invalid")


if __name__ == '__main__':
	main()
