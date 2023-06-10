
# 97 - 122 lowercase letters
# 65 - 90 Caps letters

def decoding_text(stringToShift, key):
  
   i = 0
   newletter = ""
   while i < len(stringToShift):
     
      letterUnicode = ord(stringToShift[i])
     
      if (letterUnicode > 122 or letterUnicode < 97):
         letterUnicode = letterUnicode
         
      else:
         letterUnicode += key
         if (letterUnicode > 122):
            letterUnicode = letterUnicode - 26

      newletter += chr(letterUnicode)
      i+= 1   
   return newletter


def coding_text(stringToshift, key):

   i=0
   newletter = ""

   while i < len(stringToshift):
      unicode= ord(stringToshift[i])
      if unicode > 122 or unicode < 97:
         unicode= unicode


      else:
         unicode-=key
         if unicode < 97:
            unicode= unicode+26
      newletter += chr(unicode)
      i+=1
   return newletter

print("would you like to code a text or decode a text today? ")
print(" ")
user_input = input("code/decode: ")
print(" ")

if user_input == "code":
   key= int(input("(key must be between 1 and 26 inclusive) Type Key : "))
   text= input("Message to encrypt: ")
   print(coding_text(text, key))
elif user_input == "decode":
   key= int(input("(key must be between 1 and 26 inclusive) Type Key : "))
   text= input("Message to decrypt: ")
   print(decoding_text(text, key))

# text='vhfinmxkl'
# i=0
# while i<26:
#    print(decoding_text(text, i))
#    i+=1
