import random

def main():
    name = "Swapnil Kumar Goel"
    admission_no = "22mc0103"

    print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_no}) 🔮")

    mood = input("How are you feeling today? (happy/sad/neutral/stressed/excited): ").strip().lower()

    fortunes = {
        "happy": [
            "✨ Your fortune: Great things await you, Swapnil! Keep smiling. ✨",
            "😊 Happiness is contagious. Spread it around!",
            "🌞 A sunny day brings joyful surprises."
        ],
        "sad": [
            "💖 Tough times don't last, but tough people like you do.",
            "🌈 After the rain comes the rainbow.",
            "🕊️ Peace and comfort are on their way to you."
        ],
        "neutral": [
            "🔄 Today is a blank canvas; paint it with your favorite colors.",
            "🧘‍♂️ Balance and harmony will guide your day.",
            "🌟 An unexpected event will bring excitement."
        ],
        "stressed": [
            "🛀 Take a deep breath, Swapnil. Relaxation is near.",
            "🧘‍♀️ Meditation and calmness will soothe your mind.",
            "🍵 A warm cup of tea will ease your stress."
        ],
        "excited": [
            "🎉 Your enthusiasm is the key to unlocking new adventures!",
            "🚀 Energy levels high! Channel it into something creative.",
            "🥳 Celebrate the little victories today."
        ]
    }

    if mood in fortunes:
        print(random.choice(fortunes[mood]))
    else:
        print("🤔 Mood not recognized. Please try again with happy, sad, neutral, stressed, or excited.")

if __name__ == "__main__":
    main()
