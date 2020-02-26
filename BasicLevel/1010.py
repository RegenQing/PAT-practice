def main():
    n = [int(x) for x in input().split()]
    result = []
    for i in range(len(n) // 2):
        a_i = n[2*i]
        n_i = n[2*i+1]
        if a_i == 0:
            result.append('0 0')
        elif n_i == 0:
            continue
        elif n_i == 1:
            result.append(str(a_i))
            result.append('0')
        else:
            result.append(str(a_i*n_i))
            result.append(str(n_i-1))
    if len(result) == 0:
        print('0 0')
    else:
        print(' '.join(result))
if __name__ == '__main__':
    main()