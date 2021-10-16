children = ["arbuzov_2000", "petrov_1998", "kotickov_2003"]


def by_year(name):
    return name.split('_')[-1]


s_children = sorted(children, key=by_year)
print(s_children)


def thirds(first, last):
    list = []
    for number in range(first, last + 1):
        if number % 3 == 0:
            list.append(number)
    return list


print(thirds(3, 30))

dict1 = {1: 1, 2: 3}

print(dir(dict1))
