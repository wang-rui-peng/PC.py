#多个装饰器的执行顺序
def wrapper_out1(func):
    print('--out11--')

    def inner1(*args, **kwargs):
        print("--in11  ")
        ret = func(*args, **kwargs)
        print("--in12  ")
        return ret

    print("--out12--")
    return inner1


def wrapper_out2(func):
    print('--out21--')

    def inner2(*args, **kwargs):
        print("--in21  ")
        ret = func(*args, **kwargs)
        print("--in22  ")
        return ret

    print("--out22--")
    return inner2


@wrapper_out2
@wrapper_out1
def test():
    print("--test--")
    return 1 * 2


if __name__ == '__main__':
    test()