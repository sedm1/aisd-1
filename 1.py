n = 5
K = 0.3
def custom_hash(input_string):
    hash_value = 0

    for i in range(n):
        for char in input_string:
            hash_value = int(hash_value * 31 * K + ord(char))
        hash_value = hash_value % (2**32)

    hash_str = ""
    while hash_value > 0:
        hash_value, remainder = divmod(hash_value, 36)
        if remainder < 10:
            hash_str = chr(remainder + ord('0')) + hash_str
        else:
            hash_str = chr(remainder + ord('A') - 10) + hash_str

    return hash_value

input_string = "example"
hashed_value = custom_hash(input_string)
print(hashed_value)