#2022 day5

with open('day5_input.txt' ,'r') as file:
    data = [i for i in file.read().strip().split('\n')]

d = [[0]]
for i in range(0,9):
    d.append(list(data.pop(0)))

#<<------------------part a------------------->>
# for _ in data:
#     l = _.split()
#     r ,f,t = int(l[1]),int(l[3]),int(l[5])
#     for i in range(0,r):
#         d[t].append(d[f].pop())

# for i in d:
#     print(i.pop() , end='')

#<<-------------------part b-------------------->>

for _ in data:
    nd=[]
    l = _.split()
    r ,f,t = int(l[1]),int(l[3]),int(l[5])
    for i in range(0,r):
        nd.append(d[f].pop())
    for i in range(0,r):
        d[t].append(nd.pop())
for i in d:
    print(i.pop() , end='')