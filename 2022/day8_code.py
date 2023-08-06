#2022 day8

with open('day8_input.txt' ,'r') as file:
    data = [i for i in file.read().strip().split('\n')]



#<<---------------------------part a---------------------->>

# trees = (2*(len(data) + len(data[0])))-4

# for i in range(1,len(data[0])-1):

#     for j in range(1,len(data)-1):

#         column = [row[j] for row in data]
#         column = ''.join(column)
#         tree = data[i][j] 

#         if max(data[i][:j]) < tree or max(data[i][j+1:]) < tree:
#             trees += 1

#         elif max(column[:i]) < tree or max(column[i+1:]) < tree:
#             trees+= 1
        
#         else:
#             pass

# print(trees)

#<<--------------------------------part b----------------------------->>

score = []

for i in range(1,len(data[0])-1):

    for j in range(1,len(data)-1):
        left,rith ,up,down = 0,0,0,0

        column = [row[j] for row in data]
        column = ''.join(column)
        tree = data[i][j] 

        for z in ''.join(list(reversed(data[i][:j]))):
            if z < tree:left +=1
            else: 
                left +=1
                break
        
        for z in data[i][j+1:]:
            if z < tree: rith+=1
            else :
                rith+=1
                break
        
        for z in ''.join(list(reversed(column[:i]))):
            if z < tree :up+=1
            else: 
                up+=1
                break
        
        for z in column[i+1:]:
            if z < tree: down+= 1
            else: 
                down+=1
                break

        score.append(up*down*rith*left)
        
print(max(score))

        