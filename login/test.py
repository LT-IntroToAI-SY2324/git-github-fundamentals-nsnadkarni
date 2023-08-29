import hashlib

file = open("login/info.txt", "w")

user = input("Enter a username: \n")
user = hashlib.md5(user.encode('utf-8')).hexdigest() 

str = input("Enter a Password: \n")
str = str.lower() + "salt" + user
str2 = ""

arr1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
arr2 = ["z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", " "]

for x in str:
    try:
        str2 += arr2[arr1.index(x)]
    except:
        str2 += ";"

hash_val2 = hashlib.md5(str2.encode('utf-8')).hexdigest()

str = input("Repeat Password: \n")
str = str.lower() + "salt" + user
str2 = ""

arr1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
arr2 = ["z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", " "]

for x in str:
    try:
        str2 += arr2[arr1.index(x)]
    except:
        str2 += ";"

hash_val = hashlib.md5(str2.encode('utf-8')).hexdigest()

if hash_val == hash_val2:
    file.write(user + "," + hash_val)
    print("Success")
else:
    print("Error")

file.close()