str = 'hh3[a2[cd]]'

def ToString(st):
    vec1 = []
    vec2 = []
    res = ""
    tmp = ""
    num = 0
    for el in range(len(st)):
        if st[el] not in "0123456789" and el != '[' and el != ']' and len(vec1) == 0:
           res += st[el]
        if st[el] in "0123456789":
            num += int(st[el])
            if st[el + 1] in "0123456789":
                num *= 10
            else:
                vec1.append(num)
                num = 0
        if st[el] == '[':
            continue
        if st[el] not in "01234567890" and st[el] != '[' and st[el] != ']':
            tmp += st[el]
            if st[el + 1] in "01234567890" or st[el + 1] == '[' or st[el + 1] == ']':
                vec2.append(tmp)
                tmp = ''
        if st[el] == ']':
            tmp = vec1[len(vec1) - 1] * vec2[len(vec2) - 1]
            vec1.pop()
            vec2.pop()
            if len(vec2) == 0 and el != len(st) - 1:
                continue
            elif len(vec2) != 0:
                vec2[len(vec2) - 1] = vec2[len(vec2) - 1] + tmp
        if len(vec1) == 0:
            res += tmp
        if el == len(st) - 1:
            return res


print(ToString(str))


def ToString1(str):
    num = ''
    nums = []
    values = []
    res = ''
    ind = 0
    for el in range(len(str)):
        if str[el] not in "01234567890" and el != '[' and el != ']':
            res += str[el]
        if str[el] in "01234567890":
            if str[el + 1] in "01234567890":
                num += str[el]
            else:
                nums += int(num)
                num = ''



