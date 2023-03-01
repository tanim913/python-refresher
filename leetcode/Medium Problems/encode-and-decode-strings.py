strs = ["one","two","three","four"]
encode = ""
'''
    encoding the string by adding the length and a special character before each string
    so that , even if the main string contains any of that special characters, it would be okay while decoding
    because the after the length of each string there would be a special character which isn't the part of main 
    string
'''
for s in strs:
    encode += str(len(s)) + "#" + s
print(encode)
'''
    decoding algorithm:
    1. extract the length of each string: to extraxt the len of each string , we found out the index of the special character.
                                          To find that index we increased the current index by 1 until we got that index of that 
                                          character. and then we took that len digit by taking the character from current index to
                                          the special character index (not including special char index) and converting into an 
                                          integer.

    2. appendind decoded list: we appended the character beginning from the index that comes exactly after the special char index.
                               to the index that can be calculated after adding the len of each individual string(not included)

    3. reassinging current index value : reassiging the current index value to the first point of next encoded string
                                         ("size"+"#"+"string_size"). and keep reassigning as long as it is inside the bound of the
                                         len of encoded string
            
'''
decode, i = [], 0
while i < len(encode):
  j = i
  while encode[j] != "#": 
      j += 1 #increasing index by 1 as long as we don't we the speacial character
  length = int(encode[i:j])
  decode.append(encode[j + 1 : j + 1 + length])
  i = j + 1 + length

print(decode)

