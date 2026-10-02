# Women Safety App

A **FastAPI-based backend** for a women safety platform that provides emergency SOS alerts, live location sharing, safe route recommendations, community features, emergency contacts, daily safety tips, an AI-powered safety assistant, and a Rajasthan Police SP directory.

---

## 📌 Project Overview

The Women Safety App backend is designed to provide users with quick access to safety and emergency services.

### Key Features

* 👤 User registration and profile management
* 🚨 SOS emergency alerts
* 📱 SMS and WhatsApp notifications using Twilio
* 📍 Live location sharing and tracking
* 🗺️ Safe route recommendation using Google Routes API
* 🤖 ML-based route risk scoring
* 👥 Community feed with posts, likes, comments, and media
* 🎥 Daily safety tips with video uploads
* ☁️ Cloudinary-based media storage
* 💬 AI safety assistant powered by OpenAI
* 📞 Emergency contact management
* 👮 Rajasthan Police SP directory
* 🔐 Aadhaar-related security configuration

---

## 🏗️ Architecture

```text
Women Safety App
│
├── FastAPI Application
│   │
│   ├── Routes
│   │   ├── Users
│   │   ├── SOS
│   │   ├── Location
│   │   ├── Community
│   │   ├── Safety Tips
│   │   ├── Chat Assistant
│   │   └── Rajasthan SP
│   │
│   ├── Services
│   │   ├── Twilio
│   │   ├── Google Routes
│   │   ├── Cloudinary
│   │   ├── OpenAI
│   │   └── ML Risk Model
│   │
│   ├── Database
│   │   └── MongoDB
│   │
│   └── Models & Schemas
│
└── External Services
    ├── MongoDB Atlas
    ├── Google Maps / Routes API
    ├── Twilio
    ├── Cloudinary
    └── OpenAI
```

---

## 📂 Project Structure

```text
backend/
│
├── app/
│   ├── main.py
│   │
│   ├── routes/
│   │   ├── users.py
│   │   ├── location.py
│   │   ├── community.py
│   │   ├── safety_tips.py
│   │   ├── chat.py
│   │   └── sp.py
│   │
│   ├── services/
│   │   ├── twilio_service.py
│   │   ├── route_service.py
│   │   ├── cloudinary_service.py
│   │   └── ai_service.py
│   │
│   ├── db/
│   │   └── database.py
│   │
│   ├── models/
│   │
│   ├── schemas/
│   │
│   └── core/
│       ├── config.py
│       └── cloudinary.py
│
├── requirements.txt
├── .env
└── README.md
```

---

## 🛠️ Technologies Used

| Technology            | Purpose                      |
| --------------------- | ---------------------------- |
| **FastAPI**           | Backend REST API             |
| **Python**            | Backend programming language |
| **MongoDB**           | Database                     |
| **Motor**             | Async MongoDB driver         |
| **Pydantic**          | Data validation              |
| **Twilio**            | SMS & WhatsApp notifications |
| **Google Routes API** | Route generation             |
| **Scikit-learn**      | ML-based route risk ranking  |
| **NumPy**             | Numerical processing         |
| **Cloudinary**        | Media storage                |
| **OpenAI**            | AI model integration         |
| **OpenAI GPT**        | Safety assistant             |
| **Uvicorn**           | ASGI server                  |

---

## 📦 Dependencies

The backend uses the following core Python libraries:

```text
fastapi
uvicorn
motor
pydantic
twilio
cloudinary
replicate
scikit-learn
numpy
python-multipart
```

For the complete dependency list, see:

```text
backend/requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file inside the `backend/` directory.

```env
MONGO_URI=<your-mongodb-connection-string>

GOOGLE_MAPS_API_KEY=<your-google-maps-api-key>

TWILIO_ACCOUNT_SID=<your-twilio-account-sid>
TWILIO_AUTH_TOKEN=<your-twilio-auth-token>
TWILIO_PHONE_NUMBER=<your-twilio-sms-number>
TWILIO_WHATSAPP_NUMBER=<your-twilio-whatsapp-number>

CLOUDINARY_CLOUD_NAME=<your-cloudinary-cloud-name>
CLOUDINARY_API_KEY=<your-cloudinary-api-key>
CLOUDINARY_API_SECRET=<your-cloudinary-api-secret>

