#!/bin/bash
# Install system dependencies
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv nginx

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Configure Nginx
sudo bash -c 'cat > /etc/nginx/sites-available/flask_app <<EOF
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF'

# Enable the Nginx site
sudo ln -sf /etc/nginx/sites-available/flask_app /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default

# Restart Nginx
sudo systemctl restart nginx

# Start the application with Gunicorn
gunicorn --config gunicorn_config.py wsgi:app 