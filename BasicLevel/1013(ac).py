def prime(num):
    flag = [1]*(num+1)
    flag[0] = flag[1] = 0
    result = []
    for i in range(2,num+1):
        if flag[i]:
            result.append(i)
            p = i
            while p*i <= num:
                flag[p*i] = 0
                p += 1
    return result

def main():
    [m,n] = [int(x) for x in input().split()]
    num = 105000
    result = prime(num)[:n]
    for i in range(m - 1, n, 10):
        print(' '.join(list(map(str, result[i:i + 10]))))

if __name__ == '__main__':
    main()