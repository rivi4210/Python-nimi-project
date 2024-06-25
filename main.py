import input
import command


def select_tail(map, x, y):
    x -= 1
    y -= 1

    if x % 5 == 0:
        x = x // 5
    else:
        x = x // 5 + 1
    return x


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(0)
    print(select_tail([12],13,5))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
