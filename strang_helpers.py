import pickle, math, functools

# Important limitation:
# This is highly dependent on maintaining
# strings in the ASCII space only.
# There is a hardcoded 8-bit per character
# assumption. Any Unicode-based character
# representation will break things in ways
# that will either be very silly or just kinda
# boring.

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

def get_spreading_code(order):
    with open(f'.//spreading_codes//walsh_{order}.pkl', 'rb') as f:
        spreading_code = pickle.load(f)
    
    return spreading_code

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


def decode_strang(bitwise_strang):

    bit_length = int(len(bitwise_strang)/8)
    #print(bit_length)
    order = int(math.log2(bit_length))
    spreading_code = get_spreading_code(order)

    split_strang = tuple(bitwise_strang[x:x+bit_length] for x in range(0, int(len(bitwise_strang)), bit_length))

    strang = []
    for orthogonal_code in spreading_code:
        char = int(0) # We need to start with the integer representation
        for bit, offset in zip(split_strang, range(7, -1, -1)):
            hidden_value = functools.reduce(
                lambda x, y : x+y,
                map(
                    lambda x, y : x*y,
                    orthogonal_code, bit
                )
            )
            if (hidden_value > 0):
                applied_bit = 1
            else:
                applied_bit = 0
            print(f'applying {applied_bit} at offset {offset}')
            char = char + (applied_bit << offset)
        print(char)
        strang.append(chr(char))

    return ''.join(filter(lambda x : x != '\x00', strang))



# While this isn't convoluted in a mathematical sense,
# it is absolutely convoluted in an intellectual sense.
def convert_string_to_integer(strang, order = None):
    # If you have multiple strings to process, use 
    # identify_walsh_order() on the max string length
    # and pass in that value
    if not order:
        order = identify_walsh_order(len(strang))
    if order > 10:
        raise TooStrungOutError
    spreading_code = get_spreading_code(order)

    bitwise_strang = extract_char_bits(strang)
    return encode_strang(bitwise_strang, spreading_code)