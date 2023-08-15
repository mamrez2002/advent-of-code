#2022 day7

with open('advent-of-code/2022/day7_input.txt' ,'r') as file:
    datas = [i for i in file.read().strip().split('\n')]



dirs = {'/home':0}
path = '/home'

for data in datas:

    if data[0] == "$":

        if data.split()[1] == 'ls':
            pass

        elif data.split()[1] == 'cd':

            if data.split()[2] == '/':
                path = '/home'

            elif data.split()[2] == '..':
                path = path[0:path.rfind('/')]
            
            else:
                dir_name = data.split()[2]
                path += '/' + dir_name
                dirs.update({path:0})


    elif data.split()[0] == 'dir':
        pass

    else:
        size = int(data.split()[0])

        dir = path
        for i in range(path.count('/')):
            dirs[dir] += size
            dir = dir[0:dir.rfind('/')]

#<<-----------------------part a-------------------->>

# total = 0
# for i in dirs:
#     print(i,' = ',dirs[i])
#     if dirs[i] <= 100000:
#         total += dirs[i]
# print(total)


#<<---------------------part b----------------------->>

total = []
limit = 30000000 - (70000000 - dirs['/home'])
for i in dirs:
    if dirs[i] >= limit:
        total.append(dirs[i])
total.sort()
print(total[0])