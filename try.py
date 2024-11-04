def sort_todo_list_by_time(todo_list):
    try:
        sorted_todo_list = sorted(
            todo_list.items()
            key=lambda x: datetime.strptime(x[1],"%Y-%m=%d %H:%M")
        )
    except ValueError:
        print("One or more dates are in an incorrect format. Please use 'YYYY-MM-DD HH:MM'.")

    print("\nTo-do list sorted by time:")
    for event, date_str in sorted_todo_list:
        print(f"{event}: {date_str}")

todo_list = add_event()
sort_todo_list_by_time(todo_list)