# Gunicorn configuration file
bind = "0.0.0.0:8080"
workers = 3
timeout = 120
accesslog = "-"
errorlog = "-" 