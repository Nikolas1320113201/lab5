def add_ten(x):
    if type(x) == str:
        x_num = int(x)
        result_num = x_num + 10
        return str(result_num)
    elif x is None:
        return None
    else:
        return x + 10

