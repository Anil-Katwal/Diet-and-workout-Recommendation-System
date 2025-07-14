# Diet and Workout Recommendation System

An AI-powered web application that provides personalized diet and workout recommendations based on user preferences, health conditions, and dietary restrictions.
https://diet-and-workout-recommendation-system-ls98.onrender.com

## Features

- **Restaurant Recommendations**: Personalized restaurant suggestions
- **Breakfast Options**: Healthy breakfast recommendations
- **Dinner Suggestions**: Nutritious dinner options
- **Workout Plans**: Tailored exercise recommendations
- **Personalized**: Based on age, gender, weight, height, dietary preferences, health conditions, and allergies
- **Regional**: Considers your geographical location for relevant suggestions

## Setup Instructions

### Option 1: Render Deployment (Recommended)

#### 1. Deploy to Render

1. Push your code to GitHub/GitLab
2. Go to [render.com](https://render.com) and create a new Web Service
3. Connect your repository
4. Set environment variable `GROQ_API_KEY` in Render dashboard
5. Deploy automatically

For detailed Render instructions, see [RENDER.md](RENDER.md).

### Option 2: Docker Deployment

#### 1. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

#### 2. Build and Run with Docker

**Development Mode:**
```bash
docker-compose up --build
```

**Production Mode:**
```bash
docker-compose -f docker-compose.prod.yml up --build
```

#### 3. Access the Application

Open your browser and go to `http://localhost:5000`

For detailed Docker instructions, see [DOCKER.md](DOCKER.md).

### Option 2: Local Development

#### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 2. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

#### 3. Run the Application

**Web Application:**
```bash
# Option 1: Use the startup script (recommended)
python run.py

# Option 2: Direct Flask run
python app.py
```

**Command Line Testing:**
```bash
python main.py
```

Then open your browser and go to `http://localhost:5000`

## Usage

1. **Fill out the form** with your personal information:
   - Age, gender, weight, height
   - Dietary preferences (vegetarian/non-vegetarian)
   - Health conditions and allergies
   - Preferred food types
   - Your region/location

2. **Submit the form** to get AI-generated recommendations

3. **View your personalized recommendations** for:
   - 6 restaurant suggestions
   - 6 breakfast options
   - 5 dinner choices
   - 6 workout plans

## Project Structure

```
├── app.py                    # Flask web application
├── main.py                  # Command-line testing script
├── ai_recommendation.py     # Shared AI recommendation logic
├── run.py                   # Smart startup script
├── wsgi.py                  # WSGI entry point for production
├── templates/               # Flask templates
│   ├── index.html           # User input form
│   └── result.html          # Results display page
├── requirements.txt         # Python dependencies
├── render.yaml              # Render deployment configuration
├── render-start.sh          # Render startup script
├── requirements-render.txt  # Render-specific requirements
├── Dockerfile               # Development Docker configuration
├── Dockerfile.prod          # Production Docker configuration
├── docker-compose.yml       # Development Docker Compose
├── docker-compose.prod.yml  # Production Docker Compose
├── .dockerignore            # Docker ignore file
├── DOCKER.md                # Docker deployment guide
├── RENDER.md                # Render deployment guide
└── README.md                # Documentation
```

## Technical Details

- **AI Model**: Groq's Llama3-70b-8192
- **Framework**: Flask (Python)
- **Frontend**: Bootstrap 4
- **AI Integration**: LangChain with Groq

## Error Handling

The application includes comprehensive error handling for:
- Missing API keys
- Invalid form data
- AI service failures
- Network issues

## Troubleshooting

### Watchdog Import Error
If you see an error like `ImportError: cannot import name 'EVENT_TYPE_OPENED'`, this is a compatibility issue between Flask and Watchdog. The startup script (`run.py`) automatically handles this by falling back to non-debug mode.

### Missing Dependencies
If you get import errors, make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### API Key Issues
Make sure your `.env` file contains a valid Groq API key:
```bash
GROQ_API_KEY=your_actual_api_key_here
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
