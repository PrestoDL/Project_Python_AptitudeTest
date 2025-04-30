'''
class sec:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def input(self, x):
        return self.a * (x ** 2) + self.b * x + self.c

one = sec(2, -5, 3)
print(one.input(4))

s11 = -100; s12 = -one.b / (2 * one.a);
s21 = -one.b / (2 * one.a); s22 = 100

while(True):
    if one.input((s11 + s12) / 2) * one.input(s11) < 0:
        s12 = (s11 + s12) / 2
        print((s11 + s12) / 2)
        
    elif one.input((s11 + s12) / 2) * one.input(s12) < 0:
        s11 = (s11 + s12) / 2
        print((s11 + s12) / 2)
        
    else:
        print((s11 + s12) / 2)
        break
'''

'''
lim = range(1, 31)

tri = [(a, b, c) for a in lim for b in lim for c in lim if (c**2 == a**2 + b**2 and a < b)]
print(tri)
'''

'''
class sc:
    def __init__(self, num, name, mid, fin):
        self.num = num
        self.name = name
        self.aver = str((int(mid) + int(fin)) / 2)

info = input('입력').split()
your = sc(info[0], info[1], info[2], info[3])


a = open('score.txt', 'a')
a.write(your.num + ' ' + your.name + ' ' + your.aver + '\n')
a.close()

b = open('score.txt', 'r')
print(b.read())
'''

class stud:
    
    def __init__(self, num, name, sc):
        self.__num = num
        self.__name = name
        self.__sc = sc






        