AADHAAR_SECRET_KEY=<your-aadhaar-secret-key>

OPENAI_API_KEY=<your-openai-api-key>
```

> **Important:** Never commit your `.env` file or API credentials to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

# 🚀 Setup

## 1. Clone the Repository

```bash
git clone https://github.com/MdSohailAli3/Clefairy_backend
cd Clefairy_backend
```

## 2. Navigate to Backend

```bash
cd backend
```

## 3. Create a Virtual Environment

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure Environment Variables

Create:

```text
backend/.env
```

and add the required API keys and database credentials.

---

# ▶️ Running the Application

Start the FastAPI development server from the `backend/` directory:

```bash
uvicorn app.main:app --reload
```

The server will start at:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 🔌 API Endpoints

## 👤 User & Emergency Contacts

| Method | Endpoint                        | Description                 |
| ------ | ------------------------------- | --------------------------- |
| `POST` | `/users/register`               | Register a new user         |
| `POST` | `/users/add-contact`            | Add an emergency contact    |
| `GET`  | `/users/get-contacts/{user_id}` | Retrieve emergency contacts |

---

## 🚨 SOS & Live Location

| Method | Endpoint              | Description                  |
| ------ | --------------------- | ---------------------------- |
| `POST` | `/users/sos`          | Trigger SOS notifications    |
| `POST` | `/location/update`    | Update user's live location  |
| `GET`  | `/location/{user_id}` | Get the latest user location |

### SOS Flow

```text
User activates SOS
        ↓
FastAPI receives request
        ↓
Emergency contacts retrieved
        ↓
Twilio service triggered
        ↓
SMS / WhatsApp notifications sent
        ↓
Emergency contacts receive alert
```

---

## 🗺️ Safe Route Recommendation

| Method | Endpoint                   | Description                    |
| ------ | -------------------------- | ------------------------------ |
| `POST` | `/users/routes/safe-route` | Calculate and rank safe routes |

The safe routing system uses:

```text
User Location
      ↓
Google Routes API
      ↓
Available Routes
      ↓
Route Features
      ↓
ML Risk Ranking Model
      ↓
Risk Score
      ↓
Recommended Safe Route
```

The ML component uses **Scikit-learn** and **NumPy** for route risk scoring and ranking.

---

# 👥 Community

The community module allows users to share safety-related posts and interact with other users.

| Method   | Endpoint                              | Description             |
| -------- | ------------------------------------- | ----------------------- |
| `POST`   | `/community/posts`                    | Create a community post |
| `GET`    | `/community/feed`                     | Retrieve community feed |
| `GET`    | `/community/feed/trending`            | Retrieve trending posts |
| `DELETE` | `/community/posts/{post_id}`          | Delete a post           |
| `POST`   | `/community/posts/{post_id}/like`     | Like a post             |
| `DELETE` | `/community/posts/{post_id}/like`     | Unlike a post           |
| `POST`   | `/community/posts/{post_id}/comments` | Add a comment           |
| `GET`    | `/community/posts/{post_id}/comments` | Get comments            |
| `DELETE` | `/community/comments/{comment_id}`    | Delete a comment        |

### Community Flow

```text
User
 ↓
Create Post
 ↓
MongoDB
 ↓
Community Feed
 ↓
Likes / Comments
```

---

# 🎥 Safety Tips

Safety tips can be uploaded as videos and stored using Cloudinary.

| Method | Endpoint                    | Description               |
| ------ | --------------------------- | ------------------------- |
| `POST` | `/users/safety-tips/upload` | Upload a safety tip video |
| `GET`  | `/users/safety-tips/daily`  | Retrieve daily safety tip |

### Upload Flow

```text
Video
 ↓
FastAPI
 ↓
Cloudinary
 ↓
Video URL
 ↓
MongoDB
 ↓
Daily Safety Tip
```

---

# 🤖 AI Safety Assistant

The application includes an OpenAI-powered safety assistant.

| Method | Endpoint                | Description                        |
| ------ | ----------------------- | ---------------------------------- |
| `POST` | `/users/chat/{user_id}` | Send a message to the AI assistant |

### AI Chat Flow

```text
User Message
      ↓
FastAPI
      ↓
AI Service
      ↓
OpenAI
      ↓
AI Response
      ↓
