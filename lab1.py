
# example 01(lab 1 complate)
        # x = int(input("enter your number here :"))
        # y = int(input("enter your number here :"))
        # print(x+y)

# example 02(lab 2 complate)
        # x = 5
        # print(type(x))

        # f_name="menaka"
        # l_name='lakshan'
        # print((type(f_name)==type(l_name)))

        # comp_num=1+6j
        # print(type(comp_num))

        # x=10
        # y=11
        # print(id(x))
        # print(id(y))   memory location

        # weight = "55.45454"
        # print(int(float(weight)))  # Output: 55

        # devision=10/4
        # print(devision)

        # devision=10//4
        # print(devision)

        # and,or,not are use in python as the logical oparators

        # genarate random numbers
        # import random  # randome is a package
        # ran_num = random.random()
        # print(ran_num)

        # list1=[10,20,'home',10.20,78]
        # print(list1[-2])  #access array  [-5,-4,-3,-2,-1]

        # list1.append(111)  #append array
        # print(list1)

        # list1[2]=222
        # print(list1)  #append own place

        # list1.remove(10)
        # print(list1)  #remove value

        # del list1[2]
        # print(list1)  #delete index value

        # print (list1[2:])
        # print (list1[2:4])  #access values in a range

        # list2diamentional=[[10,20,30,40],[11,22,33,44],[12,24,36,48,60]]
        # print(list2diamentional[2][3])  #access two diamentional array

        # print(len(list2diamentional))  #get the legnth of array

        # x=[1,2,3,4,5]
        # y=[6,7,8,9,10]
        # print(x+y)    # array concatination

        # print([100]*5)   #repition

        # print(4 in [1,2,3,4,5]) #membership

        # for x in [1,2,3,4]:
        #    print(x)            #itaration

        # for counter in [1,2,3,5]:
        #    print("Hello World")

        # x=list(range(0, 100, 4))  #create a array
        # print(x)   #[0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96]

        # y=list(range(5,20))
        # print(y) #[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

        # z=list(range(15))
        # print(z) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# example 03(lab 3 complate)

        # memberinput=float(input("enter your marks: "))
        # if(memberinput<0):
        #    print('error input')
        # elif(memberinput<40):
        #    print('f')
        # elif(memberinput<60):
        #    print('c')
        # elif(memberinput<80):
        #   print('b')
        # elif(memberinput<100):
        #    print('A')
        # elif(memberinput>100):
        #    print('error input')

# example 04(lab 4 complate)l
        #while(True):
        # memberinput = float(input("enter your marks: "))
        # if(memberinput<0):
        #         print('error input')
        # elif(memberinput<40):
        #         print('f')
        # elif(memberinput<60):
        #         print('c')
        # elif(memberinput<80):
        #         print('b')
        # elif(memberinput<100):
        #         print('A')
        # elif(memberinput>100):
        #         print('error input')
        # memberinput1 = input("may i continue this y/n: 45")   
        # if(memberinput1=='n'):
        #         break

        #print('thanx for you')


#maximam members are 40

#for i in range(0,40):
 #       memberinput = float(input("enter your marks: "))
 #       if(0<=memberinput<=100):
  #              if(memberinput<0):
 #                       print('error input')
 #               elif(memberinput<40):
 #                       print('f')
 #               elif(memberinput<60):
 #                       print('c')
 #               elif(memberinput<80):
 #                       print('b')
 #               elif(memberinput<100):
 #                       print('A')
 #               elif(memberinput>100):
 #                       print('error input')
 #               memberinput1 = input("may i continue this y/n: ")   
 #               if(memberinput1=='n'):
 #                       break
 #       else:
 #               print('invalid marks plz re enter')
#print('thanx for you')  



#   python input and outputs

# print and input
#print(1,2,3,4,5)
#print(1,2,3,4,5, sep='-')
#print(1,2,3,4,5, sep='*',end='#')

#funcitions
'''
import math
rr=int(input('enter radious in circle : '))

def area_of_circle(r):
    return(math.pi*r**r)

print("area of of the circle is :",area_of_circle(rr))
area_of_circle(rr)
'''
#error handling
'''
num_input = input('Enter a number:')

try:
  num_val = int(num_input)
except:
  num_val = -1

if num_val > 0:
  print('A number was entered!')
else:
  print('Not a number!')
'''
#file handling in python
'''
x=open("readetextfile.txt").read()
y=x.read()
print(y)
'''

#reade a file after writing
'''
x=open("readetextfile.txt","w")
mystring="$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
x.write(mystring)
x=open('readetextfile.txt')
y=x.read()
print(y)
'''

#python strings
'''
print("hello"+"world")
print("hello"*5)
x="menaka"
print(x[0])
print(x[0:5])
print(x[2:6])
print(x[-1]) # lass caractor(a)
print(x[-2]) # 2nd lass caractor(k)
print(x[-2:]) # lass caractors(ka)
print(x[:-2]) # lass caractors(ka)
print(len(x))

#membership(in, not in)
m='m'
print(m in x)
z='z'
print(z not in  x)
'''

def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def multy(a,b):
    return(a*b)
def dev(a,b):
    if(b==0):
        print("Not a valid number,please enter again")
        return None
    else:
        return(a/b)
def power(a, b):
    return a ** b
def remainder(a, b):
    if b == 0:
        print("Not a valid number,please enter again")
        return None
    else:
        return (a % b)

def select_op(choice):
    if choice == '+':
        return add
    elif choice == '-':
        return sub
    elif choice == '*':
        return multy
    elif choice == '/':
        return dev
    elif choice == '^':
        return power
    elif choice == '%':
        return remainder
    else:
        print("Unrecognized operation")
        return None

while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  a = input("Enter 1st number: ")
  b = input("Enter 22st number: ")
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  print(a)
  print(b)


  if(select_op(choice) == -1):
    print("Done. Terminating")
    exit()

