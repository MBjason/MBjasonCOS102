class Man:# a class was created{MAN IS AN OBJECT}
    def __init__(self, name, age): #we created a function  and added name and age to it. so basically what the self keyword does is it acts as
        #reference whenever another variable would be defined. It is like a constant reference.
        self.name = name# this also helps the value of name to differ in the code. It could be changed
        self.age = age#same as the previous
    def get_name(self):#{A METHOD} now we have defined our main function. this main gets any inputed name and returns self name. remember self name was assigned to it previously
        return self.name
    def get_age(self):# same
        return self.age
    
m1 = Man("Jason", 18)#  we created our first variable m1.Assinged class man to is
m2 = Man("ROY", 18)#same
print(m1.get_name(),m1.get_age())
print(m2.get_name(), m1.get_age())

