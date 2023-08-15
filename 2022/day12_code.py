#2022 day 12

with open('2022/day12_input.txt' ,'r') as file:
    data = [list(i) for i in file.read().strip().split('\n')]

#<<---------------------------part a-------------------------->>

# for r , row in enumerate(data):
#     for c , item in enumerate(row):
#         if item == 'S':
#             sr = r
#             sc = c
#             data[r][c] = 'a'
#         if item == 'E':
#             er = r
#             ec = c
#             data[r][c] = 'z'
        
# q = []
# q.append((0,sr,sc))
# vis = {(sr, sc)}

# while q:
#     d , r , c = q.pop(0)
    
#     for nr ,nc in [( 1+ r , c) , (r - 1, c),(r, c + 1), (r, c - 1)]:
#         if nr < 0 or nr >= len(data) or nc < 0 or nc >= len(data[0]):
#             continue
#         if (nr , nc ) in vis:
#             continue
#         if ord(data[nr][nc]) - ord(data[r][c]) > 1:
#             continue
#         if nr == er and nc == ec:
#             print('part a : ', d + 1)
#             exit(0)
#         vis.add((nr , nc))
        
#         q.append((d+1 , nr , nc))


#<<-----------------------------part b------------------->>

for r , row in enumerate(data):
    for c , item in enumerate(row):
        if item == 'S':

            data[r][c] = 'a'

        if item == 'E':
            er = r
            ec = c
            data[r][c] = 'z'
        
q = []
q.append((0,er,ec))
vis = {(er, ec)}

while q:
    d , r , c = q.pop(0)
    
    for nr ,nc in [( 1+ r , c) , (r - 1, c),(r, c + 1), (r, c - 1)]:
        if nr < 0 or nr >= len(data) or nc < 0 or nc >= len(data[0]):
            continue
        if (nr , nc ) in vis:
            continue
        if ord(data[nr][nc]) - ord(data[r][c]) < -1:
            continue
        if data[nr][nc] == 'a':
            print('part 2 :',d + 1)
            exit(0)
        vis.add((nr , nc))
        
        q.append((d+1 , nr , nc))