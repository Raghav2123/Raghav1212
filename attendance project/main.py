import time
import json


print("\n")

file=open("data.json","r")
students=json.load(file)
file.close()

f = open(f"{time.strftime('%d-%m-%Y')}.txt", "a")

f.write("\n")

f.write("\n")

checklist=[]
Entry_list=[]

for student2 in students:
  checklist.append(student2['pin'])


print(checklist)
 

def attendance_Entry():
  
  var=input("Enter your pin : ")


  if var =="exit":
    print("Entry saved..")
    exit()

  entry=int(var)


 
  for student in students:
    
    # print(student['pin'])
    if str(entry) in Entry_list:
      print('You have already entered')
      # print(str(student['pin']))
      # print(Entry_list)
      break

    
    elif student['pin']==entry:
      Entry_list.append(str(entry))
      f.write(f"{time.strftime('%H-%M-%S')} | Entry {student['name']} | roll no{student['roll_no']} \n")
      print(f"welcome {student['name']} | roll no{student['roll_no']}")
      break


    elif entry not in checklist:
      print('Invalid Input Please try again')
      break

   
  
      

    

while True:
  attendance_Entry()

f.close()

