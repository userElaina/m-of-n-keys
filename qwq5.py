import os
import itertools
from scipy.special import comb
import _aes

def qwq5encode(m:int,n:int,key:bytes=os.urandom(32),info:bytes=None,uinfo:list=None,pth_l:str='',pth_r:str='.key')->None:
    m,n=min(m,n),max(m,n)
    try:
        if not isinstance(info,bytes):
            info=info.encode('utf8')
    except:
        info=b''
    try:
        uinfo=[i.encode('utf8') if isinstance(uinfo,str) else bytes(i) for i in uinfo]
        if len(uinfo)!=n:
            raise ValueError
    except:
        uinfo=[b'']*n

    len_key=len(key)
    key=int.from_bytes(key,'little')
    f=list()
    for j in range(n):
        _f=open(pth_l+str(j)+pth_r,'wb')
        _b=b''
        _b+=j.to_bytes(1,'little')
        _b+=n.to_bytes(1,'little')
        _b+=len_key.to_bytes(2,'little')
        _b+=len(info).to_bytes(2,'little')
        _b+=len(uinfo[j]).to_bytes(2,'little')
        _b+=info
        _b+=uinfo[j]
        _f.write(_b)
        _f.flush()
        f.append(_f)
    for i in itertools.combinations(range(n),m):
        _sum=key
        for j in range(m-1):
            _rd=os.urandom(len_key)
            _sum^=int.from_bytes(_rd,'little')
            f[i[j]].write(_rd)
            f[i[j]].flush()
        f[i[-1]].write(_sum.to_bytes(len_key,'little'))
        f[i[-1]].flush()
    for i in f:
        i.close()

# def get_n(n:int,l:list)->int:
#     h=-1
#     m=len(l)
#     ans=0
#     for i in l:
#         m-=1
#         for j in range(i-h):
#             if j:
#                 ans+=int(comb(n,m))
#             n-=1
#         h=i
#     return ans

def get_n(n:int,l:list)->tuple:
    m=len(l)
    th=[-1]*m
    ans=0
    for i in itertools.combinations(range(n),m):
        ans+=1
        flg=True
        for j in i:
            try:
                k=l.index(j)
                th[k]+=1
            except:
                flg=False
        if flg:
            return ans,th


def qwq5decode(f:list):
    f=[open(i,'rb') for i in f]
    f=sorted([(int.from_bytes(i.read(1),'little'),i,) for i in f])
    num=[i[0] for i in f]
    f=[i[1] for i in f]
    for i in num:
        if i<0:
            raise ValueError('num<0')

    m=len(num)
    if m>num[-1]:
        raise ValueError('m>num')

    n=[int.from_bytes(i.read(1),'little') for i in f]
    for i in n:
        if i!=n[0]:
            raise ValueError('n!=n')
    n=n[0]
    if n<m:
        raise ValueError('n<m')
    a,b=get_n(n,num)

    len_key=[int.from_bytes(i.read(2),'little') for i in f]
    for i in len_key:
        if i!=len_key[0]:
            raise ValueError('len_key!=len_key')
    len_key=len_key[0]
    if len_key<0:
        raise ValueError('len_key<0')

    len_info=[int.from_bytes(i.read(2),'little') for i in f]
    for i in len_info:
        if i!=len_info[0] or i<0:
            raise ValueError('len_info')
    len_info=len_info[0]
    
    len_uinfo=[int.from_bytes(i.read(2),'little') for i in f]

    info=[i.read(len_info) for i in f]
    for i in info:
        if i!=info[0]:
            raise ValueError('info')
    info=info[0]

    uinfo=list()
    for j,i in enumerate(len_uinfo):
        if i<0:
            raise ValueError('len_uinfo')
        uinfo.append(f[j].read(i))

    key=0
    for j,i in enumerate(f):
        i.read(len_key*b[j])
        key^=int.from_bytes(i.read(len_key),'little')

    return key.to_bytes(len_key,'little'),info,uinfo

def qwq5AESencrypt(m:int,n:int,p1:str,p2:str=None,key:bytes=os.urandom(32),info:bytes=None,uinfo:list=None):
    _aes.encrypt(key,p1,p2)
    qwq5encode(m,n,key,info,uinfo,pth_l=p1+'.')

def qwq5AESdecrypt(f:list,p1:str,p2:str=None):
    key,info,uinfo=qwq5decode(f)
    _aes.decrypt(key,p1,p2)
    return info,uinfo
