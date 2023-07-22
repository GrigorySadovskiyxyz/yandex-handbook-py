def func():
    x = None
    try:
        x = int('Hello, world!')
    except ValueError as ve:
        print("ValueError")
    except TypeError as te:
        print("TypeError")
    except SystemError as se:
        print("SystemError")
    else:
        print("No Exceptions")

