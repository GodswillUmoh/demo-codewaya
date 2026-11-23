import argparse
import sys
from task_manager import TaskManager


def print_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "[x]" if task.completed else "[ ]"
        line = f"{status} {task.id}. {task.title}"
        if task.description:
            line += f" - {task.description}"
        print(line)


def main():
    parser = argparse.ArgumentParser(description="Simple task checklist manager")
    parser.add_argument("--file", default="tasks.json", help="Storage file path")

    sub = parser.add_subparsers(dest="command", required=True)

    add_p = sub.add_parser("add", help="Add a new task")
    add_p.add_argument("title", help="Task title")
    add_p.add_argument("-d", "--description", default="", help="Task description")

    list_p = sub.add_parser("list", help="List tasks")
    list_p.add_argument("-a", "--all", action="store_true", help="Include completed tasks")

    done_p = sub.add_parser("done", help="Mark a task as completed")
    done_p.add_argument("id", type=int, help="Task id")

    del_p = sub.add_parser("delete", help="Delete a task")
    del_p.add_argument("id", type=int, help="Task id")

    args = parser.parse_args()
    manager = TaskManager(storage_file=args.file)

    if args.command == "add":
        task = manager.add_task(args.title, args.description)
        print(f"Added task {task.id}: {task.title}")
    elif args.command == "list":
        print_tasks(manager.list_tasks(include_completed=args.all))
    elif args.command == "done":
        if manager.complete_task(args.id):
            print(f"Completed task {args.id}")
        else:
            print(f"Task {args.id} not found")
            sys.exit(1)
    elif args.command == "delete":
        if manager.delete_task(args.id):
            print(f"Deleted task {args.id}")
        else:
            print(f"Task {args.id} not found")
            sys.exit(1)


if __name__ == "__main__":
    main()
