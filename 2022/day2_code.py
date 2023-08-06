#2022 day2 a

scor = 0

with open('advent-of-code/2022/day2_input.txt' ,'r') as file:
    data = [i.split() for i in file.read().strip().split('\n')]

d = {
    'A':1,
    'B':2,
    'C':3,
    'X':1,
    'Y':2,
    'Z':3
}

# <<----------part a-------------->>

# for i in data:
#     # print(i)
#     if d[i[0]] == d[i[1]] :
#         scor+=(d[i[1]] + 3)
#         # print('mosavi ',(d[i[1]] + 3))

#     elif d[i[1]] == 1:
#         scor += (1 + (-12 +(6*d[i[0]])))
#         # print('R ',(1 + (-12 +(6*d[i[0]]))))

#     elif d[i[1]] == 2:
#         scor += (2 + (9 -(3*d[i[0]])))
#         # print('P ', (2 + (9 -(3*d[i[0]]))) )

#     elif d[i[1]] == 3:
#         scor += (3 + (-6 +(6*d[i[0]])))
#         # print('S ',  (3 + (-6 +(6*d[i[0]]))))
#     # print()

# print (scor)

#<<-------------part b--------------->>

for i in data:
    if d[i[1]] == 1:
        scor += 1 if d[i[0]] == 2 else int(7/2 - d[i[0]]/2)
    elif d[i[1]] == 2:
        scor+= 3+ d[i[0]]
    elif d[i[1]] == 3:
        scor += 9 if d[i[0]] == 2 else int(5/2 - d[i[0]]/2)+6
print(scor)