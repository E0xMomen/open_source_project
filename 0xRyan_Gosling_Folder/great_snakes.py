# Ascii
#
# ascii_array = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]  # Example ASCII values

# # Convert ASCII values to characters
# char_array = [chr(ascii_value) for ascii_value in ascii_array]

# # Join characters into a string
# result_string = ''.join(char_array)

# # Print the resulting string
# print(result_string)  # Output:
#####################################################################

#Hexa 

# hexa_text1="63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
# flag= bytes.fromhex(hexa_text1)
# print("the flag is: ", flag)
#####################################################################

#Hexa + base64

# import base64
# hexa_text="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
# text= bytes.fromhex(hexa_text)
# base64text= base64.b64encode(text)
# print("the flag is: ", base64text)
#####################################################################

#from digits to chars

# from Crypto.Util.number import *
# encr_txt= 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# flag = long_to_bytes(encr_txt)
# print("the flag is ", flag)
#####################################################################

#XOR Label XOR 13
# label = "label"
# key = 13
# result = ''.join(chr(ord(char) ^ key) for char in label)
# print("Result after XOR:", result)

# for i in label:
    # print(chr(ord(i)^13))

#####################################################################

#OXRpuzzel 1

# from Crypto.Util.number import *

# KEY1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
# K1_XOR_K2_hex = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
# K2_XOR_K3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
# FLAG_XOR_K1_XOR_K2_XOR_K3_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"


# KEY1 = int(KEY1_hex, 16)
# K1_XOR_K2 = int(K1_XOR_K2_hex, 16)
# K2_XOR_K3 = int(K2_XOR_K3_hex, 16)
# FLAG_XOR_K1_XOR_K2_XOR_K3 = int(FLAG_XOR_K1_XOR_K2_XOR_K3_hex, 16)


# KEY2 = KEY1 ^ K1_XOR_K2


# KEY3 = KEY2 ^ K2_XOR_K3


# FLAG = KEY1 ^ KEY2 ^ KEY3 ^ FLAG_XOR_K1_XOR_K2_XOR_K3

# print(long_to_bytes(FLAG))



#other solution 

# from pwn import xor
# k1=bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
# k2_3=bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
# flag=bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
# print(xor(k1,k2_3,flag))  

#####################################################################

#OXRpuzzel_2

# from pwn import xor
# a="73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
# for i in range(0,99):
#     print (xor(i, bytes.fromhex(a)))

#####################################################################

#OXRpuzzel_3

# from pwn import xor
# flag = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
# key = xor(flag, 'crypto{')
# print ("     ", key)#from here i gets the key myXORkey and i will use it 
# final_flag = xor(flag, 'myXORkey') 
# print("     ", final_flag)

########################################################################

text = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
flag = bytes.fromhex(text)
print("       \n     ",flag)





