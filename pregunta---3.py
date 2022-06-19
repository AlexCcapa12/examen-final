import time

def mesureTime(function):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = function(*args, **kwargs)

        total = time.time() - start
        print("el tiempo de demora de ejecución fue de: {}".format(total))

        return result

    return wrapper


@mesureTime
def div(a, b):
    time.sleep(1)
    division = a/b
    return division

"ejemplo 1"
print("division del primer ejemplo: ", div(1600, 800))

"ejemplo 2"
print("division del segundo ejemplo: ", div(500000000000, 25))




