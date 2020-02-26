def out(num):
    if num == 0:
        return 'N'
    else:
        return str(num)

def main():
    obj = [int(x) for x in input().split()][1:]
    a1 = a2 = a3 = a4 = a5 = 0
    f1 = 1
    f2 = 0
    for i in obj:
        if i % 10 == 0:
            a1 += i
        elif i % 5 == 1:
            a2 += (-1)**(f1+1)*i
            f1 += 1
        elif i % 5 == 2:
            a3 += 1
        elif i % 5 ==3:
            f2 += 1
            a4 += i
        elif i % 5 == 4:
            if i > a5:
                a5 = i
    if f1 == 1:
        a2 = 'N'
    elif a2 == 0:
        a2 = '0'
    if f2 == 0:
        a4 = 'N'
    else:
        a4 = '{:.1f}'.format(a4/f2)
    print(' '.join(list(map(out,[a1,a2,a3,a4,a5]))))

if __name__ == '__main__':
    main()