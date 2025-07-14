# Docker Deployment Guide

This guide explains how to deploy the Diet and Workout Recommendation System using Docker.

## Prerequisites

- Docker installed on your system
- Docker Compose installed
- Groq API key

## Quick Start

### 1. Set up Environment Variables

Create a `.env` file in the project root:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 2. Build and Run

#### Development Mode
```bash
# Build and run in development mode
docker-compose up --build

# Or run in background
docker-compose up -d --build
```

#### Production Mode
```bash
# Build and run in production mode with Gunicorn
docker-compose -f docker-compose.prod.yml up --build

# Or run in background
docker-compose -f docker-compose.prod.yml up -d --build
```

### 3. Access the Application

Open your browser and go to:
- **Development**: http://localhost:5000
- **Production**: http://localhost:5000

## Docker Commands

### Basic Docker Commands

```bash
# Build the image
docker build -t diet-workout-app .

# Run the container
docker run -p 5000:5000 --env-file .env diet-workout-app

# Run in background
docker run -d -p 5000:5000 --env-file .env --name diet-workout diet-workout-app

# Stop the container
docker stop diet-workout

# Remove the container
docker rm diet-workout

# View logs
docker logs diet-workout

# Execute commands in running container
docker exec -it diet-workout bash
```

### Docker Compose Commands

```bash
# Start services
docker-compose up

# Start services in background
docker-compose up -d

# Stop services
docker-compose down

# Rebuild and start
docker-compose up --build

# View logs
docker-compose logs

# View logs for specific service
docker-compose logs diet-workout-app

# Scale services (if needed)
docker-compose up --scale diet-workout-app=3
```

## Production Deployment

### Using Production Dockerfile

```bash
# Build production image
docker build -f Dockerfile.prod -t diet-workout-prod .

# Run production container
docker run -d -p 5000:5000 --env-file .env --name diet-workout-prod diet-workout-prod

# Or use production compose
docker-compose -f docker-compose.prod.yml up -d
```

### Production Features

- **Gunicorn WSGI Server**: Better performance and reliability
- **Multiple Workers**: Handles concurrent requests
- **Health Checks**: Automatic health monitoring
- **Resource Limits**: Memory and CPU constraints
- **Security**: Non-root user execution

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key | Yes |
| `FLASK_ENV` | Flask environment (development/production) | No |
| `FLASK_APP` | Flask application entry point | No |

## Volumes

- `./logs:/app/logs`: Application logs directory

## Networks

- `diet-workout-network`: Internal network for services

## Health Checks

The application includes health checks that:
- Check if the application is responding on port 5000
- Run every 30 seconds
- Retry 3 times before marking as unhealthy
- Start checking after 40 seconds

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Check what's using port 5000
   lsof -i :5000
   
   # Use different port
   docker run -p 5001:5000 --env-file .env diet-workout-app
   ```

2. **Environment Variables Not Loading**
   ```bash
   # Check if .env file exists
   ls -la .env
   
   # Pass environment variables directly
   docker run -p 5000:5000 -e GROQ_API_KEY=your_key diet-workout-app
   ```

3. **Container Won't Start**
   ```bash
   # Check container logs
   docker logs diet-workout-app
   
   # Run interactively for debugging
   docker run -it --env-file .env diet-workout-app bash
   ```

4. **Permission Issues**
   ```bash
   # Fix file permissions
   chmod 644 .env
   chmod -R 755 .
   ```

### Logs and Debugging

```bash
# View real-time logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f diet-workout-app

# Check container status
docker-compose ps

# Inspect container
docker inspect diet-workout-app
```

## Security Considerations

- The application runs as a non-root user
- Environment variables are properly managed
- Health checks prevent unhealthy containers from serving traffic
- Resource limits prevent resource exhaustion

## Performance Optimization

- Use production Dockerfile for better performance
- Adjust Gunicorn workers based on your CPU cores
- Monitor resource usage with `docker stats`
- Consider using Docker volumes for persistent data

## Scaling

```bash
# Scale to multiple instances
docker-compose up --scale diet-workout-app=3

# Use with load balancer
# (Add nginx or traefik configuration)
```

## Monitoring

```bash
# Monitor container resources
docker stats

# Check application health
curl http://localhost:5000/

# View application logs
docker-compose logs -f diet-workout-app
``` 