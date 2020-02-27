def main():
    case = input()
    num = sum([int(x) for x in case])
    sums = str(num)
    output = []
    digits = ['zero','one','two','three','four','five',
            'six','seven','eight','nine']
    for i in sums :
        output.append(digits[int(i)])
    print(' '.join(output))
if __name__ == '__main__':
    main()