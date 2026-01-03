# Medical Awareness AI Chatbot (Tamil and English)

Live Application: https://medical-chatbot-uhs3.onrender.com/

## Overview
This project is a full-stack, AI-powered medical awareness chatbot designed to provide basic health guidance, symptom awareness, and preventive advice through natural conversation. The system supports both Tamil and English languages and includes voice input and voice output functionality. It is fully mobile-responsive and deployed online using Render.

The chatbot is built with ethical AI principles and is intended strictly for educational and awareness purposes. It does not diagnose diseases or replace professional medical consultation.

---

## Problem Statement
Access to reliable medical awareness remains limited for many users, particularly those who prefer regional languages or voice-based interaction. Many existing solutions are text-only, English-centric, or not optimized for mobile usage.

This project addresses these challenges by delivering a multilingual, voice-enabled, mobile-friendly AI chatbot that provides safe and accessible medical awareness information.

---

## Key Features
- AI-powered conversational responses using Groq LLaMA 3.1
- Tamil and English language support
- Voice input using browser speech recognition
- Voice output using text-to-speech
- Stop speech functionality for better user control
- Typing and speaking indicators for improved user experience
- Dark mode interface
- Persistent chat history on the client side
- Secure admin login system
- Mobile-responsive and cross-device compatible
- Deployed online with HTTPS support

---

## Technology Stack

Frontend:
- HTML
- CSS
- JavaScript (Web Speech API)

Backend:
- Python
- Flask

AI Model:
- Groq LLaMA 3.1

Deployment:
- Render (Web Service)

Version Control:
- Git and GitHub

---

## System Architecture
1. The user interacts with the chatbot using text or voice input.
2. The frontend sends the processed input to the Flask backend.
3. The backend constructs a prompt and sends it to the Groq AI model.
4. The AI model generates a response focused on medical awareness.
5. The response is returned to the frontend, displayed as text, and spoken aloud if voice output is enabled.

---

## Project Structure
medical-chatbot/ │ ├── app.py ├── requirements.txt ├── disease.json │ ├── templates/ │   ├── index.html │   ├── login.html │   └── admin.html │ └── static/ └── style.css

---

## Environment Variables
The application uses environment variables for secure API key management.

Required variable:
GROQ_API_KEY = your_groq_api_key
---

## Deployment
The application is deployed on Render as a web service using Gunicorn. The deployment setup includes secure environment variable handling and HTTPS support, enabling microphone and speech features across devices.

Live URL:
https://medical-chatbot-uhs3.onrender.com/

---

## Security and Ethical Considerations
- The chatbot does not provide medical diagnosis or treatment
- Clear medical disclaimer is presented to users
- API keys are secured using environment variables
- No sensitive user data is stored or shared
- Designed with ethical AI usage principles in healthcare

---

## Resume Value
This project demonstrates the following skills and competencies:
- Full-stack web development using Python and Flask
- Integration of large language models via APIs
- Multilingual application design
- Voice-based user interaction using browser APIs
- Secure deployment and environment configuration
- Ethical application of AI in the healthcare domain

---

## Future Enhancements
- Database-backed chat history storage
- Analytics dashboard for usage insights
- Role-based user authentication
- Progressive Web App support
- Doctor and hospital recommendation module
- Enhanced admin controls for medical content management

---

## Author
Suraj  
AI and Full-Stack Developer  
India

---

## License
This project is open-source and intended for educational and demonstration purposes only.
