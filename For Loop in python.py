#  Loops in python : Loops are bascially a tool or a code or command to re-execute a group
#                               or a block of code over for multiple times
# There are 2 types of loops in python. For and While loop.


#  FOR LOOP :-
# a = range(0,70,5)
# for x in a:
#     print(x)
#     as well as this for loop works without a given variable tooo

# for y in range(0,35,3):
#      print(y)
    
# for p in range(-3,-16,-1):
#     print(p)


# QnA : Print a table of 12
#  ans

# for m in range(12,121,12):
#     print(m)

# run a code for a user in which he wants to run a multiplication table of any number where number = n
# ans

# n = int(input("Write the MUltiplication table of :-"))
# 
# for m in range(n , n*11 , n):
#     print(m)


#  loop for strings
# a = "You will have to win at any cost"
# # print(len(a))
# 
# for i in range(len(a)):
#     print(a[i])

# con = "INDIA"
# for x in con:
#     print(x)




# a = "CDA ACADEMY"
# # print(len(a))
# for i in range(11):
#     print(a[i])
#     
#     
# a = "I love AI and ML Learning"
# # print(len((a)))
# 
# for x in range(len(a)):
#     print(a[x])
#     

# for i in range(1,21):
#     if i == 15:
#         continue  
#print(i)
  
  
# for i in range(1,51,2):
#     if i == 39:
#         print("Break is executed")
#         break
#     print(i)
# else:
#     print("Break is not executed")



for m in range(0,61,5):
    if m ==55:
        print("Break is executed")
        break
    print(m)
else:
    print("Break is not executed")