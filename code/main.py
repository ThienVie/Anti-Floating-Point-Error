a = 0.1
b = 25884576894.0

def controll(object):
    if isinstance(object, float):
        return True

c = controll(a)
print(c)
c = controll(b)
print(c)