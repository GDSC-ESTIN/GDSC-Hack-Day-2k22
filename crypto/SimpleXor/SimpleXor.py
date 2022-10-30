encrypted_admin_password="wqgrIHSEgH_GkXAnPCVM"

#leaked_password:
plain_text_user_password="joooseeeephjoestarrr"
encrypted_user_password="ZZ[^ATSS]@X_[TAEWDJB"


#the function of decryption:
def xor(message, key):
    return ''.join([chr(ord(a)^ord(b)) for a,b in zip(message, key)] )
