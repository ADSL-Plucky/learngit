import string
import keyword
def isIdentifier(s):
    if s not in keyword.kwlist:
        if s[0] in string.ascii_letters or s[0] == '_':
            for i in s[1:]:
                if i not in (string.ascii_letters + string.digits+'_'):
                    return False
            return True
    return False
s = []
for i in range(3):
    a = raw_input()
    a = a.rstrip()
    s.append(a)
for b in s:
    if isIdentifier(b):
        print 'True'
    else:
        print 'False'