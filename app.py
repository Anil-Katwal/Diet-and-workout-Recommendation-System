from flask import Flask, render_template, request, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For flash messages

# Initialize the recommender
recommender = None
try:
    from ai_recommendation import DietWorkoutRecommender
    recommender = DietWorkoutRecommender()
except Exception as e:
    print(f"Initialization error: {e}")
    print("Running in demo mode without AI recommendations")
    recommender = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == "POST":
        try:
            # Check if recommender is available
            if recommender is None:
                flash("AI service is not available. Please check your API key configuration.", "error")
                return render_template('index.html')
            
            # Get form data
            age = request.form.get('age')
            gender = request.form.get('gender')
            weight = request.form.get('weight')
            height = request.form.get('height')
            veg_or_nonveg = request.form.get('veg_or_nonveg')
            disease = request.form.get('disease')
            region = request.form.get('region')
            allergics = request.form.get('allergics')
            foodtype = request.form.get('foodtype')
            
            # Validate required fields
            if not all([age, gender, weight, height, veg_or_nonveg, disease, region, allergics, foodtype]):
                flash("Please fill in all required fields.", "error")
                return render_template('index.html')
            
            # Prepare input data
            input_data = {
                'age': age,
                'gender': gender,
                'weight': weight,
                'height': height,
                'veg_or_nonveg': veg_or_nonveg,
                'disease': disease,
                'region': region,
                'allergics': allergics,
                'foodtype': foodtype
            }
            
            # Get recommendations
            if recommender is None:
                # Provide demo data
                flash("Running in demo mode. Here are sample recommendations.", "info")
                results = {
                    'restaurant_names': ['Demo Restaurant 1', 'Demo Restaurant 2', 'Demo Restaurant 3'],
                    'breakfast_names': ['Demo Breakfast 1', 'Demo Breakfast 2', 'Demo Breakfast 3'],
                    'dinner_names': ['Demo Dinner 1', 'Demo Dinner 2', 'Demo Dinner 3'],
                    'workout_names': ['Demo Workout 1', 'Demo Workout 2', 'Demo Workout 3']
                }
            else:
                results = recommender.get_recommendations(input_data)
            
            # Check if we got any recommendations
            if not any(results.values()):
                # Provide demo data if AI is not available
                if recommender is None:
                    flash("Running in demo mode. Here are sample recommendations.", "info")
                    results = {
                        'restaurant_names': ['Demo Restaurant 1', 'Demo Restaurant 2', 'Demo Restaurant 3'],
                        'breakfast_names': ['Demo Breakfast 1', 'Demo Breakfast 2', 'Demo Breakfast 3'],
                        'dinner_names': ['Demo Dinner 1', 'Demo Dinner 2', 'Demo Dinner 3'],
                        'workout_names': ['Demo Workout 1', 'Demo Workout 2', 'Demo Workout 3']
                    }
                else:
                    flash("Unable to generate recommendations. Please try again.", "warning")
                    return render_template('index.html')
            
            return render_template(
                'result.html',
                restaurant_names=results['restaurant_names'],
                breakfast_names=results['breakfast_names'],
                dinner_names=results['dinner_names'],
                workout_names=results['workout_names']
            )
            
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "error")
            return render_template('index.html')

    return render_template('index.html')


if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0', port=8000)
    except ImportError as e:
        if "EVENT_TYPE_OPENED" in str(e):
            print("Watchdog compatibility issue detected. Running without debug mode...")
            app.run(debug=False, host='0.0.0.0', port=8000)
        else:
            raise e
