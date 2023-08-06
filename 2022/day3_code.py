#2022 day3


charlis = []
with open('day3_input.txt' ,'r') as file:
    data = [i for i in file.read().strip().split('\n')]

#<<-----------------part a----------------------->>

# scor = 0
# for d in data:
#     l =int(len(d)/2)
#     if len(d) % 2 != 0 :print(d)

#     for i in d[:l]:
#         if i in d[l:] :
#             scor += ord(i) - 96 if ord(i) >= 97 else ord(i)-38
#             break

# print(scor)

#<<-----------------part b----------------------->>

scor = 0
l = 0
while l< len(data):
    print(l)
    for  i in data[l]:
        if i in data[l+1] and i in data[l+2]: 
            print(i)
            scor += ord(i) - 96 if ord(i) >= 97 else ord(i)-38
            break
    l+= 3
print(scor)