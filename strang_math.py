from strang_helpers import identify_walsh_order, convert_string_to_integer, decode_strang

def add(strang1, strang2):
    length = max(len(strang1), len(strang2))
    order = identify_walsh_order(length)

    s1 = convert_string_to_integer(strang1, order = order)
    s2 = convert_string_to_integer(strang2, order= order)

    print(s1)
    print(s2)

    sum = tuple(map(lambda x, y : x+y, s1, s2))
    print(sum)

    return decode_strang(sum)

def subtract(strang1, strang2):
    length = max(len(strang1), len(strang2))
    order = identify_walsh_order(length)

    s1 = convert_string_to_integer(strang1, order = order)
    s2 = convert_string_to_integer(strang2, order= order)

    #print(s1)
    #print(s2)

    sum = tuple(map(lambda x, y : x-y, s1, s2))
    #print(sum)

    return decode_strang(sum)

def multiply(strang1, strang2):
    length = max(len(strang1), len(strang2))
    order = identify_walsh_order(length)

    s1 = convert_string_to_integer(strang1, order = order)
    s2 = convert_string_to_integer(strang2, order= order)

    #print(s1)
    #print(s2)

    product = tuple(map(lambda x, y : x*y, s1, s2))
    #print(sum)

    return decode_strang(product) 