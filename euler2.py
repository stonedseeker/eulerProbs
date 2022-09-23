#secondByMe
supersum = 0
sum = 0
prev = 0
next = 1
# for i in range(400000):
#     # 0 1 1
#     # 1 1 2
#     # 1 2 3
#     # 2 3 5
#     # 3 5 8
#     sum = prev + next
#     prev = next 
#     next = sum

#     if sum % 2 == 0:
#         supersum += sum

while True:
    sum = prev + next
    prev = next 
    next = sum 

    if sum >= 4000000: 
        break
    if sum % 2 == 0:
        supersum += sum

print(supersum)
