def main():
    n = [int(x) for x in input().split()]
    list = [i for i in input().split()]
    print(' '.join(list[n[0]-n[1]:] + list[:n[0]-n[1]]))

if __name__ == '__main__':
    main()