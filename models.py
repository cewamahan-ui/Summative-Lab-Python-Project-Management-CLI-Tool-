# models.py - User, Project, and Task classes

class Task:
    next_id = 1

    def __init__(self, title, project, status="todo", assigned_to=""):
        self.id = Task.next_id
        Task.next_id += 1
        self.title = title
        self.project = project
        self.status = status  # todo / in-progress / done
        self.assigned_to = assigned_to

    def to_dict(self):
        return {"id": self.id, "title": self.title, "project": self.project,
                "status": self.status, "assigned_to": self.assigned_to}

    @classmethod
    def from_dict(cls, d):
        t = cls(d["title"], d["project"], d["status"], d["assigned_to"])
        t.id = d["id"]
        return t

    def __str__(self):
        return f"  [{self.id}] {self.title} ({self.status}) -> {self.assigned_to or 'unassigned'}"


class Project:
    next_id = 1

    def __init__(self, title, owner, due_date=""):
        self.id = Project.next_id
        Project.next_id += 1
        self.title = title
        self.owner = owner
        self.due_date = due_date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_task(self, title):
        for t in self.tasks:
            if t.title.lower() == title.lower():
                return t

    def to_dict(self):
        return {"id": self.id, "title": self.title, "owner": self.owner,
                "due_date": self.due_date, "tasks": [t.to_dict() for t in self.tasks]}

    @classmethod
    def from_dict(cls, d):
        p = cls(d["title"], d["owner"], d["due_date"])
        p.id = d["id"]
        p.tasks = [Task.from_dict(t) for t in d["tasks"]]
        return p

    def __str__(self):
        return f"  [{self.id}] {self.title} (due: {self.due_date or 'none'}) - {len(self.tasks)} tasks"


class User:
    next_id = 1

    def __init__(self, name, email=""):
        self.id = User.next_id
        User.next_id += 1
        self.name = name
        self.email = email
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def get_project(self, title):
        for p in self.projects:
            if p.title.lower() == title.lower():
                return p

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email,
                "projects": [p.to_dict() for p in self.projects]}

    @classmethod
    def from_dict(cls, d):
        u = cls(d["name"], d["email"])
        u.id = d["id"]
        u.projects = [Project.from_dict(p) for p in d["projects"]]
        return u

    def __str__(self):
        return f"  [{self.id}] {self.name} ({self.email or 'no email'}) - {len(self.projects)} projects"
