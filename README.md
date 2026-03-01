# Task Manager CLI

Manage users, projects, and tasks from the command line. Data is saved to `data/store.json`.

## Setup

```bash
pip install -r requirements.txt   # optional (only for coloured output)
```

## Commands

```bash
python main.py add-user      --name "Alex" --email "alex@example.com"
python main.py list-users

python main.py add-project   --user "Alex" --title "CLI Tool" --due-date 2025-12-31
python main.py list-projects --user "Alex"

python main.py add-task      --project "CLI Tool" --title "Write tests" --assign "Alex"
python main.py list-tasks    --project "CLI Tool"
python main.py update-task   --project "CLI Tool" --task "Write tests" --status in-progress
python main.py complete-task --project "CLI Tool" --task "Write tests"
```

## Run Tests

```bash
python tests.py
```

## Files

| File | Purpose |
|------|---------|
| `main.py` | CLI commands |
| `models.py` | User, Project, Task classes |
| `storage.py` | Load/save JSON |
| `tests.py` | Unit tests |
