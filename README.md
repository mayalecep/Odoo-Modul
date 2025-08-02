# Odoo Todo App Module

A simple and efficient Todo application module for Odoo 16.0. This module helps users manage their tasks with features like priority setting, deadlines, and status tracking.

## Features

- Task management with name and description
- Priority levels (Low, Normal, High)
- Deadline tracking
- Task completion status
- User-friendly views (Tree and Form)

## Requirements

- Odoo 16.0
- Python 3.x
- PostgreSQL

## Installation

### Using Docker

1. Clone this repository:
```bash
git clone https://github.com/mayalecep/Odoo-Modul.git
cd Odoo-Modul
```

2. Start the containers:
```bash
docker compose up -d
```

3. Access Odoo at `http://localhost:8069`
4. Create a new database when prompted
5. Go to Apps menu
6. Remove the "Apps" filter from search
7. Find and install "Todo App"

### Direct Installation on Odoo Server

1. Copy the `todo_app` folder to your Odoo addons directory
2. Set proper permissions:
```bash
sudo chown -R odoo:odoo todo_app
sudo chmod -R 755 todo_app
```

3. Restart Odoo service:
```bash
sudo service odoo restart
```

4. Install the module through Odoo interface

For detailed deployment instructions, see [deployment.md](deployment.md)

## Module Structure

```
todo_app/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── todo.py
├── security/
│   └── ir.model.access.csv
└── views/
    └── todo_view.xml
```

## Configuration

The module comes with default access rights that allow all users to:
- Create tasks
- Read tasks
- Update tasks
- Delete tasks

You can modify these permissions in `security/ir.model.access.csv`.

## Usage

1. After installation, you'll find "Todo Tasks" in your Odoo menu
2. Click "Create" to add a new task
3. Fill in the task details:
   - Task Name (required)
   - Description (optional)
   - Priority (Low/Normal/High)
   - Deadline
4. Mark tasks as done when completed

## Development

This module is developed on the `dev` branch. To contribute:

1. Fork this repository
2. Create your feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## License

This module is licensed under LGPL-3.

## Support

For issues and feature requests, please use the GitHub issues tracker.
