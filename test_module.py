import module

def test_function():
    try:
        f=Function()
        return True
    except NameError:
        raise AssertionError("No class with this name")
    except:
        raise AssertionError("Other error")
