class Person1:
    def __init__(self, name, age, work):
        self.name=name
        self.age=age
        self.work=work
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def job(self,career):
       print(f"Work: {self.work} career: {career}")


self = Person1("Thomas", 20, "Engineer")
self.display()
self.job("Software Engineer")

bet=Person1("Betty", 25, "Doctor")
bet.display()
bet.job("Pediatrician")

class Person2(Person1):
    pass

typ = Person2("Typ", 30, "Artist")
typ.display()
