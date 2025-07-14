from ai_recommendation import DietWorkoutRecommender

def main():
    try:
        # Initialize the recommender
        recommender = DietWorkoutRecommender()
        
        # Input data for testing
        input_data = {
            'age': 60,
            'gender': 'male',
            'weight': 120,
            'height': 5,
            'veg_or_nonveg': 'veg',
            'disease': 'aneamia',
            'region': 'Nepal',
            'allergics': 'Latex Allergy',
            'foodtype': 'Fruits'
        }
        
        # Get recommendations
        results = recommender.get_recommendations(input_data)
        
        # Print final output
        print("Recommended Restaurants:", results['restaurant_names'])
        print("Recommended Breakfasts:", results['breakfast_names'])
        print("Recommended Dinners:", results['dinner_names'])
        print("Recommended Workouts:", results['workout_names'])
        
    except ValueError as e:
        print(f"Error: {e}")
        print("Please make sure you have set the GROQ_API_KEY environment variable.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
