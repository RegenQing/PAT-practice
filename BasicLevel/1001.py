def main():
    n = int(input())
    count = 0
    while n != 1:
        if n%2 == 0:
            n /= 2
            count += 1
        else:
            n = 1.5*n+0.5
            count += 1
    print(count)
if __name__ == '__main__':
    main()