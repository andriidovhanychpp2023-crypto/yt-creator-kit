import os
import sentry_sdk
from dotenv import load_dotenv
from posthog import Posthog

# Завантажуємо змінні з .env
load_dotenv()

# Ініціалізація Sentry
sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    traces_sample_rate=1.0,
    environment="development",
)

posthog_key = os.getenv("POSTHOG_API_KEY")
posthog = Posthog(posthog_key, host="https://eu.i.posthog.com")

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
        # 1: Фіксуємо помилку вводу в PostHog
        posthog.capture(
            distinct_id="andrii",
            event="input_error",
            properties={"error_type": "empty_string"},
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


# --- ГОЛОВНИЙ БЛОК ПРОГРАМИ ---
if __name__ == "__main__":

    # КРОК 3: Встановлюємо контекст користувача на початку сесії
    sentry_sdk.set_user(
        {
            "id": "andrii",
            "email": "andrii.dovhanych.pp.2023@lpnu.ua",
            "username": "Andrii Student",
            "segment": "premium_user",
        }
    )

    # Перевірка прапорця функцій (Feature Flag)
    is_premium = posthog.feature_enabled("brainrot-premium-mode", "andrii")

    if is_premium:
        print("--- PREMIUM SIGMA MODE ACTIVATED ---")
    else:
        print("--- Standard Mode ---")

    analysis_count = 0

    # 2: Початок сесії в PostHog
    posthog.capture(
        distinct_id="andrii",
        event="session_started",
        properties={"app_version": "1.0"}
    )
    posthog.flush()

    print("Welcome to Brainrot Analyzer v1.0")

    while True:
        # КРОК 4: Моніторинг продуктивності операції
        with sentry_sdk.start_transaction(op="task", name="Analyze Title"):
            prompt = "\nEnter video title (or type 'exit' to quit): "
            user_input = input(prompt)

            if user_input.lower() == "break":
                # Виклик помилки для перевірки Sentry
                err_msg = "Sentry Test Error: Brainrot overload!"
                raise ValueError(err_msg)

            if user_input.lower() == "exit":
                # Очистка контексту при виході
                sentry_sdk.set_user(None)

                # 3: Завершення сесії
                posthog.capture(
                    distinct_id="andrii",
                    event="session_ended",
                    properties={"total_analyses": analysis_count},
                )
                print(f"Total analyses: {analysis_count}. Stay sigma!")

                posthog.flush()
                # Примусова відправка даних перед закриттям
                sentry_sdk.flush(timeout=2.0)
                break

            result = analyze_brainrot_title(user_input)
            analysis_count += 1
            print(f"Result: {result}")

            # 4: Аналітика успішного аналізу
            posthog.capture(
                distinct_id="andrii",
                event="title_analyzed",
                properties={
                    "user_input": user_input,
                    "analysis_result": result,
                    "is_successful": result != "L TITLE",
                },
            )
            posthog.flush()
