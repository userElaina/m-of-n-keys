import os
import base64
import hashlib
from Crypto.Cipher import AES

bs=AES.block_size
bs2=bs<<10

def encrypt(key:bytes,p1:str,p2:str=None):
    if p2 is None:
        p2=p1+'.aes'
    f1=open(p1,'rb')
    f2=open(p2,'wb')
    size=os.path.getsize(p1)
    name=os.path.basename(p1).encode('utf8')
    len_name=len(name)

    cipher=AES.new(key,AES.MODE_CBC)
    f2.write(cipher.iv)
    data=size.to_bytes(8,'little')+len_name.to_bytes(4,'little')+os.urandom(4)+name+os.urandom(bs-(len_name-1)%bs-1)
    f2.write(cipher.encrypt(data))
    f2.flush()

    while True:
        data=f1.read(bs2)
        if not data:
            break
        data+=os.urandom(bs-(len(data)-1)%bs-1)
        f2.write(cipher.encrypt(data))
        f2.flush()
    f1.close()
    return p2

def decrypt(key:bytes,p1:str,p2:str=None):
    f1=open(p1,'rb')
    size_f=os.path.getsize(p1)
    if size_f<16:
        raise EOFError('File is too small')

    iv=f1.read(bs)
    cipher=AES.new(key,AES.MODE_CBC,iv)

    data=f1.read(bs)
    data=cipher.decrypt(data)
    size=int.from_bytes(data[:8],'little')
    size_padded=size+bs-(size-1)%bs-1
    len_name=int.from_bytes(data[8:12],'little')
    len_name_padded=len_name+bs-(len_name-1)%bs-1
    if bs+len_name_padded+size_padded>size_f:
        raise EOFError('File is too small')
    
    data=f1.read(len_name_padded)
    data=cipher.decrypt(data)
    if os.path.isdir(p2):
        name=os.path.join(p2,data[:len_name].decode('utf8'))
    elif os.path.isdir(os.path.dirname(p2)):
        name=p2
    else:
        name=data[:len_name].decode('utf8')
    f2=open(name,'wb')

    while size>0:
        data=f1.read(bs2)
        if not data:
            break
        data=cipher.decrypt(data)
        f2.write(data[:size])
        f2.flush()
        size-=bs2
    f2.close()
    return

if __name__=='__main__':
    encrypt(b'1234567890123456','./example/p1.jpg','./example/p1.test')
    decrypt(b'1234567890123456','./example/p1.test','./example/p2.jpg')
