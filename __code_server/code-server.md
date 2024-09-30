# Code-server Set up

To set up code-server on a server so that each student can connect to it via a browser with their own user and folder, follow these steps:

1. **Install code-server**: Install code-server on your server.

2. **Create user accounts**: Create a separate user account for each student.

3. **Configure code-server for each user**: Set up a systemd service for each user to run code-server.

4. **Set up a reverse proxy**: Use a reverse proxy like Nginx to manage the connections and route them to the appropriate code-server instance.

### Step-by-Step Instructions

#### 1. Install code-server

```sh
curl -fsSL https://code-server.dev/install.sh | sh
```

#### 2. Create user accounts

```sh
sudo adduser student1
sudo adduser student2
# Repeat for each student
```

#### 3. Configure code-server for each user

Create a systemd service file for each user. For example, for `student1`:

```sh
sudo nano /etc/systemd/system/code-server-student1.service
```

Add the following content:

```ini
[Unit]
Description=code-server for student1
After=network.target

[Service]
User=student1
WorkingDirectory=/home/student1
ExecStart=/usr/bin/code-server --bind-addr 127.0.0.1:8081
Restart=always

[Install]
WantedBy=multi-user.target
```

Repeat this for each student, changing the `User`, `WorkingDirectory`, and `ExecStart` port.

#### 4. Enable and start the services

```sh
sudo systemctl enable code-server-student1
sudo systemctl start code-server-student1
# Repeat for each student
```

#### 5. Set up a reverse proxy with Nginx

Install Nginx:

```sh
sudo apt update
sudo apt install nginx
```

Configure Nginx to proxy requests to the appropriate code-server instance. Edit the Nginx configuration file:

```sh
sudo nano /etc/nginx/sites-available/default
```

Add the following configuration:

```nginx
server {
    listen 80;
    server_name your_server_domain_or_IP;

    location /student1/ {
        proxy_pass http://127.0.0.1:8081/;
        proxy_set_header Host $host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection upgrade;
        proxy_set_header Accept-Encoding gzip;
    }

    location /student2/ {
        proxy_pass http://127.0.0.1:8082/;
        proxy_set_header Host $host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection upgrade;
        proxy_set_header Accept-Encoding gzip;
    }

    # Repeat for each student
}
```

Restart Nginx:

```sh
sudo systemctl restart nginx
```

### Summary

- Install code-server.
- Create user accounts for each student.
- Configure a systemd service for each user to run code-server.
- Set up Nginx as a reverse proxy to route requests to the appropriate code-server instance.

Each student can now access their own code-server instance via `http://your_server_domain_or_IP/student1/`, `http://your_server_domain_or_IP/student2/`, etc.