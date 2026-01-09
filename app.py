from flask import Flask, render_template, request, jsonify
import json
import os
import openai

app = Flask(__name__)

# =========================
# CONFIG
# =========================
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load questions
with open("questions.json", "r") as f:
    QUESTIONS = json.load(f)


# =========================
# ROUTES
# =========================

@app.route("/")
def index():
    """
    Home page – sends first question to frontend
    """
    return render_template("index.html", question=QUESTIONS[0])


@app.route("/submit", methods=["POST"])
def submit():
    """
    Receives student answer, checks correctness,
    and runs AI analysis if incorrect
    """
    user_answer = request.form.get("answer", "").strip()
    question_data = QUESTIONS[0]

    correct_answer = question_data["answer"]
    topic = question_data["topic"]
    question_text = question_data["question"]

    # Correct answer case
    if user_answer.lower() == correct_answer.lower():
        return jsonify({
            "status": "correct",
            "feedback": "✅ Correct! You’ve mastered this concept."
        })

    # Incorrect → AI analysis
    ai_feedback = analyze_with_ai(
        question_text,
        correct_answer,
        user_answer,
        topic
    )

    return jsonify({
        "status": "incorrect",
        "feedback": ai_feedback
    })


# =========================
# AI LOGIC
# =========================

def analyze_with_ai(question, correct_answer, student_answer, topic):
    """
    Uses AI to identify weak concept and suggest practice
    """

    prompt = f"""
You are an AI tutor.

A student answered a question incorrectly.

Question: {question}
Topic: {topic}
Correct Answer: {correct_answer}
Student Answer: {student_answer}

Tasks:
1. Identify the weak concept in simple terms.
2. Give a short explanation.
3. Suggest ONE new practice question.

Keep the response concise and student-friendly.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )

        return response.choices[0].message.content

    except Exception as e:
        return "⚠️ AI analysis failed. Please try again."


# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(debug=True)
