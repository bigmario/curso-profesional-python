def make_division_by(n):
    def divide(x):
        assert ((type(x) == int or type(x) == float) and 
                (type(n) == int or type(n) == float), 'No puedes dividir cadenas de caracteres')
        assert n != 0,  'no puedes dividir entre 0'
        return x // n
    return divide


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))

if __name__ == '__main__':
    run()