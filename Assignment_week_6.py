#1 create a credit card class with the following attributes: 
#card number, expiration date, and security code. 
#Create a method that will print out the card number, 
#expiration date, and security code.
#Create an instance of the class and call the method.

class CreditCard:
    # Main Method
    @staticmethod
    def main(args):
        number = 5196081888500645
        print(str(number) + " is " +
              ("valid" if CreditCard.isValid(number) else "invalid"))
         
    # Return true if the card number is valid
    @staticmethod
    def isValid(number):
        return (CreditCard.getSize(number) >= 13 and CreditCard.getSize(number) <= 16) and (CreditCard.prefixMatched(number, 4) or CreditCard.prefixMatched(number, 5) or CreditCard.prefixMatched(number, 37) or CreditCard.prefixMatched(number, 6)) and ((CreditCard.sumOfDoubleEvenPlace(number) + CreditCard.sumOfOddPlace(number)) % 10 == 0)
     
    # Get the result from Step 2
    @staticmethod
    def sumOfDoubleEvenPlace(number):
        sum = 0
        num = str(number) + ""
        i = CreditCard.getSize(number) - 2
        while (i >= 0):
            sum += CreditCard.getDigit(int(str(num[i]) + "") * 2)
            i -= 2
        return sum
       
    #2  Return this number if it is a single digit, otherwise,
    # return the sum of the two digits
    @staticmethod
    def getDigit(number):
        if (number < 9):
            return number
        return int(number / 10) + number % 10
       
    # Return sum of odd-place digits in number
    @staticmethod
    def sumOfOddPlace(number):
        sum = 0
        num = str(number) + ""
        i = CreditCard.getSize(number) - 1
        while (i >= 0):
            sum += int(str(num[i]) + "")
            i -= 2
        return sum
       
    # Return true if the digit d is a prefix for number
    @staticmethod
    def prefixMatched(number,  d):
        return CreditCard.getPrefix(number, CreditCard.getSize(d)) == d
       
    # Return the number of digits in d
    @staticmethod
    def getSize(d):
        num = str(d) + ""
        return len(num)
       
    # Return the first k number of digits from
    # number. If the number of digits in number
    # is less than k, return number.
    @staticmethod
    def getPrefix(number,  k):
        if (CreditCard.getSize(number) > k):
            num = str(number) + ""
            return int(num[0:k])
        return number
 
if __name__ == "__main__":
    CreditCard.main([])
 

#create Animal class and Dog class. Make the Dog class inherit from the Animal class. 
# Add a bark method to the Dog class. Create an instance of the Dog class and call the 
# bark method.


class Dog():
    def makeSound(self):
        print('bark')

 #sound       
sam:Dog ()

sam.makeSound()

class Dog():
    sound = 'bark'
    
    def makeSound(self):
        print(self.sound)  
        
sam:Dog()

sam.makeSound()


#create a class called Queue. The class should have the following methods: 
# enqueue, dequeue, and size. The enqueue method should add an item to the queue. 
# The dequeue method should remove an item from the queue. 
# The size method should return the size of the queue.
  
  
from queue import Queue
  
# Initializing a queue
q = Queue(maxsize = 3)
  
# qsize() give the maxsize 
# of the Queue 
print(q.qsize()) 
  
# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')
  
# Return Boolean for Full 
# Queue 
print("\nFull: ", q.full()) 
  
# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
  
# Return Boolean for Empty 
# Queue 
print("\nEmpty: ", q.empty())
  
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())
  

#create a class called Stack. The class should have the following methods: 
# push,pop, and size. The push method should add an item to the stack. 
#The pop method should remove an item from the stack. 
#The size method should return the size of the stack.


 
# append() function to push

stack =(a,b,c)

stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)


#create a class called Person. 
# The class should have the following attributes: name, age, and address. 
# The class should have the following methods: eat, sleep, and work. 
# The eat method should print out the name of the person and the word "is eating". 
# The sleep method should print out the name of the person and the word "is sleeping". 
# The work method should print out the name of the person and the word "is working"


class Person:
    def __init__(self,Name,Age,Address):
        self.Name=Name
        self.Age=Age
        self.Address=Address
   
    def eat(self):
        print("{} is eating".format(self.Name))

    def sleep(self):
        print("{} is sleeping".format(self.Name))


  
    def work(self):
        print("{} is working".format(self.Name))

    
#Creating an object
obj_1=Person("besty",20,"Male")

obj_1.eat('betsy' is 'eating')

obj_1.sleep('betsy' is 'sleeping')

obj_1.work('betsy' is 'working')



#create a class called Employee. 
# The class should have the following attributes: name, age, and salary. 
# The class should have the following methods: eat, sleep, and work. 
# The eat method should print out the name of the person and the word "is eating". 
# The sleep method should print out the name of the person and the word "is sleeping". 
# The work method should print out the name of the person and the word "is working". 
# Create a subclass of Employee called Programmer. 
# The Programmer class should have the following attributes: 
# name, age, salary, and programming language. 
# The Programmer class should have the following methods: eat, sleep, work, and code. 
# The code method should print out the name of the person and the word "is coding in" and the programming language. 
#Create an instance of the Programmer class and call all the methods.

class Employee:
    def __init__(self,Name,Age,Salary):
        self.Name=Name
        self.Age=Age
        self.Salary=Salary
   
    def eat(self):
        print("{} is eating".format(self.Name))

    def sleep(self):
        print("{} is sleeping".format(self.Name))
  
    def work(self):
        print("{} is working".format(self.Name))

    
#Creating an object
obj_1=Person("besty",20,"Male")

obj_1.eat('betsy' is 'eating')

obj_1.sleep('betsy' is 'sleeping')

obj_1.work('betsy' is 'working')












