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

        #вынести в функцию
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

def ch(st):
    index = 0
    while 1:
        if st[index] not in "0123456789":
            index += 1
        else:
            break
    return(st[:index], st[index:])

def indexZak(st):
    ind = 0
    cnt = 1
    while cnt > 0:
        ind += 1
        if st[ind] == '[':
            cnt += 1
        if st[ind] == ']':
            cnt -= 1
    return ind
def toString(st):
    if '[' not in st:
        return st
    st = st.replace('[', ' ', 1)
    index = indexZak(st)
    st = st[:index] + ' ' + st[index + 1:]
    tmp = st.split(' ')
    return ch(tmp[0])[0] + int(ch(tmp[0])[1]) * toString(tmp[1]) + toString(tmp[2])

print(toString(str))