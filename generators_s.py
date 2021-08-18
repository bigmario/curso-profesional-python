def my_gen():
    print("Hola 0")
    n=0
    yield n

    print("Hola 1")
    n=1
    yield n

    print("Hola 2")
    n=2
    yield n

    print("Hola 3")
    n=3
    yield n


a = my_gen()

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
