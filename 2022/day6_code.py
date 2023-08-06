#2022 day6

with open('advent-of-code/2022/day6_input.txt' ,'r') as file:
    data = file.read().strip()

#<<---------------------part a------------------>>

# for i in range(0,len(data)-4):
#     t = data[i:(i+4)-len(data)]
#     if (t.count(t[0]) == 1) and (t.count(t[1]) == 1)  and (t.count(t[3]) == 1):
#         print(data.index(t)+4)
#         break
# else:
#     print(len(data))

#<<---------------------part b------------------>>

for i in range(0,len(data)-14):
    t = data[i:(i+14)-len(data)]
    for j in range(0,14):
        if t.count(t[j]) != 1: break
    else:
        print(data.index(t)+14)
        break
else:print(len(data))