User
```

The `OPENAI_API_KEY` environment variable is required for the AI integration.

---

# 👮 Rajasthan SP Directory

The application provides a directory containing Rajasthan district-level Superintendent of Police information.

| Method | Endpoint                | Description             |
| ------ | ----------------------- | ----------------------- |
| `POST` | `/sp/add`               | Add SP information      |
| `PUT`  | `/sp/update/{district}` | Update SP information   |
| `GET`  | `/sp/{district}`        | Get SP details          |
| `GET`  | `/sp/`                  | List all SP entries     |
| `POST` | `/sp/bulk-add`          | Add multiple SP entries |

### Example SP Object

```json
{
  "district": "Jaipur",
  "sp_name": "SP Name",
  "office_phone": "XXXXXXXXXX",
  "email": "sp@example.com"
}
```

---

# 🗄️ Database

The application uses **MongoDB** for persistent data storage.

MongoDB is accessed asynchronously using **Motor**.

The backend initializes required database indexes when the application starts.

```text
FastAPI
   ↓
Motor
   ↓
MongoDB
```

---

# ☁️ External Services

The backend integrates with multiple third-party services:

### MongoDB

Used for:

* User data
* Emergency contacts
* Location information
* Community posts
* Comments and likes
* Safety tips
* SP directory

### Twilio

Used for:

* Emergency SMS
* WhatsApp SOS notifications

### Google Routes API

Used for:

* Route generation
* Safe route recommendations

### Cloudinary

Used for:

* Safety tip video storage
* Community media uploads

### OpenAI

Used for:

* AI model integration
* Safety assistant responses

---

# ⚙️ Application Configuration

The FastAPI application provides:

* CORS configuration
* MongoDB initialization
* Database index creation
* Router registration
* Custom Swagger UI
* Application startup configuration

CORS is currently configured for development using:

```python
allow_origins=["*"]
```

> **Production:** Restrict `allow_origins` to the actual frontend domain before deployment.

---

# 🔄 Overall Application Flow

```text
                    ┌──────────────┐
                    │   Frontend   │
                    └──────┬───────┘
                           │
                           ↓
                    ┌──────────────┐
                    │   FastAPI    │
                    │   Backend    │
                    └──────┬───────┘
                           │
          ┌────────────────┼─────────────────┐
          │                │                 │
          ↓                ↓                 ↓
      MongoDB          External APIs       ML / AI
          │                │                 │
          │          ┌─────┼─────┐      ┌────┴────┐
          │          │     │     │      │         │
          │       Twilio Google Cloud  Route    GPT
          │              Routes inary  Model
          │
          ↓
     Application Data
```

---

# 🧪 Development

Run the application with auto-reload enabled:

```bash
uvicorn app.main:app --reload
```

For a production-style server:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

# 📁 Useful Paths

| Path                       | Purpose                         |
| -------------------------- | ------------------------------- |
| `backend/app/main.py`      | FastAPI application entry point |
| `backend/app/routes/`      | API route handlers              |
| `backend/app/services/`    | Business logic and integrations |
| `backend/app/core/`        | Configuration and media setup   |
| `backend/app/db/`          | MongoDB connection and indexes  |
| `backend/app/models/`      | Database models                 |
| `backend/app/schemas/`     | Pydantic schemas                |
| `backend/requirements.txt` | Python dependencies             |
| `backend/.env`             | Environment configuration       |

---

# 🔒 Security Notes

* Keep API keys and secrets in environment variables.
* Never commit `.env` to Git.
* Use restricted API keys in production.
* Restrict CORS origins before deployment.
* Use HTTPS in production.
* Validate and sanitize user-uploaded media.
* Apply authentication and authorization to sensitive endpoints.
* Protect emergency contact and location information.
* Store sensitive identifiers such as Aadhaar-related data securely.

---

# 🚧 Future Improvements

Potential improvements include:

* JWT-based authentication
* Role-based authorization
* WebSocket-based real-time location tracking
* Push notifications
* Improved route risk prediction
* More advanced ML risk features
* Redis caching
* Rate limiting
* Automated testing
* Docker deployment
* CI/CD pipeline
* Production monitoring and logging

---

# 📜 License

MIT License

---

# 👨‍💻 Project

**Women Safety App**

A backend system focused on providing emergency assistance, location-based safety features, community support, and AI-powered safety guidance.
