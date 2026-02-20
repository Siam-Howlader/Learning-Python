name= "siam howlader \n\n\n\n\n\n\n"
# print("first name :",name[0:4].upper(),"\nlast name :",name[5:].lower())
# print(name.count("\n"))
# print(name)
# print(len(name))
new_name = name.replace("howlader", "hossain").replace(" \n\n\n\n\n\n\n", "")
# print(new_name)
# reyad="reyad"
# roommate="roommate"
# message="{}s {} is {}".format(new_name,roommate,reyad)
# print(message)
# message2=f"{new_name.upper()}s {roommate} is {reyad.upper()}"
# print(message2)
# fh = dir(new_name)
# for i in range(34,len(fh)):
#     print(i+1,fh[i])
v = new_name.partition(" ")
print(help(str))