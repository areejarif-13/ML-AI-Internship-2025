# General Health Query Chatbot 🤖

##  Task Objective
The objective of this project was to create a chatbot capable of answering general health-related questions using a Large Language Model (LLM). The chatbot:
- Provides clear, layman-friendly responses.
- Maintains a professional yet supportive tone.
- Includes safety disclaimers.
- Avoids giving harmful or unsafe medical advice.

---

##  Dataset Used
No custom dataset was used. The chatbot leverages Google's **Gemini 2.5 Flash** model for real-time responses, using carefully engineered prompts to ensure safe and user-friendly output.

---

##  Models Applied
- **Google Gemini 2.5 Flash**
  - API: `google.genai`
  - Reason: Fast response time and ability to follow complex prompts reliably.

---

##  Key Results and Findings
- Successfully integrated Gemini API into a Python conversational loop.
- Implemented safety filters to detect and restrict harmful or sensitive medical topics.
- Ensured all answers include a safety disclaimer.
- The chatbot provides relevant, clear, and supportive responses for general health-related questions.
- API key security is maintained using environment variables for safe deployment.

---

