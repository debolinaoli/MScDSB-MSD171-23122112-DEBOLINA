# CREATE A MENU DRIVEN PROGRAM THAT COLLECTS STUDENTS DETAIILS [NAME, EMAIL,PHONE] {USE DICTIONARY TO STORE STUDENT DETAILS}
# MENU OPTIONS <1. CREATE STUDENTS 2. SEARCH FOR STUDENTS 3. PRINT STUEDNTS >


studentDict = {}    #empty list to store the names.
# store a name to the list
def createStudent(name, regno, email, phone) :
    Student = {
        "Name" : name,
        "Email" : email,
        "Phone no" : phone,   

    }