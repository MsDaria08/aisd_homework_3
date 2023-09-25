data = [197, 130, 1]

def toBin(value):
    res = ''
    while value > 0:
        tmp = value % 2
        res = str(tmp) + res
        value = value // 2
    return res

def utf8(data):
    res = [toBin(i).zfill(8) for i in data]
    i = 0
    while i + 1 <= len(data):
        if res[i][0] == '0':
            i += 1
        elif i + 1 <= len(data) - 1 and res[i].startswith('0'):
            i += 1
        elif i + 2 <= len(data) - 1 and res[i].startswith('110') and res[i + 1].startswith('10'):
            i += 2
        elif i + 3 <= len(data) - 1 and res[i].startswith('1110') and res[i + 1].startswith('10') and res[i + 2].startswith('10'):
            i += 3
        elif i + 4 <= len(data) - 1 and res[i].startswith('11110') and res[i + 1].startswith('10') and res[i + 2].startswith('10') and res[i + 3].startswith('10'):
            i += 4
        else:
            return 0
    return 1

print(utf8(data))
