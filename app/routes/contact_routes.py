from fastapi import APIRouter
from app.schemas.contact_schema import EmergencyContact
from app.services.contact_service import (
    add_emergency_contact,
    get_user_contacts
)

router = APIRouter(prefix="/users", tags=["Emergency Contacts"])
# prefix is placed before user_id
# tags is used to maitain structure in fastapi docs(swagger)

# url -> /users/add-contact
@router.post("/add-contact")
async def add_contact(contact: EmergencyContact):
    await add_emergency_contact(contact.model_dump())
    return {"message": "Contact added successfully"}


# url -> /users/get-contact
@router.get("/get-contacts/{user_id}")
async def fetch_contacts(user_id: int):
    contacts = await get_user_contacts(user_id)
    
    #converting ObjectId(mongo dtype) to str before returning  
    for contact in contacts:
        contact["_id"] = str(contact["_id"])

    return contacts
