
from twilio.rest import Client
from datetime import datetime

# Twilio credentials (example values, replace with your own)
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'

client = Client(account_sid, auth_token)

def send_exam_reminder(phone_number, exam_date):
    today = datetime.today().date()
    exam_day = datetime.strptime(exam_date, "%Y-%m-%d").date()
    days_left = (exam_day - today).days

    if days_left < 0:
        message_text = "📚 ваша экзамен уже прошёл."
    elif days_left == 0:
        message_text = "📢 Сегодня ваш экзамен! Удачи 🙌"
    else:
        message_text = f"📆 До экзамена осталось {days_left} дней."

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        to=f'whatsapp:+91{phone_number}',
        body=message_text
    )

    print("✅ Напоминание отправлено:", message.sid)

# Example usage
send_exam_reminder('9824101260', '2025-05-21')
