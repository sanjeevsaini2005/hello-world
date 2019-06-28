list_of_students = [ "Dakshil", "Sanjeev", "Sailu", "Kiran" ]

name = input("Please enter the name of student: ")

if name in list_of_students:
	print("The student " + name + " is enrolled")
else:
	print("Sorry the student " + name + " is not enrolled")

