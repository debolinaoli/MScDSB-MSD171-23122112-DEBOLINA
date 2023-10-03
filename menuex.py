listnames = []   #empty list to store the names.
# store a name to the list
def storeName(name):
    name = name.strip().title()
    if name in listnames:
        return False
    else:
        listnames.append(name)
        return True
    #list of all names
def printnames():
        print("-"*30)
        for name in listnames:
            print(name)
        print("-"*30)
 # function to search for a name
def searchname(name):
    name = name.strip().title()
    flag = False
    for item in listnames:
        if name == item:
             flag = True
             break
    if flag == True:
         print("name exist in the list")
    else:
         print(" name is not exists")
        
while True:
    print("menu options")
    print("*"*30)
    print("1. enter a name") 
    print("2. search a name")
    print("3. list of names")
    print("4. exit")

    choice = int(input("enter your choice : "))
    if choice == 1:  
         userinp = input("enter a name")
         retval = storeName (userinp)
         if retval == True:
              print("name added successfully")
         else:
            print("name exists in the list")
    elif choice == 2:
         userinp = input("enter the name to be searched")
         searchname(userinp)
    elif choice == 3:
         printnames()
    elif choice == 4:
         exit()
    else:
         print("invalid option, please choose correct one...........")