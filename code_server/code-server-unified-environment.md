To ensure that all students have the same VS Code environment with the same extensions and settings, and to prevent them from modifying these configurations, you can follow these steps:

1. **Create a common configuration directory**: Store the extensions and settings in a common directory.
2. **Set up code-server to use the common configuration**: Configure code-server to use this common directory for extensions and settings.
3. **Set permissions**: Ensure that only the teacher has write permissions to this directory.

### Step-by-Step Instructions

#### 1. Create a Common Configuration Directory

Create a directory to store the common extensions and settings:

```sh
sudo mkdir -p /opt/code-server-config/extensions
sudo mkdir -p /opt/code-server-config/user-data
```

#### 2. Install Extensions and Configure Settings

Install the required extensions and configure the settings as needed. For example, you can manually install extensions and create a `settings.json` file:

```sh
# Install extensions (example)
code-server --install-extension ms-python.python
code-server --install-extension esbenp.prettier-vscode

# Create settings.json
sudo nano /opt/code-server-config/user-data/User/settings.json
```

Add the desired settings to `settings.json`:

```json
{
    "python.pythonPath": "/usr/bin/python3",
    "editor.formatOnSave": true
}
```

#### 3. Set Permissions

Ensure that only the teacher has write permissions to the configuration directory:

```sh
sudo chown -R teacher:teacher /opt/code-server-config
sudo chmod -R 755 /opt/code-server-config
```

#### 4. Configure code-server to Use the Common Configuration

Modify the code-server systemd service file to use the common configuration directory. For example, for [`student1`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22untitled%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22Untitled-1%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A21%2C%22character%22%3A13%7D%7D%5D%2C%227a75e217-23c9-4a5a-9f9d-e54273b3dd64%22%5D "Go to definition"):

```sh
sudo nano /etc/systemd/system/code-server-student1.service
```

Update the [`ExecStart`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22untitled%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22Untitled-1%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A44%2C%22character%22%3A0%7D%7D%5D%2C%227a75e217-23c9-4a5a-9f9d-e54273b3dd64%22%5D "Go to definition") line to include the `--extensions-dir` and `--user-data-dir` options:

```ini
[Unit]
Description=code-server for student1
After=network.target

[Service]
User=student1
WorkingDirectory=/home/student1
ExecStart=/usr/bin/code-server --bind-addr 127.0.0.1:8081 --extensions-dir /opt/code-server-config/extensions --user-data-dir /opt/code-server-config/user-data
Restart=always

[Install]
WantedBy=multi-user.target
```

Repeat this for each student, changing the [`User`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22untitled%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22Untitled-1%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A42%2C%22character%22%3A0%7D%7D%5D%2C%227a75e217-23c9-4a5a-9f9d-e54273b3dd64%22%5D "Go to definition"), [`WorkingDirectory`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22untitled%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22Untitled-1%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A43%2C%22character%22%3A0%7D%7D%5D%2C%227a75e217-23c9-4a5a-9f9d-e54273b3dd64%22%5D "Go to definition"), and [`ExecStart`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22untitled%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22Untitled-1%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A44%2C%22character%22%3A0%7D%7D%5D%2C%227a75e217-23c9-4a5a-9f9d-e54273b3dd64%22%5D "Go to definition") port as needed.

#### 5. Reload and Restart the Services

Reload the systemd daemon and restart the code-server services:

```sh
sudo systemctl daemon-reload
sudo systemctl restart code-server-student1
# Repeat for each student
```

### Summary

- Create a common configuration directory for extensions and settings.
- Install the required extensions and configure the settings.
- Set permissions to ensure only the teacher can modify the configuration.
- Configure code-server to use the common configuration directory.
- Reload and restart the code-server services.

This setup ensures that all students have the same VS Code environment, and only the teacher can modify the extensions and settings.