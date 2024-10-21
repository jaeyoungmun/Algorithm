
import sys
input = sys.stdin.readline
aeiou = ['a','e','i','o','u']
while(1):
    test = input()
    test = test.strip()
    first = False
    second = True
    third = True
    if test == 'end': # 종료
        break
    
    for i in range(len(test)):
        if test[i] in aeiou:
            first = True
        if i == 0:
            continue
        elif i == 1:
            if test[i-1] == test[i] and test[i] not in ['e','o']:
                second = False
                break
            continue
        # i가 2이상일때만 여길 지남
        if test[i-1] == test[i] and test[i] not in ['e','o']:
            second = False
            break

        if (test[i-2] not in aeiou) and (test[i-1] not in aeiou) and (test[i] not in aeiou):
            third = False
            break
        if (test[i-2] in aeiou) and (test[i-1] in aeiou) and (test[i] in aeiou):
            third = False
            break
    
    if (first == False) | (second == False) | (third == False):
        print("<"+test+"> is not acceptable.")
    else:
        print("<"+test+"> is acceptable.")
        