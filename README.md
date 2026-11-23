# Demo Repo — Python Task Checklist

A simple command-line task checklist manager, built as a demo repo for testing codewaya.

## Requirements
- Python 3.8+

No third-party dependencies.

## Usage

```bash
# Add a task
python cli.py add "Buy groceries" -d "Milk, eggs, bread"

# List tasks (all, including completed)
python cli.py list --all

# List only incomplete tasks
python cli.py list

# Mark a task done
python cli.py done 1

# Delete a task
python cli.py delete 1
```

Tasks are persisted to `tasks.json` in the current directory.

## Run tests

```bash
python -m unittest discover -s tests
```
