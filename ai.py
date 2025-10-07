from google import genai
import speech_recognition as sr
import pyttsx3
import pyaudio


client = genai.Client(api_key= "AIzaSyAfOq7WgsWnTtqKCeBa9EiA7fsyfyG62qI")
# function to interact with AI chatbot

def aichatbot(prompt):
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents = prompt, 
    )
    print(response.text)
# main function to record text
def recordtext():
    case = True
    while(case):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        case = False
# main loop
if __name__ == "__main__":
    while(True):
        text = recordtext()
        aichatbot(text)
        #command = input("Do you want to continue? (yes/no): ").strip().lower()
        #if command != 'yes':
        #    break   
