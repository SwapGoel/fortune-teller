print("🔮 Welcome to Swapnil Kumar Goel's Fortune Teller (22mc0103) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()
import random

fortunes = {
    "happy": ["Great things await you, Swapnil! Keep smiling.", "Your joy is contagious today!"],
    "sad":   ["Every cloud has a silver lining. Chin up!", "Tough times don't last."],
    "neutral": ["Something exciting is just around the corner.", "Life is full of surprises!"],
    "stressed": ["Take a deep breath. You’ve got this, Swapnil!", "Relax—better days are on their way!"]
}
fortune = random.choice(fortunes.get(mood, ["I’m not sure how that feeling translates into a fortune!"]))
print(f"✨ Your fortune: {fortune} ✨")
