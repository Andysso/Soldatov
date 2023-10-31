m = list()

for i in range(10):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

b = 0
s = 0

for i in range(len(m)):
    if m[len(m)-1] < m[i]:
        b += 1
    elif m[len(m)-1] > m[i]:
        s += 1

print('Количество меньших максимального элемента:',s,'\n','Количество больших максимального элемента:',b)
