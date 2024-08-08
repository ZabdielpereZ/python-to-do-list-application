from helper import d


def add_task(task_list):
    task = input('Add a task.\n')
    if task not in task_list:
        task_list.append(task)
        print(f'{task} Task added successfully.')
    else:
        print('Task already exists.')

def display_tasks(task_list):
     print('Task list:')
     for item in task_list:
          print(f"- {item}")


def delete_task(task_list):
     task = input('Enter the task to delete.\n')
     if task in task_list:
         task_list.remove(task)
         print(f'{task} Task deleted successfully.')
     else:
         print('Task not found')

# bonus <----- come back!!

#def task_complete(task_list):
#    return [task + " X" for task in task_list]


