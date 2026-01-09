📘 StudySense AI

StudySense AI is a browser-based AI-powered study assistant that helps students study smarter by identifying weak concepts and recommending targeted practice questions.

Instead of revising everything blindly, StudySense AI analyzes student mistakes and provides personalized feedback so learners can focus on what actually needs improvement.

🚀 What It Does

Displays practice questions to students

Accepts user answers in real time

Checks correctness instantly

Uses AI to analyze incorrect answers

Identifies weak concepts

Suggests follow-up practice questions with explanations

🧠 Why StudySense AI?

Many students struggle not because they don’t study enough, but because they don’t know what to study.
StudySense AI solves this by guiding students toward their weak areas instead of wasting time on concepts they already understand.

This project aims to make learning more efficient, personalized, and less overwhelming.

🛠️ Built With

Python

Flask

HTML

CSS

JavaScript

OpenAI API

JSON

⚙️ How It Works

The student answers a practice question

The backend checks if the answer is correct

If incorrect, the response is sent to an AI tutor

The AI identifies the weak concept

A short explanation and a new practice question are generated

Feedback is shown instantly without page reload

📂 Project Structure
StudySense-AI/
│
├── app.py
├── questions.json
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js

▶️ How to Run Locally

Clone the repository:

git clone https://github.com/your-username/StudySense-AI.git


Navigate to the project directory:

cd StudySense-AI


Install dependencies:

pip install -r requirements.txt


Set your OpenAI API key as an environment variable:

Windows

setx OPENAI_API_KEY "your_api_key_here"


Mac / Linux

export OPENAI_API_KEY="your_api_key_here"


Run the application:

python app.py


Open your browser and visit:

http://localhost:5000

🎥 Demo

A short demo video is included in the Devpost submission, showing:

Answer submission

AI feedback generation

Personalized recommendations

🔮 Future Improvements

Support for multiple subjects

Tracking student progress over time

Personalized difficulty adjustment

Teacher and student dashboards

🏁 Hackathon Submission

This project was built during AlamedaHacks as part of the Machine Learning / AI track.

All code was written during the hackathon period.

🔒 Security Note

For security reasons, API keys are never included in the codebase and are managed using environment variables.
