# inheritance came in handy when we can user methods defined under one class into others

class Mamale:
    def walk(self):
        print("walk")


#to inherit mamale in other class we need to pass name of parent class in paranthesis

class dog(Mamale):
    pass
# pyhton does not like empty class so it will throw error - so to avoid this we can write pass


class cat(Mamale):
    def meow(self):
        print("meow")

cat = cat()
cat.meow()
cat.walk()

#after inheritance subclass have access to all the methods defined under parent class