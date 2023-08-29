import hashlib

file = open("login/info.txt", "r")
file2 = open("login/salt.txt", "r")

salt = file2.read()


username = input("Username: ")
password = input("Password: ") + salt
username = hashlib.md5(username.encode('utf-8')).hexdigest()
password = password.lower() + username




str2 = ""

arr1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
arr2 = ["z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", " "]

for x in password:
    try:
        str2 += arr2[arr1.index(x)]
    except:
        str2 += ";"

password = hashlib.md5(str2.encode('utf-8')).hexdigest()

if file.read() == username + "," + password:
    print("Success")
else:
    print("Denied")

file.close()
file2.close()

