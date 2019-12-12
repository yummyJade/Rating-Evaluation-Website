# hashlib加密示例
import hashlib
pwd = 'sk123'

#创建sha1对象
sha1 = hashlib.sha1()
#对字符进行加密，默认支持字节串，字符串须先编码
sha1.update(pwd.encode())
#获取加密后的数据（字符串）
res1 = sha1.hexdigest()
# res1 = sha1.digest()  这个返回的是字节穿
print(res1,type(res1))
#打印结果：7c610fefe783705bb3ff23bed147d7e1e4a213c7 <class 'str'>
