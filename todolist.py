# User Interface (UI):
#Create a command-line interface (CLI) for the To-Do List Application.
#Display a welcoming message and a menu with the following options:


#  Menu:
#  1. Add a task
#  2. View tasks
#  3. Mark a task as complete
#  4. Delete a task
#  5. Quit

def add_task():
       pass
def view_tasks():
       pass
def mark_task_complete():
       pass
def delete_task():
       pass


def interface():
        while True:
                print(" **** Welcome to your Todo Application ****")
                print(" Menu: ")
                print(" 1. Add task")
                print(" 2. View all tasks")
                print(" 3. Mark a task complete")
                print(" 4. Delete  a task")
                print(" 5. Quit")

                choice = int(input("Please select a choice (1-5)."))

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
interface()