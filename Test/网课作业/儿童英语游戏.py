from __future__ import print_function
def Pig_Latin(a):
    a = a.lower()
    b = a[0]
    if b in 'aeiou':
        a = a + 'hay'
        return a
    elif b == 'q' and a[1] == 'u':
        a = a[2:] + a[:2] + 'ay'
        return a
    else:
        for c in a[1:]:
            if c in 'aeiouy':
                n = a.find(c)
                a = a[n:] + a[:n] + 'ay'
                return a
        else:
            a = a + 'ay'
            return a
a = raw_input()
b = a.split()
d = []
for c in b:
    d.append(Pig_Latin(c))
strnew = ' '.join(d)
print (strnew)