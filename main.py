# main.py - CLI entry point
# Run: python main.py add-user --name "Alex"

import argparse, sys
import storage
from models import User, Project, Task


def find_user(users, name):
    for u in users:
        if u.name.lower() == name.lower():
            return u
    sys.exit(f"User '{name}' not found.")


def find_project(users, title):
    for u in users:
        p = u.get_project(title)
        if p:
            return p
    sys.exit(f"Project '{title}' not found.")


def main():
    parser = argparse.ArgumentParser(prog="taskman")
    sub = parser.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("add-user");    s.add_argument("--name", required=True); s.add_argument("--email", default="")
    sub.add_parser("list-users")
    s = sub.add_parser("add-project"); s.add_argument("--user", required=True); s.add_argument("--title", required=True); s.add_argument("--due-date", default="", dest="due_date")
    s = sub.add_parser("list-projects"); s.add_argument("--user", default="")
    s = sub.add_parser("add-task");    s.add_argument("--project", required=True); s.add_argument("--title", required=True); s.add_argument("--assign", default="")
    s = sub.add_parser("list-tasks");  s.add_argument("--project", required=True)
    s = sub.add_parser("update-task"); s.add_argument("--project", required=True); s.add_argument("--task", required=True); s.add_argument("--status", choices=["todo","in-progress","done"]); s.add_argument("--assign", default="")
    s = sub.add_parser("complete-task"); s.add_argument("--project", required=True); s.add_argument("--task", required=True)

    args = parser.parse_args()
    users = storage.load()

    if args.cmd == "add-user":
        users.append(User(args.name, args.email))
        storage.save(users)
        print(f"User '{args.name}' added.")

    elif args.cmd == "list-users":
        print("Users:") or [print(u) for u in users] if users else print("No users.")

    elif args.cmd == "add-project":
        u = find_user(users, args.user)
        u.add_project(Project(args.title, u.name, args.due_date))
        storage.save(users)
        print(f"Project '{args.title}' added for '{u.name}'.")

    elif args.cmd == "list-projects":
        pool = [find_user(users, args.user)] if args.user else users
        projects = [p for u in pool for p in u.projects]
        print("Projects:") or [print(p) for p in projects] if projects else print("No projects.")

    elif args.cmd == "add-task":
        p = find_project(users, args.project)
        p.add_task(Task(args.title, p.title, assigned_to=args.assign))
        storage.save(users)
        print(f"Task '{args.title}' added to '{p.title}'.")

    elif args.cmd == "list-tasks":
        p = find_project(users, args.project)
        print(f"Tasks in '{p.title}':") or [print(t) for t in p.tasks] if p.tasks else print("No tasks.")

    elif args.cmd == "update-task":
        p = find_project(users, args.project)
        t = p.get_task(args.task) or sys.exit(f"Task '{args.task}' not found.")
        if args.status: t.status = args.status
        if args.assign: t.assigned_to = args.assign
        storage.save(users)
        print(f"Task '{t.title}' updated.")

    elif args.cmd == "complete-task":
        p = find_project(users, args.project)
        t = p.get_task(args.task) or sys.exit(f"Task '{args.task}' not found.")
        t.status = "done"
        storage.save(users)
        print(f"Task '{t.title}' marked as done.")


if __name__ == "__main__":
    main()
