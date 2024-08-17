#!/bin/bash
set -a


echo "Checking if the .rc file exists..."
if [ ! -f ./.rc ]; then
    echo "The .rc file does not exist. Please create it before running this script."
    exit 1
fi

echo "Sourcing the .rc file..."

source ./.rc

USER=$(whoami)
GROUP=$(whoami)
USER_ID=$(id -u)
GROUP_ID=$(id -g)

if [ -z "$USER" ]; then
  USER=ocpuser
fi

if [ -z "$GROUP" ]; then
  GROUP=ocpgroup
fi

if [ -z "$USER_ID" ]; then
  USER_ID=1000
fi

if [ -z "$GROUP_ID" ]; then
  GROUP_ID=1000
fi

export USER GROUP USER_ID GROUP_ID


echo "Creating the ./static/* directories..."
mkdir -p ./static/admin
mkdir -p ./static/rest_framework

export BACKEND_RUN_SRVR_COMMAND="python manage.py runserver 0.0.0.0:8000"

echo "Building the containers..."
docker compose -f docker-compose.yml -p orc build

echo "Running the backend server..."
docker compose -f docker-compose.yml -p orc up

echo "Script finished. You can pass --help or -h to see the available options."
exit 0
