#AIzaSyDQpr_GRBee7jU2_LcS-WadPR8Z8hhF7zg

# hii i am naiteek, and i just contributed to  your repo

# well it's nice to  know  you brother
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

# # /// commit new/////
# # AIzaSyBYRuFPTpVeVw7F1OUWBbd2IJ-9DkbepaI
# import openai
# import json
# import os
# import pyttsx3
# import time
# import random
# import threading
# from typing import List, Dict, Any
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Configuration
# CONFIG = {
#     "api_key": os.getenv("OPENAI_API_KEY"),
#     "model_name": "gpt-4o-mini",  # Using GPT-4o-mini model
#     "history_file": "conversation_history.json",
#     "system_prompt": """You are an exceptional personal teacher. Your characteristics:
# - Adapt explanations to the student's learning style
# - Maintain detailed context of all previous interactions
# - Provide clear examples and analogies
# - Identify knowledge gaps and suggest practice
# - Encourage critical thinking and questions
# - Correct mistakes gently with detailed feedback"""
# }

# def validate_config() -> None:
#     """Validate configuration settings."""
#     if not CONFIG["api_key"]:
#         raise ValueError("OPENAI_API_KEY environment variable is not set")
#     if not os.path.exists(CONFIG["history_file"]):
#         with open(CONFIG["history_file"], "w") as f:
#             json.dump([], f)

# # Initialize OpenAI client
# try:
#     client = openai.OpenAI(api_key=CONFIG['api_key'])
# except Exception as e:
#     print(f"Error initializing OpenAI: {str(e)}")
#     exit(1)

# def load_history() -> List[Dict[str, Any]]:
#     """Load conversation history with error handling."""
#     try:
#         if os.path.exists(CONFIG['history_file']):
#             with open(CONFIG['history_file'], 'r') as f:
#                 return json.load(f)
#         return []
#     except Exception as e:
#         print(f"Error loading history: {str(e)}")
#         return []

# def save_history(history: List[Dict[str, Any]]) -> None:
#     """Save conversation history with error handling."""
#     try:
#         with open(CONFIG['history_file'], 'w') as f:
#             json.dump(history, f, indent=2)
#     except Exception as e:
#         print(f"Error saving history: {str(e)}")

# def type_and_speak_synchronized(text: str) -> None:
#     """
#     Prints text with human-like typing speed and synchronizes speech with typing.
    
#     Parameters:
#         text (str): The text to be printed with typing simulation and synchronized speech.
#     """
#     # Initialize text-to-speech engine
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)  # Speech rate
    
#     # Base typing speed (seconds per character)
#     base_speed = 0.05
    
#     # Create a flag to control speech timing
#     speech_started = threading.Event()
    
#     def speak_text():
#         speech_started.wait()  # Wait for typing to start
#         engine.say(text)
#         engine.runAndWait()
    
#     # Start speech in a separate thread
#     speech_thread = threading.Thread(target=speak_text)
#     speech_thread.start()
    
#     # Display text with human-like typing speed
#     for char in text:
#         # Add natural variation to typing speed
#         if char in '.!?':  # Longer pause after sentence endings
#             delay = base_speed * 3
#         elif char in ',;':  # Medium pause after punctuation
#             delay = base_speed * 2
#         elif char == ' ':  # Slight pause for spaces
#             delay = base_speed * 1.5
#         else:
#             # Random variation in typing speed
#             delay = base_speed * random.uniform(0.8, 1.2)
        
#         # Start speech after first character
#         if not speech_started.is_set():
#             speech_started.set()
        
#         print(char, end='', flush=True)
#         time.sleep(delay)
    
#     # Wait for speech to complete
#     speech_thread.join()

# def handle_response(user_input: str) -> str:
#     """Handle user input and generate response."""
#     try:
#         if not user_input.strip():
#             return "Please provide a valid input."
            
#         # Create messages list with system prompt and conversation history
#         messages = [
#             {"role": "system", "content": CONFIG['system_prompt']}
#         ]
        
#         # Add conversation history
#         for msg in chat_history:
#             messages.append(msg)
            
#         # Add current user input
#         messages.append({"role": "user", "content": user_input})
        
#         # Get response from OpenAI
#         response = client.chat.completions.create(
#             model=CONFIG['model_name'],
#             messages=messages,
#             stream=True
#         )
        
#         full_response = []
#         print("Tutor: ", end='', flush=True)
        
#         for chunk in response:
#             if chunk.choices[0].delta.content is not None:
#                 content = chunk.choices[0].delta.content
#                 print(content, end='', flush=True)
#                 full_response.append(content)
        
#         # Save the new message to history
#         chat_history.append({"role": "user", "content": user_input})
#         chat_history.append({"role": "assistant", "content": ''.join(full_response)})
#         save_history(chat_history)
        
