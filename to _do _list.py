# To-Do List
tasks = []
print()
n=0
function=0
 
while True:
    print(" ")
    print("""1.Add a task 
2.remove a task 
3.View my  to do list
4.Quit""")
    if function==1 or 2 or 3 or 4:
        function=int(input("Enter your Choice :"))   
        print(" ")
    
       
        if function==1:
        
            task=input("Enter the task to be added:")
            print(" ")
            n=n+1
            tasks.append(task)
            print(n,".Task ",task,"added.")
            print(" ")
        
        elif function==2:
            task=input("Choose the task to be removed:")
            print(" ")
            if task in tasks:
                tasks.remove(task)
                print(f"{task} is removed")
            else:
                print("Invalid index, task not removed.")
                print(" ")
            
        elif function==3:
            if tasks:
                print("Your To-Do List:")
                print(" ")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                   
            else:
                print("Your to-do list is empty.")
                print(" ")
    
        
        elif function==4:
           print("Quit")
           print(" ")
           break
        else:
            print(" Error")       
    else:
     print("Invalid")
     


mainloop()
