from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#encrypting
def encrypt(text,shift):
    enc_txt=''
    for i in text:
        if i in alphabet:
           a=alphabet.index(i)
           new=alphabet[a+shift]
           enc_txt+=new
        else:
            enc_txt+=i
    print(f'the encoded text is {enc_txt}')

def decrypt(text,shift):
    dec_txt=''
    for i in text:
        if i in alphabet:
          a=alphabet.index(i)
          new=alphabet[a-shift]
          dec_txt+=new
        else:
          dec_txt+=i
    print(f'the decoded text is {dec_txt}')
while True:
  direction = input("type 'encode' to encrypt and type 'decode' to decrypt:")
  text = input('enter your message:').lower()
  shift = int(input('enter the shift number:'))
  shift=shift%26
  if direction=='encode':
     encrypt(text,shift)
  if direction=='decode':
     decrypt(text,shift)
  ch=input("If you want to continue further type 'yes' else 'no' :")
  if ch.lower()=='yes':
      None
  elif ch.lower()=='no':
      break
      print('goodbye')
  else:
      print('please enter a valid answer')


#__________________________________________________________________________
'''
def ceaser(text,shift,direction):
    plain_txt=''
    for i in text:
        pos=alphabet.index(i)
        if direction=='decode':
            shift*=-1
        if direction=='encode':
            shift*=1
        plain_txt+=alphabet[pos+shift]
        print(f'Here is the {direction} result: {plain_txt}')
'''