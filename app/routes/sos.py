from fastapi import APIRouter, HTTPException
from app.schemas.sos_schema import SOSRequest
from app.services.twilio_service import (
    send_sos_whatsapp,
    send_sos_sms
)
from app.services.contact_service import get_user_contacts
from app.services.live_location import update_location

router = APIRouter(prefix="/users",tags=["Emergency-SOS"])

# url - >  /users/sos
@router.post("/sos")
async def trigger_sos(data: SOSRequest):

    link=f"https://live-tracking-nine.vercel.app/?user_id={data.user_id}"
    #we need to send this lat long to hosted webpage, to do this first we need to update this in mongodb
    
    await update_location(data)

    contacts = await get_user_contacts(data.user_id)
                            
    if not contacts:
        raise HTTPException(
            status_code=404,
            detail="No Emergency contacts found!"
        )
        
    results = []

    try:
        for contact in contacts:
            whatsapp_sid = send_sos_whatsapp(
                to_number=contact["phone"],
                location_link= link,
                name=data.name
            )
            sms_sid = send_sos_sms(
                to_number=contact["phone"],
                location_link= link,
                name=data.name
            )
            

            results.append({
                "contact_name": contact["name"],
                "phone": contact["phone"],
                "whatsapp_sid": whatsapp_sid,
                "sms_sid": sms_sid
            })
    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail = f"SOS Failed while sending message: {str(e)}"
        )
    return {
        "status": "SOS Sent Succesfully",
        "total_contacts": len(results),
        "details": results
    }
