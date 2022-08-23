import math

data_pizza1 = {'p': 35,
        'r': 30
}

data_pizza2 = {'p': 55,
        'r': 35
}


def my_func(pizza1, pizza2):

    area = math.pi * pizza1['r']**2
    area2 = math.pi * pizza2['r']**2
    print(area,area2)

    ratio1 = pizza1['p']/area
    ratio2 = pizza2['p']/area
    if ratio1 <= ratio2:
        return "hi"
    else:
        return "bye"    
    


ret = my_func(data_pizza1, data_pizza2)
print(ret)