#what is lopp?
#a loop is used to repeat a block of code multiple times until a condition is met.

##TYPES OF LOOPS IN PYTHON
#1] For Loop
#used when we know how many times we want to repeat.
#syntax:
#for variable in sequence:
    #code

#range() is commonly used to generate a sequence of numbers.
#range comes with 3 parameters.
#1.start(inclusive)
#2.stop(exclusive)
#3.step(optional,default is 1)
#example:
for i in range(1,6):
    print(i)
#output:12345

#key points-
#1.range(start,stop)generates number
#2.loops runs fixed number of times.


#2]While Loop
#used when we repeat until a condition become false.
#syntax:
#while condition:
# code
#example:
i=1
while i<=5:
    print(i)
    i+=1
#output:12345
#keypoints;
# 1

# loops conrtol statement: 
# 1.break
# stops the loop immediately.
# example:
for i in range(1,6):
    if i == 3:
        break
    print(i)  
#output:12
# 2.continue
# skips current iteration.
# example
for i in range(1,6):
    if i == 3:
        continue
    print(i)  
#output:12345
# 3.pass
#does nothing (placeholder)
for i in range(5):
    pass 


#task1
#print numbers from 1 to 10 using for loop.
for i in range(1,11):
    print(i)

#task2
# #print even numbers from 1 to 20.
#first method
for i in range(2,21,2):
        print(i,end='')

#second method  
for i in range(2,21):
    if i % 2 == 0:
        print(i,end='')

#task3
# print odd numbers from 1 to 15. 
#ascending order   
for i in range(1,16,2):
        print(i,end='')
#decending order
for i in range(21,1,-2):
        print(i,end='')

#task4
#print each character of string.text="python"  
#first method
for char in "python":
    print(char)  

#second method
string="python"
for char in string:
     print(char)     

#task5
#print all items in the list.
##data=["data","science","ai"]  
data=["Data","Science","AI"] 
for item in data:
     print(item)

#task6
#find the sum of numbers from 1 to 10.
sum=0
for i in range(1,11):
     sum=sum+i
     print(sum)

#task7
#print multiplication of table 5.
for i in range(1,11):
     print("5 x",i,"=",5 * i)   

#task8
#count how many vowels are in a string.  
text="hello world"   
count=0
for ch in text:
     if ch.lower()in"aeiouAEIOU":
          count+=1
          print("num of vowels:",count)

#task9
#print numbers in reverse order from 10 to 1.
for i in range(10,0,-1):
     print(i)    

#task10     
#print square of numbers from 1 to 5.
#first method        
for i in range(1,6):
     print("ans:",i**2)

#second method        
for i in range(1,6):
     print("ans:",i*i)  
     
            