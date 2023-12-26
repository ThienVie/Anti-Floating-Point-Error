def fl(object: float):
    try:
        if not isinstance(object,float):
            quit()
        object = list(str(object))
        print(object)
    except:
        print(f"['{object}'] is not a foat.")
        quit()