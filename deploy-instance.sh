#!/bin/bash

# Install Docker and Docker Compose
sudo apt-get update
sudo apt-get install -y docker.io docker-compose

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Clone your repository (replace with your repo URL)
git clone YOUR_GITHUB_REPO_URL
cd christmas-stock-picker

# Build and run with Docker Compose
sudo docker-compose up -d --build 