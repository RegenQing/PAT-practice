def PAT(n):
    result = 'YES'
    na = 100
    np = 100
    nt = 100
    na1 = 0
    na2 = 0
    na3 = 0
    for i in n:
        if i not in ('A','P','T'):
            result = 'NO'
            break
        elif i == 'P':
            if np == 100:
                np = n.index(i)
            else:
                result = 'NO'
                break
        elif i == 'T':
            if nt == 100:
                nt = n.index(i)
            else:
                result = 'NO'
                break
        elif i == 'A':
            na = n.index(i)
            if np == 100:
                na1 += 1
            elif np != 100 and nt == 100:
                na2 += 1
            elif np != 100 and nt != 100:
                na3 += 1
    if na == 100 or np == 100 or nt == 100:
        result = 'NO'
    else:
        if na1 == 0 and na3 != 0 or na2 == 0:
            result = 'NO'
        elif na1 == na3:
            if na2 == 0:
                result = 'NO'
        else:
            if na3 != na1*na2:
                result = 'NO'
    return result

def main():
    n = int(input())
    for i in range(n):
        string = str(input())
        print(PAT(string))


if __name__ == '__main__':
    main()

