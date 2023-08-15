#2022 day 13

with open('2022/day13_input.txt' , 'r') as file:
    data = [i for i in file.read().strip().split('\n\n')]



def check_item(l, r):
    leftItem = l if type(l) == list else eval('['+ str(l) + ']')
    rightItem = r if type(r) == list else eval('['+ str(r) + ']')

    if len(leftItem) == 0 or len(rightItem) == 0:
        if len(leftItem) == len(rightItem):
            return '#'
        else:
            if len(leftItem) == 0 : return True
            elif len(rightItem) == 0 : return False
    
    loop = len(leftItem) if len(leftItem) <= len(rightItem) else len(rightItem) 

    for i in range(loop):
        if type(leftItem[i]) == list or type(rightItem[i]) == list:
            if check_item(leftItem[i] , rightItem[i]) == '#': pass
            else : return check_item(leftItem[i] , rightItem[i])
        
        elif leftItem[i] < rightItem[i] : return True
        elif leftItem[i] > rightItem[i] : return False
        else : continue  #return '#'

    if len(leftItem) < len(rightItem) : return True
    elif len(leftItem) > len(rightItem) : return False
    else : return '#'

        
#<<----------------------------part a---------------------------->>

# sum = 0
# for j , i in enumerate(data):

#     left = eval(i.split('\n')[0])
#     right = eval(i.split('\n')[1])
#     check = check_item(left, right)

#     if check == True:

#         sum += j+1
    
# print('--part a--> :' , sum)


#<<---------------------------part b--------------------------->>

data.append('''[[2]]\n[[6]]''')
lis = []
for i in data:
    lis.append(eval(i.split('\n')[0]))
    lis.append(eval(i.split('\n')[1]))
data = ['*' for i in range(len(lis))]

# data = [data[14]]


for item in lis:
    sum = 0
    for i in lis:
        if item != i:
            if check_item(item , i):
                sum += 1
    data[(len(lis)-1) - sum] = item


print('--part b--> :' , (data.index([[2]])+1) * (data.index([[6]])+1))