def convert(x, base):
    # alphabet = '0123456789ABCDEF'
    res = ''
    while x > 0:
        res += str(x % base)
        x //= base
    return res[::-1]


def to10(x, base):
    res = 0
    for i in range(len(x)):
        res += int(x[-1 - i]) * (base ** i)
    return res


def reshu_ege_easy():
    x = 216 ** 6 + 216 ** 4 + 36 ** 6 - 6 ** 14 - 24
    res = convert(x, 6)
    print(res)
    print(len(set(res)))


def reshu_ege_easy_2():
    x = 8 ** 7 + 4 ** 5 + 2 ** 10 - 32
    print(bin(x)[2:].count('1'))


# reshu_ege_easy_2()

def reshu_ege_2302():
    for base in range(2, 10):
        if convert(18, base) == '30':
            print(base)
            return


# reshu_ege_2302()


def reshu_ege_2309():
    for x in range(6, 50):
        for y in range(6, 50):
            if to10('225', x) == to10('405', y):
                print(x, y)
                return


reshu_ege_2309()
