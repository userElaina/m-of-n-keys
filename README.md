# m of n keys
一个 **key** /文件生成 `n` 个 **keyfile**,
获取其中的任意 `m` 个即可还原 **key** /解密原文件.

原理是对每一种组合生成一组异或和为原 **key** 的序列...
从密码学角度来说很扭曲)

### 接口介绍
#### qwq5.qwq5encode
通过 **key** 生成 `n` 个 **keyfile**.
##### 函数定义
```py
def qwq5encode(m:int,n:int,key:bytes=os.urandom(32),info:bytes=None,uinfo:list=None,pth_l:str='',pth_r:str='.key')->None:
```
##### 变量介绍
|名称   |类型   |解释|
|-      |-      |-|
|`m`    |`int`  |上述 `m`|
|`n`    |`int`  |上述 `n`|
|`key`  |`bytes`|上述 **key**|
|`info` |`bytes`|附加信息1|
|`uinfo`|`list` |附加信息2|
|`pth_l`|`str`  |**keyfile** 的路径前缀|
|`pth_r`|`str`  |**keyfile** 的路径后缀|
附加信息1与 **key** 相关,如 **key** 的哈希/需要用 **key** 解密的文件的哈希.

附加信息2与每个 **keyfile** 相关.

这些附加信息将分别写入每个 **keyfile** 中.
它们可以是 `b''` `os.urandom(233)` 等任何 `bytes`.

#### qwq5.qwq5decode
通过 `m` 个 **keyfile** 还原 **key**.
##### 函数定义
```py
def qwq5decode(f:list)->tuple:
```
##### 变量介绍
|名称   |类型   |解释|
|-      |-      |-|
|`f`    |`str`  |`m` 个 **keyfile** 的路径|
|返回值 |`tuple`|(key,info,uinfo)|

#### _aes.encrypt
将文件以随机生成的 `vi` 进行 **AES_CBC**, 自动加入包含原文件长度/原文件名的文件头.
##### 函数定义
```py
def _aes.encrypt(key:bytes,p1:str,p2:str=None)->None:
```
##### 变量介绍
|名称   |类型   |解释|
|-      |-      |-|
|`key`  |`bytes`|密钥|
|`p1`   |`str`  |待加密的文件路径|
|`p2`   |`str`  |加密后的文件路径|

#### _aes.decrypt
将 `_aes.encrypt` 生成的文件解密,即其反函数.
##### 函数定义
```py
def _aes.decrypt(key:bytes,p1:str,p2:str=None)->None:
```
##### 变量介绍
|名称   |类型   |解释|
|-      |-      |-|
|`key`  |`bytes`|密钥|
|`p1`   |`str`  |待解密的文件路径|
|`p2`   |`str`  |解密后的文件路径|


#### qwq5.qwq5AESencrypt
使用 **AES_CBC** 加密文件并生成如上所述 `n` 个 **keyfile**.
##### 函数定义
```py
def qwq5AESencrypt(m:int,n:int,p1:str,p2:str=None,key:bytes=os.urandom(32),info:bytes=None,uinfo:list=None)->None:
```
##### 变量介绍
|名称   |类型   |解释|
|-      |-      |-|
|`m`    |`int`  |上述 `m`, 同 `qwq5.qwq5encode`|
|`n`    |`int`  |上述 `n`, 同 `qwq5.qwq5encode`|
|`p1`   |`str`  |待加密的文件路径,同 `_aes.encrypt`|
|`p2`   |`str`  |加密后的文件路径,同 `_aes.encrypt`|
|`key`  |`bytes`|上述 **key**, 同 `qwq5.qwq5encode`|
|`info` |`bytes`|附加信息1,同 `qwq5.qwq5encode`|
|`uinfo`|`list` |附加信息2,同 `qwq5.qwq5encode`|

#### qwq5.qwq5AESdecrypt
通过 `m` 个 **keyfile** 解密文件.
##### 函数定义
```py
def qwq5AESdecrypt(f:list,p1:str,p2:str=None)->tuple:
```
##### 变量介绍
|名称   |类型   |解释|
|-      |-      |-|
|`f`    |`list` |`m` 个 **keyfile** 的路径,同 `qwq5.qwq5decode`|
|`p1`   |`str`  |待解密的文件路径,同 `_aes.decrypt`|
|`p2`   |`str`  |解密后的文件路径,同 `_aes.decrypt`|
