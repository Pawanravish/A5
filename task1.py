Student_data={"pawan":100,"siddharth":33,"raman":97,"prashat":75}
print(Student_data.values())
print(Student_data.keys())
User_Ques=input("enter Student name to know the number")

def Student_Marks_Finder(User_Ques):

     for i in Student_data.keys():
         if i==User_Ques:
             return Student_data[i]
     else :
      print("Student Marks  not available")

ans=Student_Marks_Finder(User_Ques)
print(ans)



