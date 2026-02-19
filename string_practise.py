#1️⃣ Reverse a String
hl = "hello"
print(hl[::-1])

#2️⃣ Count Vowel
pr="programming"
print(pr.count("a")+pr.count("e")+pr.count("i")+pr.count("o")+pr.count("u"))

#3️⃣ Check Palindrome
pl="madam"
print(pl==pl[::-1])
pll = "hello"
print(pll==pll[::-1])

#4️⃣ Count Characters
bn="banana"
str=""
for i in bn:
    if not str.count(i):
        print(i,"-->",bn.count(i))
        str+=i

#5️⃣ Remove Spaces
strr = "hello world python"
print(strr.replace(" ",""))

#6️⃣ Find Longest Word
lw = "I love backend development"
arr=lw.split(" ")
ans=""
for a in arr:
    if(len(a)>len(ans)):
        ans=a
print(ans)

#7️⃣ Capitalize First Letter of Each Word
wr = "python backend developer"
nrr=wr.split(" ")
for i in range(len(nrr)):
    nrr[i]=nrr[i].capitalize()
print(" ".join(nrr))

#8️⃣ Check Anagram
an="listen"
an2="silent"
print("".join(sorted(an)) == "".join(sorted(an2)))

#9️⃣ Count Words
words ="I love python very much"
print(words.count(" ")+1)

#🔟 Remove Duplicate Characters
strrr="programming"
ans=""
for i in strrr:
    if not (ans.count(i)):
        ans+=i

print(ans)
#11️⃣ First Non-Repeating Character
nr = "aabbcdd"
for i in nr:
    if nr.count(i)==1:
        print(i)
        break

#12️⃣ Most Frequent Character
crr="banana"
ans=""
var=0
for i in crr:
    if crr.count(i)>var:
        var = crr.count(i)
        ans=i
print(ans)


#13️⃣ String Compression
cmp = "aaabbc"
ann=""
for i in cmp:
    if not ann.count(i):
        print(i+str(cmp.count(i)),end="")
        ann+=i


#14️⃣ Check if String Contains Only Digits
dns = "123a5"
ans=True
for i in dns:
    if not i.isdigit():
        ans=False
        break
print(ans)

#15️⃣ Find All Substrings
str="abcde"
for i in range(0,len(str)):
    for j in range(len(str),i,-1):
        print(str[i:j])