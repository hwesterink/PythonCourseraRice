'''
Practice Activity 2.2: Binary Representations for Numbers
'''
def make_binary(length):
    """
    This function creates a list of all binaries with the given length
    """
    if length == 0:
        return [""]
    else:
        shorter_binaries = make_binary(length-1)
        binaries = []
        for binary in shorter_binaries:
            binaries.append("0" + binary)
        for binary in shorter_binaries:
            binaries.append("1" + binary)
        return binaries

def bin_to_dec(bin_num):
    """
    This function computes a decimal number from a binary number
    represented in a string
    """
    length = len(bin_num)
    if length == 0:
        return 0
    else:
        return ( int(bin_num[0]) * 2 ** (length-1)) + bin_to_dec(bin_num[1:]) 

def make_gray(length):
    """
    This function creates a list of all gray binaries with the given length
    """
    if length == 0:
        return [""]
    else:
        shorter_binaries = make_gray(length-1)
        binaries = []
        for binary in shorter_binaries:
            binaries.append("0" + binary)
        shorter_binaries.reverse()
        for binary in shorter_binaries:
            binaries.append("1" + binary)
        return binaries

def gray_to_bin(gray_code):
    """
    This function converts a gray coded binary into a binary number
    """
    if len(gray_code) <= 1:
        return gray_code
    else:
        significant_bits = gray_to_bin(gray_code[:-1])
        last_bit = (int(gray_code[-1]) + int(significant_bits[-1])) % 2
        return significant_bits + str(last_bit)

    
# Testing the functions created for this assignment
print "1. Tests for make_binary"
print "Expected: ['']; Computed:", make_binary(0)
print "Expected: ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', \
'1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']\nComputed:", make_binary(4)
print "Expected: ['1111110101', '1111110110', '1111110111', '1111111000', '1111111001', \
'1111111010', '1111111011', '1111111100', '1111111101', '1111111110', '1111111111']\
\nComputed:", make_binary(10)[1013:1024]
print
print "2. Tests for bin_to_dec"
binaries = make_binary(10)
print "Expected: 0; Computed:", bin_to_dec(binaries[0])
print "Expected: 10; Computed:", bin_to_dec(binaries[10])
print "Expected: 53; Computed:", bin_to_dec(binaries[53])
print "Expected: 1023; Computed:", bin_to_dec(binaries[1023])
print
print "3. Tests for make_gray"
print "Expected: ['']; Computed:", make_gray(0)
print "Expected: ['000', '001', '011', '010', '110', '111', '101', '100']\nComputed:", make_gray(3)
print "Expected: ['00000', '00001', '00011', '00010', '00110', '00111', '00101', '00100', \
'01100', '01101', '01111', '01110', '01010', '01011', '01001', '01000', '11000', '11001', \
'11011', '11010', '11110', '11111', '11101', '11100', '10100', '10101', '10111', '10110', \
'10010', '10011', '10001', '10000']\nComputed:", make_gray(5)
print
print "4. Tests for gray_to_bin"
grays = make_gray(10)
print "Expected: 0; Computed:", bin_to_dec(gray_to_bin(grays[0]))
print "Expected: 10; Computed:", bin_to_dec(gray_to_bin(grays[10]))
print "Expected: 53; Computed:", bin_to_dec(gray_to_bin(grays[53]))
print "Expected: 1023; Computed:", bin_to_dec(gray_to_bin(grays[1023]))
