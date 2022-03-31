#def simple_in():
 #   p=int(input("enter principal value :"))
  # r=int(input("enter rate :"))
 #   t=int(input("enter time :"))
 #   si=(p*r*t)/100
 #   print("simple intrest =", si)
#simple_in()
################################
#def simple_intrest(p,r,t):
#    print("princple value: ",p)
 #   print("rate % : ",r)
  #  print("time value : ",t)
   # si=(p*r*t)/100
   # print("simple intrest= ",si)
    #return si
#simple_intrest(100,20,2)
################# s-i ########################
#def simple_intrest(p,r,t):
#    return(p * r * t) / 100
#p=float(input("enter princple value: "))
#r=float(input("enter rate % : "))
#t=float(input("ente time : "))
#print("simple intrest= ",simple_intrest(p,r,t))
################ s-i #######################
#def func(name):
#    message ="Hi "+name
 #   return message
#name=input("enter the name : ")
#print(func(name))
##################### armstrong no #############
x=int(input("enter any no to find armstrng :"))
order=len(str(x))
temp=x
sum=0
while(temp!=0):
    r=temp%10
    sum=sum+r**order
    temp=temp//10
if x==sum:
    print(x," is an armstrong no")
else:
    print(x," is not armstrong no")
################## Array rotation ###############################
# def roarray(arr,n,d):
#     temp=[]
#     i=0
#     while (i<d):
#         temp.append(arr[i])
#         i=i+1
#     i=0
#     while (d<n):
#         arr[i]=arr[d]
#         i=i+1
#         d=d+1
#         arr[:]=arr[: i]+temp
#         return arr
# arr=[1,2,3,4,5,6,7]
# print("after rotation",end="")
# print(roarray(arr,len(arr),2))

