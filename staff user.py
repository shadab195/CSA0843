tu=int(input("enter the total users: "))
if(tu<=0):
    print("value error")
su=int(input("enter the staff user:"))
if(su<=0):
    print("invalid")
a=su/3
stu=tu-su-a
print("student user: ",stu)
