# Todo App Module Deployment Guide

This guide provides instructions for deploying the Todo App module in both Docker and direct Odoo server environments.

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

## 1. Docker Deployment

### Prerequisites
- Docker and Docker Compose installed on the server
- Access to the remote server

### Deployment Steps

1. **Prepare Files Locally**
   - Compress the `todo_app` folder into a ZIP file
   - Gather these files:
     - `todo_app.zip`
     - `docker-compose.yml`
     - `config/odoo.conf`

2. **Server Setup**
   ```bash
   mkdir odoo-todo
   cd odoo-todo
   unzip todo_app.zip
   mkdir config
   ```

3. **Start Containers**
   ```bash
   docker compose up -d
   ```

### Access and Installation
1. Access Odoo at `http://your-server-ip:8069`
2. Create a new database when prompted
3. Go to Apps menu
4. Remove the "Apps" filter from search
5. Search for "Todo App" and install it

### Configuration Details
- **Ports:**
  - Odoo web interface: 8069
  - PostgreSQL: 5432 (internal)
- **Database Credentials:**
  - Username: odoo
  - Password: myodoo
  - Database: postgres

### Updating the Module
1. Make local changes
2. Create new ZIP file
3. Transfer to server
4. Replace existing module
5. Restart containers:
   ```bash
   docker compose restart
   ```

## 2. Direct Odoo Server Deployment

### Prerequisites
- Access to Odoo server (SSH/FTP)
- Sudo privileges

### Deployment Steps

1. **Prepare Module**
   - Create ZIP file of `todo_app` folder
   - Ensure all required files are included

2. **Server Upload**
   - Connect to Odoo server
   - Navigate to addons directory (`/usr/lib/python3/dist-packages/odoo/addons/` or `/opt/odoo/addons/`)
   - Upload `todo_app` folder
   - Set permissions:
     ```bash
     sudo chown -R odoo:odoo todo_app
     sudo chmod -R 755 todo_app
     ```

3. **Configure Odoo**
   - Edit `/etc/odoo/odoo.conf`
   - Update `addons_path`:
     ```
     addons_path = /usr/lib/python3/dist-packages/odoo/addons,/opt/odoo/custom/addons
     ```

4. **Restart Odoo**
   ```bash
   sudo service odoo restart
   ```

5. **Install Module**
   - Login to Odoo web interface
   - Go to Apps
   - Click "Update Apps List"
   - Remove "Apps" filter
   - Search for "Todo App"
   - Click Install

### Troubleshooting

1. **Module Not Visible**
   - Check logs: `sudo tail -f /var/log/odoo/odoo-server.log`
   - Verify permissions
   - Check `addons_path` configuration
   - Update apps list again

2. **Permission Issues**
   ```bash
   sudo chown -R odoo:odoo /path/to/your/module
   sudo chmod -R 755 /path/to/your/module
   ```

3. **Force Update**
   - Update version in `__manifest__.py`
   - Go to Apps → Update Apps List
   - Find module and click Upgrade

### Security Notes
- Module provides full CRUD access to base users
- Review `ir.model.access.csv` for permission adjustments if needed
- Regular backups recommended
