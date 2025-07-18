import array

# Signed 8-bit integer array ('b' = signed char)
signed_array = array.array('b', [-128, -1, 0, 1, 127])

# Unsigned 8-bit integer array ('B' = unsigned char)
unsigned_array = array.array('B', [0, 1, 255])

print("Signed array:", signed_array)
print("Unsigned array:", unsigned_array)

# Demonstrating overflow manually (array module doesn't wrap automatically)
try:
    # This will raise an OverflowError
    signed_array.append(128)
except OverflowError as e:
    print("Signed overflow error:", e)

try:
    # This will raise an OverflowError
    unsigned_array.append(256)
except OverflowError as e:
    print("Unsigned overflow error:", e)
