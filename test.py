import os
import _aes
import qwq5
import random

p='./example/1.jpg'
q='./example/2.data'
_aes.encrypt(b'1234567890123456',p,q)
_aes.decrypt(b'1234567890123456',q,'./example/2.jpg')

n=8
m=4
key=os.urandom(32)
info=b'qwq'
uinfo=[os.urandom(n) for i in range(n)]
pth_l='./example/random.'
pth_r='.key'
print(key,info,uinfo)

qwq5.qwq5encode(m,n,key=key,info=info,uinfo=uinfo,pth_l=pth_l,pth_r=pth_r)

f=set()
while len(f)<m:
    f.add(random.randint(0,n-1))
f=list(f)
random.shuffle(f)
print(f)
f=[pth_l+str(i)+pth_r for i in f]

a=qwq5.qwq5decode(f)
print(a)

n=7
m=5
pth_l=p+'.'
q='./example/3.data'
qwq5.qwq5AESencrypt(m,n,p,q)

f=set()
while len(f)<m:
    f.add(random.randint(0,n-1))
f=list(f)
random.shuffle(f)
print(f)
f=[pth_l+str(i)+pth_r for i in f]

qwq5.qwq5AESdecrypt(f,q,'./example/3.jpg')

'''
b'\x19\x8ctT\xf12{\xaf\x95\xc9\x82\x04\xbc\x87\xaa)\xf4\xa7mr]\xa0\xc7\xaa\xa2\x95\xad\xeb\xb1\x89\xcc\xc0' b'qwq' [b'!\xd6\xf5\xba\xafH@\xee', b'w\tB\xe4g\xf9\xc0r', b'\x07O\x1e\xf3]\x16\x8dN', b'\x0e<\r\xd9\x1b\xbc\xb9/', b'%qq\xcc\x12\xfc\x1f8', b"#\x0c'\xf2$_\xdaR", b'5e\x97\xdf~\xe4z\xaa', b'\x1fL\x15\x18k\xd9=\xee']
[0, 2, 7, 6]
(b'\x19\x8ctT\xf12{\xaf\x95\xc9\x82\x04\xbc\x87\xaa)\xf4\xa7mr]\xa0\xc7\xaa\xa2\x95\xad\xeb\xb1\x89\xcc\xc0', b'qwq', [b'!\xd6\xf5\xba\xafH@\xee', b'\x07O\x1e\xf3]\x16\x8dN', b'5e\x97\xdf~\xe4z\xaa', b'\x1fL\x15\x18k\xd9=\xee'])
[6, 0, 3, 5, 2]
'''