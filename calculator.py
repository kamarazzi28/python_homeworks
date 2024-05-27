def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y 
def multiplication(x, y):
    return x * y
def division(x, y):
    if y == 0:
        raise ValueError('This operation is not supported for given input parameters')
    return x / y
def modulo(x, y):
    if y <= 0 or x < y:
        raise ValueError('This operation is not supported for given input parameters')
    return x % y
def secondPower(x):
    return x ** 2
def power(x, y):
    if y < 0: 
        raise ValueError('This operation is not supported for given input parameters')
    return float(x ** y)
def secondRadix(x):
    if x <= 0:
        raise ValueError('This operation is not supported for given input parameters')
    return x ** 0.5
def magic(x, y, z, k):
    l = x + k
    m = y + z
    if m == 0:
        raise ValueError('This operation is not supported for given input parameters')
    return ((l/m) + 1)
def control(a, x, y, z, k):
    if a == 'ADDITION':
        return addition(x, y)
    elif a == 'SUBTRACTION':
        return subtraction(x, y)
    elif a == 'MULTIPLICATION':
        return multiplication(x, y)
    elif a == 'DIVISION':
        return division(x, y)
    elif a == 'MOD':
        return modulo(x, y)
    elif a == 'SECONDPOWER':
        return secondPower(x)
    elif a == 'POWER':
        return power(x, y)
    elif a == 'SECONDRADIX':
        return secondRadix(x)
    elif a == 'MAGIC':
        return magic(x, y, z, k)
    else:
        raise ValueError('This operation is not supported for given input parameters')  