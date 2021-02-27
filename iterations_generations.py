listik = [1, 2, 3]  # он хранится в памяти всегда
listik2 = [i * i for i in range(3)]  # читается только 1 раз


def gen():
    svoi_listik = range(3)
    for i in svoi_listik:
        yield i * i


def gen_without_yield(n):
    svoi_listik = []
    for i in range(n):
        svoi_listik.append(i * i)
    return svoi_listik


my_gen = gen()  # отсюда он сразу уйдет
my_gen_without_iterator = gen_without_yield(3)  # этот будет храниться в памяти всегда
for i in my_gen:
    print(i)

for i in my_gen_without_iterator:
    print(i)

for i in [i for i in range(10)]:
    print(i, end=', ')