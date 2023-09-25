str = 'hh3[a2[cd]]'
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