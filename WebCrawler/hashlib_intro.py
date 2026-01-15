import hashlib

name_str = "Yuan Ze University"
name_str_bin = name_str.encode("utf-8")  # encode the string to utf-8


data = hashlib.sha512()
data.update(name_str_bin)  # hash-the-bytes

print(data.hexdigest())
