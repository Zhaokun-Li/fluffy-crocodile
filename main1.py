def printout(todolist):
    print(todolist)

def delete(todolist,index):
    if len(todolist)==0:
        print("you have nothing to delete")
    else:
        if len(todolist)<index:
            print("out of index")
        else:
            del todolist[index]
            print("delete successful")