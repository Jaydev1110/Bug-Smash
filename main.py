#AIzaSyDQpr_GRBee7jU2_LcS-WadPR8Z8hhF7zg

# hii i am naiteek, and i just contributed to  your repo

# Import necessary libraries
import google.generativeai as genai  # Google's Gemini AI SDK
import pyttsx3  # Text-to-Speech conversion
import time  # For synchronizing printing speed with speech

# Configure Gemini AI with API key (Replace with your actual key)
genai.configure(api_key="Your_API_KEY")

def get_gemini_response(prompt):
    """
    Fetches a response from Google's Gemini AI based on the given prompt.
    
    Parameters:
        prompt (str): The user-provided input query for the AI model.
        
    Returns:
        str: The generated response from Gemini AI.
    """
    # Initialize the Gemini AI model (using an available model)
    model = genai.GenerativeModel("gemini-1.5-pro")  # Use the correct model name
    
    # Generate content based on the user's prompt
    response = model.generate_content(prompt)
    
    # Return the AI response text
    return response.text if response else "No response from AI."

def type_and_speak_synchronized(text):
    """
    Prints text with human-like typing speed and synchronizes speech with typing.
    
    Parameters:
        text (str): The text to be printed with typing simulation and synchronized speech.
    """
    import random
    import threading
    
    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Increased from 130 to 140 for slightly faster speech
    
    # Base typing speed (seconds per character)
    base_speed = 0.05           #0.03
    
    # Create a flag to control speech timing
    speech_started = threading.Event()
    
    def speak_text():
        speech_started.wait()  # Wait for typing to start
        engine.say(text)
        engine.runAndWait()
    
    # Start speech in a separate thread
    speech_thread = threading.Thread(target=speak_text)
    speech_thread.start()
    
    # Display text with human-like typing speed
    for char in text:
        # Add natural variation to typing speed
        if char in '.!?':  # Longer pause after sentence endings
            delay = base_speed * 3
        elif char in ',;':  # Medium pause after punctuation
            delay = base_speed * 2
        elif char == ' ':  # Slight pause for spaces
            delay = base_speed * 1.5
        else:
            # Random variation in typing speed
            delay = base_speed * random.uniform(0.8, 1.2)
        
        # Start speech after first character
        if not speech_started.is_set():
            speech_started.set()
        
        print(char, end='', flush=True)
        time.sleep(delay)
    
    # Wait for speech to complete
    speech_thread.join()

def speak_and_display(text):
    """
    Converts AI-generated text into speech and synchronizes it with the display.

    Parameters:
        text (str): The text response to be spoken and displayed.
    """
    print("\nAI Response:\n")
    
    # Display text with human-like typing speed and synchronized speech
    type_and_speak_synchronized(text)
    print("\n")

# Main execution
if __name__ == "__main__":
    # Get user input
    user_prompt = input("Enter your prompt: ")

    # Fetch AI-generated response
    ai_response = get_gemini_response(user_prompt)

    # Call function to speak and display the response
    speak_and_display(ai_response)

