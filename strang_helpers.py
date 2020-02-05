import pickle

class TooStrungOutError(Exception):
    def __init__(self, expression):
        self.expression = expression
        self.message = "Strang way too strung out. Spreading codes spread too thin."


def identify_walsh_order(strang_lenth):
    if strang_lenth <= 8:
        walsh_order = 3
    elif strang_lenth <= 16:
        walsh_order = 4
    elif strang_lenth <= 32:
        walsh_order = 5
    elif strang_lenth <= 64:
        walsh_order = 6
    elif strang_lenth <= 128:
        walsh_order = 7
    elif strang_lenth <= 256:
        walsh_order = 8
    elif strang_lenth <= 512:
        walsh_order = 9
    elif strang_lenth <= 1024:
        walsh_order = 10
    else:
        raise TooStrungOutError

    return walsh_order

def extract_char_bits(strang):
    char_bits = []
    for character in strang:
        c = ord(character)
        char_bits.append(
            (
                (c & 128) >> 7,
                (c & 64) >> 6,
                (c & 32) >> 5,
                (c & 16) >> 4,
                (c & 8) >> 3,
                (c & 4) >> 2,
                (c & 2) >> 1,
                (c & 1)
            )
        )
    return tuple(char_bits)

def encode_strang(bitwise_strang, spreading_code):
    encoding = [0,]*(len(spreading_code[0])*8)
    for character, code in zip(bitwise_strang, spreading_code):
        encoded_char = ()
        for bit in character:
            adjusted_char = 2*bit - 1
            encoded_bit = tuple(map(lambda code_element : adjusted_char*code_element, code))
            encoded_char = encoded_char + encoded_bit
        for i in range(0,len(encoding)):
            encoding[i] = encoding[i] + encoded_char[i]

    return tuple(encoding)



# While this isn't convoluted in a mathematical sense,
# it is absolutely convoluted in an intellectual sense.
def convert_string_to_integer(strang, order = None):
    if not order:
        order = identify_walsh_order(len(strang))
    with open(f'.//spreading_codes//walsh_{order}.pkl', 'rb') as f:
        spreading_code = pickle.load(f)

    bitwise_strang = extract_char_bits(strang)
    return encode_strang(bitwise_strang, spreading_code)
    
print(convert_string_to_integer('poles'))