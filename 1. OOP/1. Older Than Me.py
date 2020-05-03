class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def compareAge(self,other):
        if other.age>self.age:
            print(other.name,"'s is greater than {}'s age".format(self.name))
        else:
            print(other.name,"'s age is lesser than {}'s age".format(self.name))


p1=Person('Samuel',24)
p2=Person('Joel',22)
p3=Person('Lilly',38)

p1.compareAge(p2)