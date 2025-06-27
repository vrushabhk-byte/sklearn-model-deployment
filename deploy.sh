#!/bin/bash
# Example remote deployment script

SERVER="your_user@your_server_ip"
APP_DIR="/home/your_user/ml-deploy-mini"

echo "Deploying to $SERVER..."

scp -r * $SERVER:$APP_DIR
ssh $SERVER <<EOF
    cd $APP_DIR
    docker build -t ml-api .
    docker stop ml-api-container || true
    docker rm ml-api-container || true
    docker run -d -p 5000:5000 --name ml-api-container ml-api
EOF
