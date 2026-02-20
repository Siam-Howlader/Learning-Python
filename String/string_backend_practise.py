# 1️⃣ Email Validator(Basic Version)
# email="siamhossain0804@gmail.com"
# if email.find("@") > 0 and email.count("@") == 1 and email.find(".", email.find("@")+1,len(email))>=0:
#     print(True)
# else:
#     print(False)

# 2️⃣ Username Validator
# user_name="si$am_19"
# if ((user_name[0]>="0" and user_name[0]<="9") or (user_name.find("-")>=0) or (not user_name.isalnum())):
#     print(False)
# else:
#     print(True)

# 3️⃣ Password Strength Checker
# password = "hello230219world"
# temp=0
# if len(password)>=8:
#     for i in password:
#         if i.islower():
#             temp+=1
#         elif i.isupper():
#             temp += 1
#         elif i.isdigit():
#             temp+=1
#         elif i in "!@#$%^&*":
#             temp+=1
#     if temp>2:
#         print("Strong Password")
#     elif temp>0:
#         print("Medium Password")
#     else:
#         print("Weak Password")
# else:
#     print("Required at least 8 characters")

# 4️⃣ Slug Generator(Used in URLs)
# slug = "Pyth@on Backend Devel_opment Course"
# slug=slug.lower().replace(" ","-")
# arr=list(slug)
# for i in arr:
#     if i!="-" and (not i.islower()):
#         arr.remove(i)
# print("".join(arr))

# 5️⃣ Extract Domain From Email
# email="siamhossain0804@gmail.com"
# print(email[email.find("@")+1:])

# 1️⃣ JWT Token Parser(Backend Authentication)
# token = "abc123.def456.ghi789"
# arr=token.split(".")
# print(arr)
# if len(arr)==3:
#     header,payload,signature=arr
#     print("Header :",header)
#     print("Payload :", payload)
#     print("Signature :", signature)
# else:
#     print("Invalid")


# 2️⃣ Log Parser (Very Common in Backend)
# log = "ERROR 2026-02-19 UserNotFound: user_id=42"

# parts = log.split()

# level = parts[0]
# date = parts[1]

# message_part = log.split(":")[0].split(" ", 2)[2]
# user_id = log.split("user_id=")[1]

# print("Level:", level)
# print("Date:", date)
# print("Message:", message_part)
# print("User ID:", user_id)

# 3️⃣ Parse URL Query String
# url = "page=2&limit=10&sort=asc"

# params = {}

# pairs = url.split("&")

# for pair in pairs:
#     key, value = pair.split("=")
#     params[key] = value

# print(params)

# 4️⃣ Parse HTTP Header
# header = "Content-Type: application/json"

# parts = header.split(":",1)

# key = parts[0].strip()
# value = parts[1].strip()

# print("Header Name:", key)
# print("Header Value:", value)

# data = "name=Siam;age=22;city=Dhaka"
# dicts={}
# lt=data.split(";")
# for i in lt:
#     key,value=i.split("=")
#     dicts[key]=value
# print(dicts)

