import os
from dotenv import load_dotenv
from posthog import Posthog

posthog = Posthog('phc_R3d1gye6FUoXi8iKSv79tHAPfzVgiPbYUKSuoCmMNW0', host='https://eu.i.posthog.com')

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
        # 1
        posthog.capture(
            distinct_id='andrii', 
            event='input_error',
            properties={'error_type': 'empty_string'}
        )
        posthog.flush()
        return "Empty title"

    has_slang = any(word in title_lower for word in trending_words)
    is_hype = title.isupper()

    if has_slang and is_hype:
        return "ULTRA RIZZ"
    elif has_slang:
        return "BOP"
    else:
        return "L TITLE"


# --- НОВИЙ БЛОК ДЛЯ ВЗАЄМОДІЇ ---
if __name__ == "__main__":
    # Прапорець
    is_premium = posthog.feature_enabled('brainrot-premium-mode', 'andrii')

    if is_premium:
        print("--- PREMIUM SIGMA MODE ACTIVATED ---")
    else:
        print("--- Standard Mode ---")

    analysis_count = 0

    # 2
    posthog.capture(
        distinct_id='andrii', 
        event='session_started',
        properties={'app_version': '1.0'}
    )
    posthog.flush()

    print("Welcome to Brainrot Analyzer v1.0")

    while True:
        user_input = input("\nEnter video title (or type 'exit' to quit): ")

        if user_input.lower() == "exit":
            # 3
            posthog.capture(
                distinct_id='andrii', 
                event='session_ended',
                properties={'total_analyses': analysis_count}
            )
            print(f'Total analyses done: {analysis_count}. Keep grinding, sigma!')
            posthog.flush()
            break

        result = analyze_brainrot_title(user_input)

        analysis_count += 1
        print(f"Result: {result}")
        
        # 4
        posthog.capture(
            distinct_id='andrii', 
            event='title_analyzed', 
            properties={
                'user_input': user_input,  
                'analysis_result': result,        
                'is_successful': result != "L TITLE" 
            }
        )
        posthog.flush()
