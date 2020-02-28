def main():
    list = [int(x) for x in input().split()]
    n = list[0]
    list[0] = 0
    count = 0
    for i in range(1,n+1):
        if list[i] > list[i-1]:
            count = count + (list[i]-list[i-1])*6 + 5
        elif list[i] == list[i-1]:
            count += 5
        else:
            count = count + (list[i-1]-list[i])*4 + 5
    print (count)
if __name__ == '__main__':
    main()