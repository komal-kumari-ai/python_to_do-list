to_do_list = []

task = input("Enter your task here: ")

to_do_list.append(task)

for task in to_do_list:
    print(task)

task = input("Enter another task: ")
to_do_list.append(task)

for task in to_do_list:
    print(task)