encadminpass="wqgrIHSEgH_GkXAnPCVM"

#leaked_password:
pass1="joooseeeephjoestarrr"
encpass1="ZZ[^ATSS]@X_[TAEWDJB"


#the function of decryption:
def xor(message, key):
    return ''.join([chr(ord(a)^ord(b)) for a,b in zip(message, key)] )
#here we xor the encrypted pass with the pass to get the key : a xor b = c ==> a xor c = b
key=xor(encpass1,pass1)

#now we have the key so we have just to xor the enc admin password with the key to get the flag
flag=xor(encadminpass,key)
print(flag)

#flag=GDSC{yes_xor_is_fun}
