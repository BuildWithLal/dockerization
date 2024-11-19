#!/bin/bash

cd ./src

echo "Starting FastAPI application..."

uvicorn main:app --host ${HOST:-0.0.0.0} --port ${APP_PORT:-8000} --reload
