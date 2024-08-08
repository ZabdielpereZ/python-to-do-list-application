# To-do list app

from helper import d, fd, welcome, clear, reset, exit
from operations import  add_task, display_tasks, delete_task


def main():
    welcome()
    task_list = []
    while True:
        action = input(''' 
select an option you'd like to preform:

menu:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Quit
''')

        if action == '1':
            reset()
            add_task(task_list)
        elif action == '2':
            reset()
            display_tasks(task_list)
        elif action == '3':
            reset()
            pass
        elif action == '4':
            reset()
            delete_task(task_list)
        elif action == '5':
            exit()
            break

main()



