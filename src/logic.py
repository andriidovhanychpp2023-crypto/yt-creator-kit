import os
from dotenv import load_dotenv

# Завантажуємо змінні з .env
load_dotenv()

# Отримуємо значення змінної
status = os.getenv("VITE_APP_STATUS", "Unknown")

print(f"--- {status} ---")


def analyze_brainrot_title(title):
    """
    Аналізує назву на відповідність стилю 'Brainrot factory'.
    """
    trending_words = ["skibidi", "rizz", "gyatt", "sigma", "fanum tax"]
    title_lower = title.lower()

    if not title_lower.strip():
        return "Empty title"

    has_slang = any(word in title_lower for word in trending_words)
    is_hype = title.isupper()

    if has_slang and is_hype:
        return "ULTRA RIZZ 🔥"
    elif has_slang:
        return "BOP ✅"
    else:
        return "L TITLE 💀"


# --- НОВИЙ БЛОК ДЛЯ ВЗАЄМОДІЇ ---
if __name__ == "__main__":
    print("Welcome to Brainrot Analyzer v1.0")

    while True:
        user_input = input("\nEnter video title (or type 'exit' to quit): ")

        if user_input.lower() == "exit":
            print("Keep grinding, sigma!")
            break

        result = analyze_brainrot_title(user_input)
        print(f"Result: {result}")
