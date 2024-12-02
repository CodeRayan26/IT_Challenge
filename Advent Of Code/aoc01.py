l1 = []
l2 = []
l1c = []
l2c = []

ans_part1 = 0
ans_part2 = 0



with open("input01.txt",'r') as input:
    for line in input :
        numbers = line.split()
        num1, num2 = map(int, numbers)
        l1.append(num1)
        l2.append(num2)
        l1c.append(num1)
        l2c.append(num2)



for i in range(0,len(l1)):
    ans_part1 = ans_part1 + abs(min(l1c) - min(l2c))
    l1c.remove(min(l1c))
    l2c.remove(min(l2c))

print(ans_part1)

for i in range(0,len(l1c)):
    found = 0
    for j in range(0,len(l2c)):
        if l2[j] == l1[i]:
            found = found + 1
    ans_part2 = ans_part2 + l1[i] * found

print(ans_part2)