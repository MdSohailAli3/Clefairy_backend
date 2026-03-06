from twilio.rest import Client
from app.core.config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_WHATSAPP_NUMBER,
    TWILIO_PHONE_NUMBER   
)

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


# -------------------- WhatsApp SOS -------------------- #
def send_sos_whatsapp(to_number: str, location_link: str, name: str):
    message = client.messages.create(
        body=f"EMERGENCY!\n{name} needs help.\nLive-Location: {location_link}",
        from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
        to=f"whatsapp:{to_number}",
    )
    return message.sid

# -------------------- SMS SOS -------------------- #
def send_sos_sms(to_number: str, location_link: str, name: str):
    message = client.messages.create(
        body=f"EMERGENCY!\n{name} needs help.\nLive-Location: {location_link}",
        from_=TWILIO_PHONE_NUMBER,   # your Twilio SMS number
        to=to_number,                
    )
    return message.sid