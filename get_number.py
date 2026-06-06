def get_num(a,b):
    while a >= (10 ** b):
        a //= 10
    return a % 10
def get_num_easy(a,b):
    return str(a)[b-1]