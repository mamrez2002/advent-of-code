#2022 day1 

with open('day1_input.txt' ,'r') as file:
    data = [i for i in file.read().strip().split('\n')]
    # print(data)
m = []
sum = 0
for i in data:
    if i != '':
        sum += int(i)
    else:
        m.append(int(sum))
        sum = 0
# print(max(m))
sum = 0
for i in range(0,3):
    sum+= max(m)
    print(max(m))
    m.remove(max(m))
print(sum)