def main():
    s = []
    listD = ['A','B','C','D','E','F','G']
    D = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    h = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F',
         'G','H','I','J','K','L','M','N']
    list = [str(x) for x in
            'a b c d e f g h i j k l m n o p q r s t u v w x y z ' \
            'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()]
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            if s == [] and s1[i] in listD:
                s.append(D[listD.index(s1[i])])
            elif s != [] and s1[i] in h:
                H = h.index(s1[i])
                if H == 0:
                    s.append('00')
                elif H < 10:
                    s.append('0'+str(H))
                else:
                    s.append(str(H))
                break
    for i in range(len(s3)):
        if s3[i] == s4[i] and s3[i] in list:
            if i == 0:
                s.append('00')
            elif i < 10:
                s.append('0' + str(i))
            else:
                s.append(str(i))
            break
    print('{} {}:{}'.format(s[0],s[1],s[2]))

if __name__ == '__main__':
    main()