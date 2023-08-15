#2022 day4

with open('advent-of-code/2022/day4_input.txt' ,'r') as file:
    data = [i.split(',') for i in file.read().strip().split('\n')]

#<<---------------------part a----------------------->>

# sum = 0
# for d in data:
#     a = d[0].split('-')[0] if int(d[0].split('-')[0]) > int(d[1].split('-')[0]) else int(d[1].split('-')[0])
#     b = d[0].split('-')[1] if int(d[0].split('-')[1]) < int(d[1].split('-')[1]) else int(d[1].split('-')[1])
#     if  f'{a}-{b}' == d[0] or  f'{a}-{b}' == d[1] : sum+=1
# print(sum)
    
#<<--------------------part b-------------------------->>

sum = 0
for d in data:
    a = int(d[0].split('-')[0]) if int(d[0].split('-')[0]) > int(d[1].split('-')[0]) else int(d[1].split('-')[0])
    b = int(d[0].split('-')[1]) if int(d[0].split('-')[1]) < int(d[1].split('-')[1]) else int(d[1].split('-')[1])
    if a <= b : sum+=1
print(sum)