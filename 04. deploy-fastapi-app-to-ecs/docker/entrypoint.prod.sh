#!/bin/bash

echo "Starting FastAPI application..."

gunicorn -c gunicorn.conf.py main:app
