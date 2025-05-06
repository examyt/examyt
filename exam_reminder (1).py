
from twilio.rest import Client
from datetime import datetime

# 👉 તમારું Twilio Account SID અને Auth Token અહીં દાખલ કરો
account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

client = Client(account_sid, auth_token)

def send_exam_reminder(phone_number, exam_date):
    today = datetime.today().date()  # આજેની તારીખ
    exam_day = datetime.strptime(exam_date, "%Y-%m-%d").date()  # Exam Date
    days_left = (exam_day - today).days  # દિવસ બાકી છે

    if days_left < 0:
        message_text = "📚 તમારી પરીક્ષા થઈ ગઈ છે."
    elif days_left == 0:
        message_text = "📢 આજે તમારી પરીક્ષા છે! શુભકામનાઓ 🙌"
    else:
        message_text = f"📆 તમારી પરીક્ષા માટે {days_left} દિવસ બાકી છે."

    # WhatsApp SandBox message મોકલવી
    message = client.messages.create(
        from_='whatsapp:+14155238886',  # Twilio SandBox Number
        to=f'whatsapp:+91{phone_number}',  # તમારા ફોન નંબર
        body=message_text
    )

    print("✅ Reminder મોકલાઈ ગયો:", message.sid)

# ======= વાપરો ========== 
# અહીં તમારું મોબાઈલ નંબર અને પરીક્ષા તારીખ દાખલ કરો
send_exam_reminder('9824101260', '2025-05-21')
