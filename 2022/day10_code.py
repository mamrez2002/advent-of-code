#2022 day 10

with open('2022/day10_input.txt' ,'r') as file:
    data = [i for i in file.read().strip().split('\n')]

ths = [20,60,100,140,180,220]


#<<------------------------part a---------------------------->>
# sum = 0

# values = [1]
# for i in data:
#     values.append(values[-1])
#     if i.split()[0] == 'addx':
#         values.append(values[-1] + int(i.split()[1]))

# for i in ths:
#     sum+= i * values[i -1]
#     print(i ,'*', values[i -1] , '=' ,  i * values[i -1])
# print('======part a==>' , sum)

#<<-------------------------part b------------------------------>>

crt =  []
pix = 0
Sprite = 0
for value in data:
    

    if value.split()[0] == 'addx':

        for _ in range(2):

            if pix >= Sprite and pix <= Sprite+2:

                crt.append('#')
                pix +=1

            else :

                crt.append('.')
                pix +=1

            if pix == 40:
                pix = 0
                crt.append('\n')

        Sprite += int(value.split()[1])

    else:

        if pix >= Sprite and pix <= Sprite +2:

            crt.append('#')
            pix+=1
        else:
            crt.append('.')
            pix +=1

    if pix == 40:
        pix = 0
        crt.append('\n')


a = ''.join(crt)
print(a)
    

