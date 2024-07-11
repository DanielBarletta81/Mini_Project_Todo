# User Interface (UI):
#Create a command-line interface (CLI) for the To-Do List Application.
#Display a welcoming message and a menu with the following options:


#  Menu:
#  1. Add a task
#  2. View tasks
#  3. Mark a task as complete
#  4. Delete a task
#  5. Quit



tasks = []

#Error Handling:
#Implement error handling using try, except, else, 
# and finally blocks to handle potential issues.

def add_task():
    try:
        task =  input("What task would you like to add? ")
        tasks.append({ "title": task, "status": "Incomplete" })

    except ValueError:
        print(ValueError)

    finally:
       print(f'Task added successfully!')

def view_tasks():
       
       if len(tasks) == 0:
             print("No tasks to display.")
       else:
             print("Current list of tasks: ")
             for i, task in enumerate(tasks):
                   status = "Incomplete" if task["status"] else "Completed"
                   print(f'{i +1} {task} ')

def mark_task_complete():
    try:
    
      if len(tasks) == 0:
        print("No tasks to mark complete.")
      else:
        print("Current list of tasks: ")
        for i, task in enumerate(tasks):
         print(f'{i +1}. {task}')

        mark_complete = int(input("Which task would you like to mark complete? ")) - 1 

        if  0 <= mark_complete <= len(tasks):

                tasks[mark_complete]["status"] = 'Completed'
                print(f'Task successfully marked complete.') 
        
        else:
                print("Please enter a valid task to mark complete. ")

    except ValueError:
        print(f'An error occurred. Make sure to only enter numbers!')
        
                  
def delete_task():
    try:
       
       if len(tasks) == 0:
             print("No tasks to delete.")
       else:
         
            for i, task in enumerate(tasks):
                   print(f'{i +1}. {task}')
                   
            task_to_delete = int(input("Which task would you like to delete? "))
            task_to_delete = task_to_delete - 1

            if 0 < task_to_delete <= len(tasks):
                    tasks.remove(task_to_delete)
                    print(f'Task deleted successfully!' )
                 
            else:
                         print("Please enter a valid task to delete. ")
    except ValueError:
         print("Please be sure to enter numbers only.")


def interface():
    try:
        while True:
                print(" **** Welcome to your Todo Application ****")
                print(" Menu: ")
                print(" 1. Add task")
                print(" 2. View all tasks")
                print(" 3. Mark a task complete")
                print(" 4. Delete  a task")
                print(" 5. Quit")


                choice = int(input("Please select a choice (1-5). "))

                if choice == 1:
                    add_task()
                elif choice == 2:
                    view_tasks()
                elif choice == 3:
                    mark_task_complete()
                elif choice == 4:
                      delete_task()
                else:
                      print("Thank you for using the Todo application!")
                      break
    except ValueError:
        print("Please enter a valid choice, numbers only.")
        if ValueError:
             interface()  # restart program if value error
            

interface()