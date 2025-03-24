import google.generativeai as genai
from config import GEMINI_API_KEY
import PIL.Image

def get_response(prompt, image_path):
    # Configure Gemini API with the API key
    genai.configure(api_key=GEMINI_API_KEY)
    img = PIL.Image.open(image_path)
    # import pprint
    # for model in genai.list_models():
    #     pprint.pprint(model)

    

    # Create a model instance that supports vision
    # model = genai.GenerativeModel("gemini-pro-vision")

    model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-1219")


    # Send image along with the text prompt
    response = model.generate_content([prompt, img])

    return response.text

# Example Usage


# response = get_response('screenshot.png')
# print(response)



