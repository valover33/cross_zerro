def main():
    x = [1, 3, 5, 0, -1, 3, -2]
    for i, n in enumerate(x):
        if n < 0:
            x.pop(i)
    print(x)

    a = 0
    y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
    for i in y:
        for j in i:
            if j < 0:
               a = a + 1
    print(a)

    z = -4
    if z < -5:
        print ("veri low")
    elif z in range(-5, 0):
        print("low")
    elif z == 0:
        print("neutral")
    else:
        print("hi")

    x = [1, 3, 5, 0, -1, 3, -2]
    x_ = []
    x_ = [item for item in x if item >= 0]                              # Генератор словаря
    print(x_)

    odd_ = (item for item in range(1, 100) if item % 2 != 0)            # Выражение генератор
    for odd in odd_:
        print(odd, end=' ')
    print()

    kubes = {item: item * item * item for item in range(11, 16)}        # Генератор словаря
    print(kubes)


if __name__ == '__main__':
    main()
