from fastapi import FastAPI
from app.routes.chat import router as chat_router
from app.routes.sos import router as sos_router
from app.routes.contact_routes import router as contact_router
from app.routes.direction import router as safe
from app.routes.register import router as user
from app.routes.location_routes import router as location_router
from fastapi.middleware.cors import CORSMiddleware
from app.db.init_indexes import create_indexes
from app.routes.community_routes import router as community_router
from app.routes.safety_tip_routes import router as safety_tip_router
from app.routes.sp_routes import router as sp_router
from contextlib import asynccontextmanager
from app.db.mongodb import MongoManager
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 App starting...")
    await MongoManager.connect()
    await create_indexes()
    yield
    print("🛑 App shutting down...")
    await MongoManager.close()

app = FastAPI(
    lifespan=lifespan,
    docs_url=None,
    redoc_url=None
    )

app.mount("/static", StaticFiles(directory="app/static"), name="static")

# backend testing using ngrok
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Clefairy API",
        swagger_favicon_url="/static/app_logo.jpeg"  
    )

# Sakhi- Chat-Bot
app.include_router(chat_router)

# sos - messaging
app.include_router(sos_router)

# add emergency contact
app.include_router(contact_router)

# add safe route 
app.include_router(safe)

# add new user
app.include_router(user)

# live location
app.include_router(location_router)

# community
app.include_router(community_router)

# safety tips
app.include_router(safety_tip_router)

# sp
app.include_router(sp_router)