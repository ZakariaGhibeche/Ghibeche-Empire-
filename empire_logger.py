# Ghibeche Empire Logger
import datetime

def log_event(event):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("empire_log.txt", "a") as f:
        f.write(f"[{timestamp}] {event}\n")
    print(f"تم توثيق الحدث: {event}")

# تجربة تسجيل أول حدث في الإمبراطورية
if __name__ == "__main__":
    print("مرحباً بك في إمبراطورية غيبش الرقمية.")
    action = input("ما هو الحدث الذي تريد توثيقه اليوم؟: ")
    log_event(action)
