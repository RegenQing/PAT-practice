def compare(target):
    if target[0]+target[1] > target[2]:
        result = 1
    else:
        result = 0
    return result

def main():
    n = int(input())
    for i in range(n):
        num = [int(x) for x in input().split()]
        if compare(num) == 0:
            print('Case #{}: false'.format(i+1))
        else:
            print('Case #{}: true'.format(i+1))

if __name__ == '__main__':
    main()
