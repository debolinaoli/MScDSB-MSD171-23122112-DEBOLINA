# OOP
class MSCDSB:

    def __init__(self):  #membar fuction
        #   DATA MEMBERS/ PRPPERTIES/ATTRIBUTES..........
        self.name = "MSCDSB"
        self.students = ["A","B","C"]
    
    def printstudents(self): #member fuctions
        for student in self.students:
            print(student)


obj = MSCDSB()
print(obj.name)           # or => print(obj.name,obj.students)
print(obj.students)        #  => obj.printstudents.             then output will come in objectwise like rowwise a,b,c
class car:

    def __init__(self,mfg,mdl,yer):
        self.manufacturer = mfg
        self.model = mdl
        self.year = yer

    def __str__(self):
        return self.manufacturer

BMW = car("bmw","F series",2023)
print(BMW.manufacturer)
print(BMW.model)
ferrari = car ("FERARI","A SERIES",2022)
print(ferrari.model)    # .year or .manufacturer