#         # Convert the response to speech
#         response_text = ''.join(full_response)
#         type_and_speak_synchronized(response_text)
        
#         return response_text
    
#     except Exception as e:
#         save_history(chat_history)
#         return f"Error: {str(e)}"

# def main() -> None:
#     """Main function to run the tutor."""
#     try:
#         validate_config()
#         global chat_history
#         chat_history = load_history()
        
#         print("Personal Tutor: Hello! Let's continue our learning journey. (Type 'exit' to quit)")
#         while True:
#             try:
#                 user_input = input("\nYou: ")
#                 if user_input.lower() in ('exit', 'quit'):
#                     print("Goodbye! Have a great day!")
#                     break
                
#                 handle_response(user_input)
#                 print()
                
#             except KeyboardInterrupt:
#                 print("\nGoodbye! Have a great day!")
#                 break
#             except Exception as e:
#                 print(f"\nAn error occurred: {str(e)}")
#                 continue
                
#     except Exception as e:
#         print(f"Fatal error: {str(e)}")
#         exit(1)

# if __name__ == "__main__":
#     main()

# # #AIzaSyDQpr_GRBee7jU2_LcS-WadPR8Z8hhF7zg

# # # hii i am naiteek, and i just contributed to  your repo

# # # well it's nice to  know  you brother
# # # Import necessary libraries
# # import google.generativeai as genai  # Google's Gemini AI SDK
# # import pyttsx3  # Text-to-Speech conversion
# # import time  # For synchronizing printing speed with speech

# # # Configure Gemini AI with API key (Replace with your actual key)
# # genai.configure(api_key="AIzaSyDQpr_GRBee7jU2_LcS-WadPR8Z8hhF7zg")

# # def get_gemini_response(prompt):
# #     """
# #     Fetches a response from Google's Gemini AI based on the given prompt.
    
# #     Parameters:
# #         prompt (str): The user-provided input query for the AI model.
        
# #     Returns:
# #         str: The generated response from Gemini AI.
# #     """
# #     # Initialize the Gemini AI model (using an available model)
# #     model = genai.GenerativeModel("gemini-1.5-pro")  # Use the correct model name
    
# #     # Generate content based on the user's prompt
# #     response = model.generate_content(prompt)
    
# #     # Return the AI response text
# #     return response.text if response else "No response from AI."

# # def type_and_speak_synchronized(text):
# #     """
# #     Prints text with human-like typing speed and synchronizes speech with typing.
    
# #     Parameters:
# #         text (str): The text to be printed with typing simulation and synchronized speech.
# #     """
# #     import random
# #     import threading
    
# #     # Initialize text-to-speech engine
# #     engine = pyttsx3.init()
# #     engine.setProperty('rate', 150)  # Increased from 130 to 140 for slightly faster speech
    
# #     # Base typing speed (seconds per character)
# #     base_speed = 0.05           #0.03
    
# #     # Create a flag to control speech timing
# #     speech_started = threading.Event()
    
# #     def speak_text():
# #         speech_started.wait()  # Wait for typing to start
# #         engine.say(text)
# #         engine.runAndWait()
    
# #     # Start speech in a separate thread
# #     speech_thread = threading.Thread(target=speak_text)
# #     speech_thread.start()
    
# #     # Display text with human-like typing speed
# #     for char in text:
# #         # Add natural variation to typing speed
# #         if char in '.!?':  # Longer pause after sentence endings
# #             delay = base_speed * 3
# #         elif char in ',;':  # Medium pause after punctuation
# #             delay = base_speed * 2
# #         elif char == ' ':  # Slight pause for spaces
# #             delay = base_speed * 1.5
# #         else:
# #             # Random variation in typing speed
# #             delay = base_speed * random.uniform(0.8, 1.2)
        
# #         # Start speech after first character
# #         if not speech_started.is_set():
# #             speech_started.set()
        
# #         print(char, end='', flush=True)
# #         time.sleep(delay)
    
# #     # Wait for speech to complete
# #     speech_thread.join()

# # def speak_and_display(text):
# #     """
# #     Converts AI-generated text into speech and synchronizes it with the display.

# #     Parameters:
# #         text (str): The text response to be spoken and displayed.
# #     """
# #     print("\nAI Response:\n")
    
# #     # Display text with human-like typing speed and synchronized speech
# #     type_and_speak_synchronized(text)
# #     print("\n")

# # # Main execution
# # if __name__ == "__main__":
# #     # Get user input
# #     user_prompt = input("Enter your prompt: ")

# #     # Fetch AI-generated response
# #     ai_response = get_gemini_response(user_prompt)

# #     # Call function to speak and display the response
# #     speak_and_display(ai_response)

