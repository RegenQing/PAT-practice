def main():
    n = input()
    cal = []
    num = [int(x) for x in str(input()).split()]
    result = sorted(num,reverse = True)
    for i in num:
        if i in cal:
            continue
        else:
            while i != 1:
                cal.append(i)
                if i % 2 == 0:
                    i /= 2
                    if i in result:
                        result.remove(i)
                else:
                    i = 1.5 * i + 0.5
                    if i in result:
                        result.remove(i)
    for i in range(len(result)):
        print(result[i],end='' if i == len(result)-1 else ' ')

if __name__ == '__main__':
    main()