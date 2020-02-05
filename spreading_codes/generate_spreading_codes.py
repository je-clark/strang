import pickle

def flip_bits(matrix):
    xirtam = []
    for row in matrix:
        xirtam.append(tuple(bit*-1 for bit in row))
    
    return tuple(xirtam)

def walsh_n_plus_1(walsh_n):
    walsh_reverse = flip_bits(walsh_n)
    walsh = []
    for row in walsh_n:
        walsh.append(row + row)

    for row, wor in zip(walsh_n, walsh_reverse):
        walsh.append(row + wor)
    
    return tuple(walsh)

def save_walsh_code(walsh_n, order):
    with open(f'walsh_{order}.pkl', 'wb') as f:
        pickle.dump(walsh_n, f)

if __name__ == "__main__":
    walsh_prime = ((1,1),(1,-1))
    walsh_2 = walsh_n_plus_1(walsh_prime)
    walsh_3 = walsh_n_plus_1(walsh_2)
    walsh_4 = walsh_n_plus_1(walsh_3)
    walsh_5 = walsh_n_plus_1(walsh_4)
    walsh_6 = walsh_n_plus_1(walsh_5)
    walsh_7 = walsh_n_plus_1(walsh_6)
    walsh_8 = walsh_n_plus_1(walsh_7)
    walsh_9 = walsh_n_plus_1(walsh_8)
    walsh_10 = walsh_n_plus_1(walsh_9)

    save_walsh_code(walsh_3, 3)
    save_walsh_code(walsh_4, 4)
    save_walsh_code(walsh_5, 5)
    save_walsh_code(walsh_6, 6)
    save_walsh_code(walsh_7, 7)
    save_walsh_code(walsh_8, 8)
    save_walsh_code(walsh_9, 9)
    save_walsh_code(walsh_10, 10)
