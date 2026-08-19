#loops

counter =1 
while counter <= 5:
    print(counter)
    counter += 1
print("end of code")


i=5
while i > 0:
    print(i * "*")
    i -= 1


#1 to 10 => even
#for loop 
for i in range(1, 11):
    if i%2 == 0:
        print(i)
print("-----------------------")
for i in range(2, 11, 2):
    print(i)


 #multiples of 3  => 21 [ to 50]
#break use 

for i in range(1,51):
    if(i == 21):
        break
    if(i% 3 == 0):
        print(i)

print("out of loop")


for i in range(1,60):
    if(i == 21):
        continue
    if(i% 3 == 0):
        print(i)

print("out of loop")

#print all odd numbers form 1 to 20 
for i in range(1,21,2):
    print(i)

#print the table of 57
for i in range(1, 11):
    print(57 *i)

#print all multiples of 3 from 1 to 50 but skip 15
for i in range(3, 51, 3):
    if i == 15:
        continue
    print(i)

#take two integers a and b as input and find and 
# print the first number 
# 1 and 1000 that is divisible by both numbers 
a = int(input("Enter a: "))
b = int(input("Enter b: "))

for i in range(1, 1001):
    if i % a == 0 and i % b == 0:
        print(i)
        break