import struct

s = 'café'
len(s)   
# convert it to bytecode 
b = s.encode('utf8')  
print(f"s's len is {len(s)}, s's bytecode is :{b}")
# convert is to character 
decode_s = b.decode()
print(f"this bytecode is encoded  {decode_s} ")

# this is an immutable type 
immutable_s = bytes("cafe", encoding = 'utf_8')
print(f"the type of slice is : {type(immutable_s[:1])}" )

# this is a mutable type 
mutable_s = bytearray("cafe", encoding = 'utf_8')
print(f"the type of slice is : {type(mutable_s[:1])}")


# this is struct of python 
format_string = "if"
struct_string = struct.pack(format_string, 4, 3.14)
print(struct_string)
date_unpack = struct.unpack(format_string, struct_string)
# after unpack, will print a Tuple
print(date_unpack)