data = "username=   SiamHossain  ;email=siamg@mailc.om;password=Hello123!"

arr = data.split(";")
dictt = {}
for i in arr:
    key,value=i.split("=")
    dictt[key]=value

user_name=dictt["username"].strip()
email=dictt["email"].strip()
password=dictt["password"]

if ((len(user_name)>=4 and len(user_name)<=20) and (not user_name[0].isdigit())):
    f1=True
    for i in user_name:
        if (i.isalnum() or (i in "_")):
            continue
        else:
            f1=False
            break
else:
    f1=False

email_arr=email.split("@")
if len(email_arr)==2:
    if len(email_arr[0])>0 and len(email_arr[1])>0:
        if email_arr[0].isalnum():
            arr2=email_arr[1].split(".")
            f2=True
            if len(arr2)>=2:
                for j in arr2:
                    if(len(j)==0 or (not j.isalpha())):
                        f2=False
                        break
            else:
                f2=False
        else:
            f2=False
    else:
        f2=False
else:
    f2=False

f3=True
if(len(password)>=8):
    f4,f5,f6,f7=False,False,False,False
    val=0
    for k in password:
        if k.islower():
            f4=True
        elif k.isupper():
            f5=True
        elif k.isdigit():
            f6=True
        elif k in "!@#$%^&*":
            f7=True
    if f4:
        val+=1
    if f6:
        val+=1
    if f5:
        val+=1
    if f7:
        val+=1
    if(val!=4):
        f3=False
else:
    f3=False

if(f1 and f2 and f3):
    print("Registration Successful")
elif not f1:
    print("Registration Failed: Invalid Username")
elif not f2:
    print("Registration Failed: Invalid Email")
elif not f3:
    print("Registration Failed: Invalid Password")