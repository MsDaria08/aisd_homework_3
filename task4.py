data = [197, 130, 1]

def utf8(data):
    value = []
    for el in range(len(data)):
        binary = ''
        while data[el] > 0:
            remainder = data[el] % 2
            binary = str(remainder) + binary
            data[el] = data[el] // 2
        value.append(int(binary))
    for el in value:
        el = el % 100000000
    for i in data:
        s = str(data[i])
        if len(s) == 1 and value[i] / 10**7 == 0:
            continue
        if len(s) == 2 and value[i] / 10**5 == 110:
        if len(s) == 3 and value[i] / 10**7 == 0:
        if len(s) == 4 and value[i] / 10**7 == 0:

utf8(data)