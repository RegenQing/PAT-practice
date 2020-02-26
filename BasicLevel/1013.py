def prime(p,pri):
    for i in pri:
        if p % i == 0:
            return False
        if i > int(p**0.5)+1:
            return True
    return True

def main():
    pri = [2]
    p = 3
    [m,n] = [int(x) for x in input().split()]
    while len(pri) < n:
        if prime(p,pri):
            pri.append(p)
        p += 2
    for i in range(m-1,n,10):
        print(' '.join(list(map(str,pri[i:i+10]))))

if __name__ == '__main__':
    main()
