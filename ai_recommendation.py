import os
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

class DietWorkoutRecommender:
    def __init__(self):
        # Check if API key is available
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable is required. Please set it in your .env file.")
        
        # Initialize Groq model
        self.llm = ChatGroq(
            temperature=0.6,
            api_key=api_key,
            model_name="llama3-70b-8192"
        )
        
        # Define prompt template
        self.prompt_template = PromptTemplate(
            input_variables=['age', 'gender', 'weight', 'height', 'veg_or_nonveg', 'disease', 'region', 'allergics', 'foodtype'],
            template=(
                "Diet Recommendation System:\n"
                "I want you to recommend 6 restaurant names, 6 breakfast names, 5 dinner names, and 6 workout names, "
                "based on the following criteria:\n"
                "Person age: {age}\n"
                "Person gender: {gender}\n"
                "Person weight: {weight}\n"
                "Person height: {height}\n"
                "Person veg_or_nonveg: {veg_or_nonveg}\n"
                "Person generic disease: {disease}\n"
                "Person region: {region}\n"
                "Person allergics: {allergics}\n"
                "Person foodtype: {foodtype}.\n"
                "Respond in the format:\n"
                "Restaurants:\n- ...\nBreakfast:\n- ...\nDinner:\n- ...\nWorkouts:\n- ..."
            )
        )
        
        # Create chain
        self.chain = self.prompt_template | self.llm
    
    def get_recommendations(self, input_data):
        """
        Get recommendations based on user input data.
        
        Args:
            input_data (dict): Dictionary containing user preferences
            
        Returns:
            dict: Dictionary with restaurant_names, breakfast_names, dinner_names, workout_names
        """
        try:
            # Validate input data
            required_fields = ['age', 'gender', 'weight', 'height', 'veg_or_nonveg', 'disease', 'region', 'allergics', 'foodtype']
            for field in required_fields:
                if field not in input_data or not input_data[field]:
                    raise ValueError(f"Missing required field: {field}")
            
            # Get AI response
            results = self.chain.invoke(input_data)
            
            # Extract and clean results
            restaurant_names = self._extract_section("Restaurants", "Breakfast", results.content)
            breakfast_names = self._extract_section("Breakfast", "Dinner", results.content)
            dinner_names = self._extract_section("Dinner", "Workouts", results.content)
            workout_names = self._extract_last_section("Workouts", results.content)
            
            return {
                'restaurant_names': restaurant_names,
                'breakfast_names': breakfast_names,
                'dinner_names': dinner_names,
                'workout_names': workout_names
            }
            
        except Exception as e:
            print(f"Error getting recommendations: {str(e)}")
            return {
                'restaurant_names': [],
                'breakfast_names': [],
                'dinner_names': [],
                'workout_names': []
            }
    
    def _extract_section(self, start, end, text):
        """Extract section between start and end markers."""
        pattern = rf'{start}:\s*(.*?)\s*{end}:'
        matches = re.findall(pattern, text, re.DOTALL)
        return self._clean_list(matches)
    
    def _extract_last_section(self, start, text):
        """Extract the last section starting with the given marker."""
        pattern = rf'{start}:\s*(.*)'
        matches = re.findall(pattern, text, re.DOTALL)
        return self._clean_list(matches)
    
    def _clean_list(self, raw_list):
        """Clean and format the extracted list."""
        if not raw_list:
            return []
        
        cleaned = []
        lines = raw_list[0].strip().split('\n')
        for line in lines:
            cleaned_line = line.strip("-• ").strip()
            if cleaned_line:
                cleaned.append(cleaned_line)
        
        return cleaned 