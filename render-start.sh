#!/bin/bash

# Render startup script for Diet and Workout Recommendation System

echo "Starting Diet and Workout Recommendation System on Render..."

# Check if GROQ_API_KEY is set
if [ -z "$GROQ_API_KEY" ]; then
    echo "Error: GROQ_API_KEY environment variable is not set"
    echo "Please set your Groq API key in the Render dashboard"
    exit 1
fi

# Start the application with Gunicorn
echo "Starting Gunicorn server..."
exec gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --access-logfile - --error-logfile - wsgi:app 