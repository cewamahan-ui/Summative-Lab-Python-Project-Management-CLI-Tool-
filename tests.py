# tests.py - unit tests for User, Project, and Task
# Run with: python tests.py

import sys, os, unittest
sys.path.insert(0, os.path.dirname(__file__))
from models import User, Project, Task


class TestTask(unittest.TestCase):

    def test_default_status_is_todo(self):
        t = Task("Write code", "My Project")
        self.assertEqual(t.status, "todo")

    def test_to_dict_and_back(self):
        t = Task("Write code", "My Project", status="done", assigned_to="Alex")
        t2 = Task.from_dict(t.to_dict())
        self.assertEqual(t.title, t2.title)
        self.assertEqual(t.status, t2.status)


class TestProject(unittest.TestCase):

    def test_add_and_find_task(self):
        p = Project("My Project", "Alex")
        p.add_task(Task("Do thing", "My Project"))
        self.assertIsNotNone(p.get_task("do thing"))  # case-insensitive

    def test_to_dict_and_back(self):
        p = Project("My Project", "Alex", due_date="2025-12-31")
        p.add_task(Task("T1", "My Project"))
        p2 = Project.from_dict(p.to_dict())
        self.assertEqual(p2.title, "My Project")
        self.assertEqual(len(p2.tasks), 1)


class TestUser(unittest.TestCase):

    def test_add_and_find_project(self):
        u = User("Alex")
        u.add_project(Project("My Project", "Alex"))
        self.assertIsNotNone(u.get_project("my project"))  # case-insensitive

    def test_to_dict_and_back(self):
        u = User("Alex", "alex@example.com")
        u.add_project(Project("P", "Alex"))
        u2 = User.from_dict(u.to_dict())
        self.assertEqual(u2.name, "Alex")
        self.assertEqual(len(u2.projects), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
