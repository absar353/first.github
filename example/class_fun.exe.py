class book:
    def __init__(self,name,author,price):
        self.name=name
        self.author=author
        self.price=price
    # def write(self):
    #      self.name=input("enter book name :")
    #      self.author=input("enter author name")
    #      self.price=input("enter price :")

    def read(self) :
        print(" book name - ",self.name,"\n author - ",self.author,"\n price - ",self.price)



while True:
    print("          menu \n 1. write \n 2. read \n 0. exit")
    ch=int(input("Enter your choice :-"))
    if ch==1:
        b1 = book(name=input("enter book name: "), author=input("enter author name: "), price=input("enter price: "))
       #b1.write()
    elif ch==2:
      try:
          b1.read()
      except:
          print("choice 1 first")
    else:
        break
