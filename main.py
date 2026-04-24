#4-m
class Talaba:
    def __init__(self, ism, yosh, kurs):
        self.ism = ism
        self.yosh = yosh
        self.kurs = kurs
        
    def name(self):
        print(f"mening ismim: {self.ism}")
        
    def age(self):
        print(f"Men {self.yosh} daman")
        
    def curs(self):
        print(f"Men {2}kurs man")
        
u1 = Talaba("Ali", 20, 2)
u1.name()
u1.age()
u1.curs()
