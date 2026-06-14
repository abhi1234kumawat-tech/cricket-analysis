def todo_manager():

    tasks = []

    print("=" * 45)
    print("         TO-DO LIST MANAGER")
    print("=" * 45)
    print("  Commands Available:")
    print("  1. Add Task")
    print("  2. View Tasks")
    print("  3. Update Task Status")
    print("  4. Delete Task")
    print("  5. Exit")
    print("=" * 45)

    while True:

        try:
            choice = int(input("\nEnter your choice (1-5): "))
        except ValueError:
            print("  ❌ Invalid input: please enter 1 to 5")
            continue

        # ── Add Task ─────────────────────────────────────
        if choice == 1:
            print("\n" + "=" * 45)
            print("           ADD NEW TASK")
            print("=" * 45)

            task_name = input("  Enter task name   : ").strip()
            status    = input("  Enter status      : ").strip()

            if not task_name or task_name == "":
                print("\n  ❌ Status : Give a valid task")
                continue

            if not status or status == "":
                status = "Pending"

            duplicate = any(
                t["task"].lower() == task_name.lower()
                for t in tasks
            )

            if duplicate:
                print("\n  ❌ Status : This is duplicate task")
                continue

            task_id = len(tasks) + 1

            tasks.append({
                "id"     : task_id,
                "task"   : task_name,
                "status" : status
            })

            print("\n" + "=" * 45)
            print("         TASK ADDED SUCCESSFULLY")
            print("=" * 45)
            print(f"  Task ID  : {task_id}")
            print(f"  Task     : {task_name}")
            print(f"  Status   : {status}")
            print("=" * 45)

        # ── View Tasks ───────────────────────────────────
        elif choice == 2:
            print("\n" + "=" * 55)
            print("              YOUR TO-DO LIST")
            print("=" * 55)

            if not tasks:
                print("  ⚠️  No tasks found — add a task first")
                print("=" * 55)
                continue

            print(f"  {'ID':<6} {'Task':<25} {'Status'}")
            print("-" * 55)

            for t in tasks:
                print(f"  {t['id']:<6} {t['task']:<25} {t['status']}")

            print("=" * 55)
            print(f"  Total Tasks : {len(tasks)}")
            print("=" * 55)

        # ── Update Task Status ───────────────────────────
        elif choice == 3:
            print("\n" + "=" * 45)
            print("          UPDATE TASK STATUS")
            print("=" * 45)

todo_manager()