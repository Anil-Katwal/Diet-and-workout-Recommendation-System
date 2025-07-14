# Render Deployment Guide

This guide explains how to deploy the Diet and Workout Recommendation System on Render.

## Prerequisites

- Render account (free tier available)
- Groq API key
- Git repository with your code

## Quick Deployment

### 1. Prepare Your Repository

Make sure your repository contains these files:
- `render.yaml` - Render configuration
- `requirements.txt` - Python dependencies
- `wsgi.py` - WSGI entry point
- `render-start.sh` - Startup script
- All application files

### 2. Connect to Render

1. Go to [render.com](https://render.com) and sign up/login
2. Click "New +" and select "Web Service"
3. Connect your GitHub/GitLab repository
4. Select the repository containing your code

### 3. Configure the Service

Render will automatically detect the `render.yaml` configuration:

```yaml
services:
  - type: web
    name: diet-workout-recommendation
    env: python
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: chmod +x render-start.sh && ./render-start.sh
    envVars:
      - key: PYTHON_VERSION
        value: 3.9.16
      - key: GROQ_API_KEY
        sync: false
    healthCheckPath: /
    autoDeploy: true
```

### 4. Set Environment Variables

In the Render dashboard:
1. Go to your service settings
2. Navigate to "Environment" tab
3. Add the following environment variable:
   - **Key**: `GROQ_API_KEY`
   - **Value**: Your Groq API key
   - **Sync**: Disabled (for security)

### 5. Deploy

1. Click "Create Web Service"
2. Render will automatically build and deploy your application
3. Wait for the build to complete (usually 2-5 minutes)

### 6. Access Your Application

Once deployed, you'll get a URL like:
`https://diet-workout-recommendation.onrender.com`

## Manual Configuration (Alternative)

If you prefer manual configuration instead of `render.yaml`:

### Build Command
```bash
pip install -r requirements.txt
```

### Start Command
```bash
gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 wsgi:app
```

### Environment Variables
- `GROQ_API_KEY`: Your Groq API key

## Configuration Details

### Service Settings

- **Environment**: Python
- **Region**: Choose closest to your users
- **Branch**: main (or your preferred branch)
- **Root Directory**: Leave empty (if code is in root)
- **Auto-Deploy**: Enabled (deploys on every push)

### Build Settings

- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `chmod +x render-start.sh && ./render-start.sh`

### Environment Variables

| Variable | Description | Required | Sync |
|----------|-------------|----------|------|
| `GROQ_API_KEY` | Your Groq API key | Yes | No |
| `PYTHON_VERSION` | Python version | No | Yes |

## Monitoring and Logs

### View Logs
1. Go to your service in Render dashboard
2. Click "Logs" tab
3. View real-time application logs

### Health Checks
- **Path**: `/`
- **Interval**: 30 seconds
- **Timeout**: 10 seconds

## Troubleshooting

### Common Issues

1. **Build Failures**
   ```bash
   # Check requirements.txt syntax
   pip install -r requirements.txt
   
   # Verify Python version compatibility
   python --version
   ```

2. **Environment Variables**
   - Ensure `GROQ_API_KEY` is set in Render dashboard
   - Check that the variable name is exactly correct
   - Verify the API key is valid

3. **Application Won't Start**
   - Check logs in Render dashboard
   - Verify `wsgi.py` exists and is correct
   - Ensure all dependencies are in `requirements.txt`

4. **Health Check Failures**
   - Verify the application responds on `/`
   - Check if the application is binding to `0.0.0.0:$PORT`
   - Review application logs for errors

### Debug Commands

```bash
# Test locally with same environment
export PORT=5000
export GROQ_API_KEY=your_key_here
gunicorn --bind 0.0.0.0:$PORT wsgi:app

# Check if all dependencies are installed
pip list

# Test the application
curl http://localhost:5000/
```

## Performance Optimization

### Free Tier Limitations
- **Build Time**: 15 minutes
- **Request Timeout**: 30 seconds
- **Sleep Mode**: After 15 minutes of inactivity

### Optimization Tips
1. **Minimize Dependencies**: Only include necessary packages
2. **Use Specific Versions**: Pin dependency versions in requirements.txt
3. **Optimize Images**: Use smaller base images if using Docker
4. **Caching**: Implement proper caching strategies

## Scaling

### Free Tier
- Single instance
- Automatic sleep/wake
- Limited resources

### Paid Plans
- Multiple instances
- Always-on service
- More resources
- Custom domains

## Security

### Best Practices
1. **Environment Variables**: Never commit API keys to code
2. **HTTPS**: Render provides automatic HTTPS
3. **Dependencies**: Keep dependencies updated
4. **Logs**: Monitor logs for security issues

### API Key Security
- Store `GROQ_API_KEY` as environment variable
- Enable "Sync" to false for sensitive data
- Rotate API keys regularly
- Use least privilege principle

## Custom Domain

1. Go to service settings
2. Navigate to "Custom Domains"
3. Add your domain
4. Configure DNS records as instructed
5. Wait for SSL certificate (automatic)

## Backup and Recovery

### Code Backup
- Use Git for version control
- Push to multiple remotes
- Regular commits and tags

### Data Backup
- Export environment variables
- Document configuration
- Keep deployment scripts

## Support

### Render Support
- [Render Documentation](https://render.com/docs)
- [Render Community](https://community.render.com)
- [Render Status](https://status.render.com)

### Application Support
- Check application logs
- Review error messages
- Test locally first 