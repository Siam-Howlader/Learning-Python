names=[]
marks=[]
grades=[]
flag=True
menu = f"""#{'='*30} MENU {'='*30}
#{' '*26}1. Add Student{' '*25}#
#{' '*26}2. Show All Students{' '*19}#
#{' '*26}3. Search Student{' '*22}#
#{' '*26}4. Show Topper{' '*25}#
#{' '*26}5. Exit{' '*32}#
#{'='*65}#
"""
while(flag):
    print(menu)
    m=int(input("Eneter number(1-5) : "))
    if(m==5):
        print(f"\n{"="*66}\n#{" "*28} EXITED {" "*28}#\n{"="*66}")
        flag=False
        break
    elif(m==1):
        name=input("Enter student name : ").strip()
        mark=-1
        while mark<0 or mark>100:
            mark = int(input("Enter students mark(0-100): "))
        names.append(name)
        marks.append(mark)
        if(mark>=80):
            grades.append("A+")
        elif(mark>=70):
            grades.append("A")
        elif (mark >= 60):
            grades.append("B")
        elif (mark >= 50):
            grades.append("C")
        else:
            grades.append("F")
    elif(m==2):
        for i in range(0,len(names)):
            print(f"Name : {names[i]} | Marks : {marks[i]} | Grade : {grades[i]}")
    elif(m==3):
        name=input("Enter name : ").strip().lower()
        for i in range(0,len(names)):
            if names[i].lower()==name:
                print(f"Name : {names[i]} | Marks : {marks[i]} | Grade : {grades[i]}")
                break
        else:
            print("Student not found!")
    elif(m==4):
        highest_mark= max(marks)
        idx = marks.index(highest_mark)
        print("="*10,"Topper details","="*10)
        print(f"Name : {names[idx]} | Marks : {marks[idx]} | Grade : {grades[idx]}")
    else:
        print("Enter correct number. Thank you.")