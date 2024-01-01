def controll(object):
    try:
         object = float(object)
    except Exception as e:
        print(f"{e}")
        quit()

def number(object: float):
    controll(object)
    print(object)
    object = list(str(object))
    print(object)