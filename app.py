from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Responses dictionary with additional emotions
responses = {
    "sad": "Take a moment to acknowledge your feelings. Maybe listen to uplifting music or talk to a friend.",
    "anxious": "Focus on your breathing or try grounding exercises. Small breaks can help clear your mind.",
    "nervous": "Visualize a positive outcome. Prepare thoroughly and remind yourself you can handle it!",
    "stressed": "Try relaxing activities like stretching or taking a walk outside to refresh your mind.",
    "unmotivated": "Break tasks into smaller steps. Celebrate small wins to boost your energy!",
    "anger": "Step away and count to 10. Try journaling or expressing your feelings constructively.",
    "fear": "Face your fears in small steps. Talking about it with someone you trust can help.",
    "unhappy": "Reflect on what’s bothering you. Engage in an activity that brings you joy.",
    "bored": "Explore a new hobby or revisit a book or show you enjoy. Creativity can break boredom!",
    "upset": "Take deep breaths and write down your thoughts. Time and space can help you feel calmer.",
    "guilty": "Acknowledge your feelings and apologize if needed. Learn from the experience and forgive yourself.",
    "lonely": "Reach out to someone you trust. Try engaging in social activities or exploring new connections.",
    "hopeless": "Focus on small, achievable goals. Surround yourself with positivity and reach out for support.",
    "frustrated": "Take a break and allow yourself time to reset. Break down challenges into manageable steps.",
    "jealous": "Focus on your own growth and celebrate your achievements. Reflect on what you truly value.",
    "helpless": "Remember, small actions lead to change. Seek advice from trusted people or professionals.",
    "embarrassed": "Everyone makes mistakes. Learn from them and treat yourself with kindness.",
    "shame": "Acknowledge your feelings but don't let them define you. It's okay to ask for forgiveness and move forward.",
    "regretful": "Reflect on what you've learned. Use it as a guide for future decisions and self-growth.",
    "disappointed": "Acknowledge the situation, but remember, it's temporary. Focus on what you can do next.",
    "bitter": "Try to let go of past resentments. Practice forgiveness and focus on building positivity.",
    "distrustful": "Start with small steps to rebuild trust. Open, honest communication can help restore faith.",
    "pessimistic": "Challenge negative thoughts and try to focus on positive aspects. Surround yourself with optimism."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("userInput", "").lower()
    if user_input in responses:
        return jsonify({"response": responses[user_input]})
    elif user_input in ["hi", "hello"]:
        return jsonify({"response": "Hello! How are you doing? Please tell me how you're feeling."})
    else:
        return jsonify({"response": "I'm sorry, I don't recognize that emotion. Please choose from the listed emotions."})

if __name__ == "__main__":
    app.run(debug=True)
