print("🔮 Welcome to Swapnil Kumar Goel's Fortune Teller (22mc0103) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()
if mood == "happy":
    fortune = "Great things await you, Swapnil! Keep smiling."
elif mood == "sad":
    fortune = "Every cloud has a silver lining. Chin up!"
elif mood == "neutral":
    fortune = "Something exciting is just around the corner."
else:
    fortune = "I’m not sure how that feeling translates into a fortune!"
print(f"✨ Your fortune: {fortune} ✨")
