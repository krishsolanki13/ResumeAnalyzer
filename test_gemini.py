from app import utils
import google.generativeai as genai

# Configure Gemini with API key from utils
genai.configure(api_key=utils.GEMINI_API_KEY)

try:
    # Use a supported model (fast and cheap)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    # Test the model
    response = model.generate_content("Convert this to french - Hello I am Krish")
    print("Gemini Response:")
    print(response.text)

except Exception as e:
    print("Error communicating with Gemini:")
    print(e)
