input1 = int(input("Enter the size: "))
input2 = [ int(input("Enter the price ")) ]

cal = 0
total = 0
for i in range(0, input1-1):

     amt = int(input()) #but this time no input string because we already taken above as input2

     input2.append(amt) # and we taken input in list

print (input2) #check it is appended or not by printing
#to not take 1st billing amount we have to do slicing like this

for a in input2[2:]:
    

        cal = ( a - 1000) / 10   # this is how we get the calculations for each billing amounts except 1st one

        total = total + cal   # add all calculations for final output

print (total)

input1 = int(input("Enter the size: "))

#i am using list comprehension here to make input as a list

input2 = [ int(input("Enter the billing amount: ")) ]

cal = 0

total = 0 #assume

for i in range(0, input1-1):

     #again taken input

     amt = int(input()) #but this time no input string because we already taken above as input2

     input2.append(amt) # and we taken input in list

#to not take 1st billing amount we have to do slicing like this

for a in input2[1:]:

        cal = ( a - 1000) / 10   # this is how we get the calculations for each billing amounts except 1st one

        total = total + cal   # add all calculations for final output

print (total)
