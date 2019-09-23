import hashlib 

password = 'abcd1234'

result = hashlib.md5(password.encode()) 
password_hash = result.hexdigest()
print(password_hash)
