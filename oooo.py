class ID:
    def __init__(self,name,lastname,age):
        self.name=name
        self.lastname=lastname
        self.age=age
    def get_info(self):
        print(f"{self.name} {self.lastname} {self.age}")
nik=ID('nia',"zauk", 16)
nik.get_info()
nik1=ID('nып',"пk", 6)
nik1.get_info()