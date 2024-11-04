todolist=[]
def add(eventandtime):
    if eventandtime != None:
        todolist.append(eventandtime)
        print("add successful")
    else:
        print("please enter an event and time")
    return todolist
def delete(eventandtime):
    if len(todolist)==0:
        print("you have nothing to delete")
    else:
        for i in todolist:
            if i==eventandtime:
                todolist.remove(i)
                print("delete successful")
            else:
                print("that is not in your list")
def clearlist():
    todolist.clear()
    print("clear successful")
    return todolist

while True:
    option=input("please enter either you want to add or delete or clear the list(enter exit to quit): ").lower()
    if option=="add":
        newevent=input("please enter the event and time: (form: event,time) ")
        add(newevent)
    elif option=="delete":
        deleteevent=input("please enter the event and time you want to delete: (form: event,time) ")
        delete(deleteevent)
    elif option=="clear":
        clearlist()
    elif option=="exit":
        break
    print("your todolist is: ")
    for i in todolist:
        print(i)

