# Loop :


for i in range(1, 51):    
    print(i) 


for i in range(2, 101, 2):   
    print(i)


for i in range(1, 101, 2):   
    print(i)



for i in range(1, 11):          
    print(7 * i)



total = 0                        
for i in range(1, 101):          
    total += i                   
print(total)



for i in range(50, 0, -1):       
    print(i)



count = 0
for i in range(1, 101):
    if i % 3 == 0:              
        count += 1
print(count)


for i in range(1, 11):
    print(i * i)


for i in range(1, 11):
    print(i ** 3)



n = int(input("Enter number: "))   
for i in range(1, n+1):            
    print(i)


# While loop :


i = 1
while i <= 20:          
    print(i)
    i += 1 


n = int(input("Enter number: "))
fact = 1
i = 1

while i <= n:
    fact *= i           
    i += 1

print(fact)



num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10         
    rev = rev * 10 + digit   
    num //= 10               

print(rev)



num = int(input("Enter number: "))
count = 0

while num > 0:
    num //= 10          
    count += 1

print(count)


while True:
    data = input("Enter: ")
    if data == "stop":     
        break

# nested loop :

for i in range(1, 5):
    print("*" * i)


for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()



for i in range(1, 6):
    for j in range(1, 11):
        print(i*j, end=" ")
    print()



for i in range(3):
    print("A B C")



num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()


# String :


s = input("Enter string: ")
count = 0

for i in s:
    count += 1

print(count)



s = input("Enter string: ")
count = 0

for i in s:
    if i.lower() in "aeiou":   
        count += 1

print(count)



s = input("Enter string: ")
count = 0

for i in s:
    if i.isalpha() and i.lower() not in "aeiou":
        count += 1

print(count)




s = input("Enter string: ")
rev = ""

for i in s:
    rev = i + rev

print(rev)



s = input("Enter string: ")

if s == s[::-1]:      
    print("Palindrome")
else:
    print("Not Palindrome")


# string slicing :


s = "PythonProgramming"


print(s[:5])



print(s[-3:])



print(s[::-1])



print(s[::2])



print(s[1:-1])



# List :



lst = [10, 20, 30, 40, 50]


print(sum(lst))



print(max(lst))



print(min(lst))



print(len(lst))



x = 20
if x in lst:
    print("Exists")



#  List operations :


lst = []
lst.append(10)
lst.append(20)
lst.append(30)


lst.insert(1, 15)



lst.remove(20)



lst = [1,2,3,4]
rev = []

for i in lst:
    rev = [i] + rev

print(rev)



lst = [5,2,9,1]

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:          # Swap
            lst[i], lst[j] = lst[j], lst[i]

print(lst)


