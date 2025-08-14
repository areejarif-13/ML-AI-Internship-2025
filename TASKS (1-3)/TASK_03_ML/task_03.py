#------------importing_libraries-----------
from google.genai import Client
import os
from dotenv import load_dotenv
#-----------Calling_API-----------------------
load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=Client(api_key=api_key)
#-----------Restricted_words------------------
safety_words = ["dosage", "death", "kill", "prescribe", "suicide", " self-harm", "overdose",
                "antibiotics without doctor","harm yourself","overdose"]
base_prompt = """
You are a compassionate and professional virtual health assistant with which user is asking a conversational questions about health problems and risk.
Your responsibilities:
1. Provide answers in clear, simple, and everyday language that anyone can understand.
2. Do NOT use any decorative symbols (e.g., ###, ***, emojis, or unusual punctuation).
3. Always include this safety disclaimer at the end of every response: 
   "This is general information, not medical advice."
4. Never provide exact medication dosages, prescriptions, or detailed treatment plans.
5. If suggesting possible causes or conditions, always instruct the user to consult a qualified healthcare professional.
6. If the user expresses thoughts of suicide or self-harm, immediately respond with empathy and include a relevant helpline number for their country (e.g., "If you are thinking about harming yourself, please seek help immediately. In the U.S., you can call or text 988. In the UK, Samaritans are available at 116 123.").
7. Ensure responses are well-structured, easy to read, and free of irregular symbols.
8.Format the output to fit in the terminal.
Tone: Supportive, calm, and trustworthy.
"""
print(f"===================================================\n"
                f"\t\t\tHealth Care Bot\n"
      f"===========(your health qury partner)===============\n")
flag=True
while flag:
    #--------------user_input-------------------------
    user_input=input("\n(for exit type 'exit' or press 0)"
                     "\n\tPlease enter your health question.\t"
                     "\nYou:")
    user_input=user_input.lower()
    #------------------------------feature#1
    if user_input=="exit" or user_input=="0":
        print("Exiting...\n"
              "Thank you for your health questions !\n"
              "Stay Health !! Goodbye unit next time\n")
        break
    #-----------------------------feature#2
    if any(word in user_input for word in safety_words):
        print("I cannot provide any further advice.\n"
              "Please consult medical professional.\n"
              "Thank you for your health questions !\n")
        continue
    #-----------------requesting model-----------------------
    prompt = base_prompt + "\n User:" + user_input
    response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
        )
#--------------model printing the output-----------------------
    print("__________________________________")
    print(f"Bot:{response.text}\n")
    print("__________________________________")
    flag=True
#--------------------end_of_program--------------->