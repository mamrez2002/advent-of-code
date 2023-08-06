#2022 day9
import time,os

with open('advent-of-code/2022/day9_input.txt' ,'r') as file:
    data = [i for i in file.read().strip().split('\n')]

mp = [list(1000*'.') for i in range(0,1000)]



{
#<<-------------------part a------------------->>

# mp[19][0] = '#'
# fix = []
# h , s = [19,0],[19,0]

# def check():
#     # os.system('cls')
#     # for i in mp:
#     #     print(''.join(i))
#     # time.sleep(0.3)

#     if abs(h[0] - s[0]) > 1 or abs(h[1] - s[1]) > 1 : return True
#     else : return False


# for move in data:

#     # move up
#     if move[0] == 'U':

#         for i in range(int(move.split()[1])):

#             h[0] -= 1
#             if check():
#                 s[0] = h[0] + 1
#                 s[1] = h[1]
#                 mp[s[0]][s[1]] = "#"

#     # move down
#     elif move[0] == 'D':

#         for i in range(int(move.split()[1])):

#             h[0] += 1
#             if check():
#                 s[0] = h[0] -1 
#                 s[1] = h[1]
#                 mp[s[0]][s[1]] = "#"

#     # move rith
#     elif move[0] == 'R':

#         for i in range(int(move.split()[1])):

#             h[1] +=1
#             if check() :
#                 s[0] = h[0]
#                 s[1] = h[1] - 1
#                 mp[s[0]][s[1]] = "#"

#     # move left
#     elif move[0] == 'L':

#         for i in range(int(move.split()[1])):

#             h[1] -= 1
#             if check():
#                 s[0] = h[0]
#                 s[1] = h[1] + 1
#                 mp[s[0]][s[1]] = "#"
    
# for i in mp:
#     # print(''.join(i))
#     fix.append(''.join(i))

# print('part a ---> ',''.join(fix).count('#'))
}

#<<--------------------part b------------------->>
r = [8,7,6,5,4,3,2,1,0]
# mp[19][0] = '#'

h = [[100,16 ] for i in range(10)]
fix = []
def prt():
    fix =[]
    # os.system('cls')
    mp[h[0][0]][h[0][1]] = '#'
    # for _ in range(10):
    #     i = h[_]
    #     print(i,'  ',h.index(i))
    #     if mp[i[0]][i[1]] != '#':
    #         mp[i[0]][i[1]] = str(_)

    for i in mp:
        # print(''.join(i))
        fix.append(''.join(i))
    print('part a ---> ',''.join(fix).count('#'))
    # time.sleep(0.1)

def check(n):
    # prt()
    ans = []
    if abs(h[n+1][0] - h[n][0]) > 1 or abs(h[n+1][1] - h[n][1]) > 1 : 
        ans.append(True)

        if h[n+1][0] - h[n][0] > 0 : ans.append(1)
        elif h[n+1][0] - h[n][0] < 0 : ans.append(-1)
        else : ans.append(0)

        if h[n+1][1] - h[n][1] > 0 : ans.append(1)
        elif h[n+1][1] - h[n][1] < 0 : ans.append(-1)
        else : ans.append(0)
        
    else : ans.append(False)
    return ans

for move in data:
    
    # move up 
    if move[0] == 'U':
        for i in range(int(move.split()[1])):
            h[9][0] -= 1

            for j in r:
                c = check(j)

                if c[0]:
                    h[j][0] += c[1]
                    h[j][1] += c[2]
            prt()
        



    # move down
    elif move[0] == 'D':
        for i in range(int(move.split()[1])):
            h[9][0] += 1

            for j in r :
                c = check(j)

                if c[0]:
                    h[j][0] += c[1]
                    h[j][1] += c[2]
            prt()            

    # mvoe right
    elif move[0] == 'R':
        for i in range(int(move.split()[1])) :
            h[9][1] += 1

            for j in r:
                c = check(j)

                if c[0]:
                    h[j][0] += c[1]
                    h[j][1] += c[2]
            prt()            
                
    elif move[0] == 'L':
        for i in range(int(move.split()[1])):
            
            h[9][1] -= 1

            for j in r:
                c = check(j)

                if c[0]:
                    h[j][0] += c[1]
                    h[j][1] += c[2]
            prt()
        
