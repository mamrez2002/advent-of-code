#2022 day 11

import re 
import gmpy2

with open('2022/day11_input.txt' ,'r') as file:
    data = file.read().replace(':','').replace(',','').split('\n\n')

# print(data[0].split())
monkeys = []
monkeys_operation = []

for i in data:
    string = ' '.join(i.split())

    monkeys.append([int(i) for i in ''.join(re.findall('items (.*)O' , string)).strip().split()])

    monkeys_operation.append({
        'operation' : ' '.join(re.findall('old (.*) T',string)).strip().split(),
        'test' : int(' '.join(re.findall('by (\d*) ',string)).strip()),
        'true' : int(' '.join(re.findall('true throw to monkey (\d*) I',string)).strip()),
        'false' : int(' '.join(re.findall('false throw to monkey (\d*).*',string)).strip())
    })
inspects  = len(monkeys)*'0'.split()
inspects  = [int(i) for i in inspects ]

#<<--------------------------part a-------------------------------->>

# for _ in range(20):
#     print('round ',_+1,' :')

#     for i in range(len(monkeys)):
#         for j in monkeys[i]:
#             old = j
#             new = 0
#             inspects[i] += 1
#             # operatons
#             if monkeys_operation[i]['operation'][0] == '+':

#                 if monkeys_operation[i]['operation'][1] == 'old':
#                     new = old + old
#                 else :
#                     new = old + int(monkeys_operation[i]['operation'][1])
            
#             elif monkeys_operation[i]['operation'][0] == '*':

#                 if monkeys_operation[i]['operation'][1] == 'old':
#                     new = old * old
#                 else :
#                     new = old * int(monkeys_operation[i]['operation'][1])

#             new = new // 3

#             # Test
#             if new % int(monkeys_operation[i]['test']) == 0:
#                 monkeys[monkeys_operation[i]['true']].append(new)
#             else:
#                 monkeys[monkeys_operation[i]['false']].append(new)
        
#         monkeys[i] = []

#     for i in range(len(monkeys)):
#         print('    monkey',i, ' --> ',monkeys[i])
#     print()

# for i in range(len(inspects)):
#     print('monkey',i,'inspected items',inspects[i],'items')

# inspects.sort(reverse=True)
# print('==== part a =====>',inspects[0]* inspects[1])


#<<------------------------------------part b----------------------------->>
modulus = 1
for i in monkeys_operation:
    modulus*= i['test']

for _ in range(10000):
    print('round ',_+1,' :')

    for i in range(len(monkeys)):
        for j in monkeys[i]:
            old = j
            new = 0
            
            # operatons
            if monkeys_operation[i]['operation'][0] == '+':

                if monkeys_operation[i]['operation'][1] == 'old':
                    new = old + old
                else :
                    new = old + int(monkeys_operation[i]['operation'][1])
            
            elif monkeys_operation[i]['operation'][0] == '*':

                if monkeys_operation[i]['operation'][1] == 'old':
                    new = old * old
                else :
                    new = old * int(monkeys_operation[i]['operation'][1])

            

            # Test
            if new % int(monkeys_operation[i]['test']) == 0:
                monkeys[monkeys_operation[i]['true']].append(new % modulus)
            else:
                monkeys[monkeys_operation[i]['false']].append(new % modulus)
        
        inspects[i]+= len(monkeys[i])
        monkeys[i] = []

    for i in range(len(inspects)):
        print('monkey',i,'inspected items',inspects[i],'items')

inspects.sort(reverse=True)
print('==== part b =====>',(inspects[0]* inspects[1]))


