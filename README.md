# HNG Stage 0 Task API

A simple FastAPI application that calls an external API and returns a random cat fact with rate limiting and logging.

## 🚀 Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **External API Integration**: Fetches random cat facts from [catfact.ninja](https://catfact.ninja/)
- **Rate Limiting**: Protects endpoints from abuse with configurable limits
- **Comprehensive Logging**: Detailed logging for debugging and monitoring
- **Clean Architecture**: Well-structured codebase following best practices
- **Pydantic Models**: Type-safe data validation and serialization

## 📋 API Endpoints

### `GET /`
Returns a welcome message.

**Rate Limit**: 10 requests per minute

**Response**:
```json
{
  "message": "Hello there! Thanks for checking out my API."
}
```

### `GET /me`
Returns user information along with a random cat fact.

**Rate Limit**: 5 requests per minute

**Response**:
```json
{
  "status": "success",
  "user": {
    "email": "abdulazeezabdulhammed001@gmail.com",
    "name": "Abdulazeez Abdulhammed",
    "stack": "backend"
  },
  "timestamp": "2024-01-15T10:30:00.000Z",
  "fact": "A random cat fact from the external API"
}
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd hng-stage0-task
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Running the Application

### Development Mode
```bash
uvicorn app.main:app --reload
```

The application will be available at:
- **API**: http://localhost:8000
- **Interactive API Docs**: http://localhost:8000/docs
- **Alternative API Docs**: http://localhost:8000/redoc

### Production Mode
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 📁 Project Structure

```
app/
├── __init__.py          # Package initialization
├── main.py             # App initialization, middleware, rate limiting setup
├── schemas.py          # Pydantic models (User, GetMeResponse)
├── routes.py           # Route handlers with rate limiting
└── services.py         # Business logic and external API calls
```

### File Responsibilities

- **`main.py`**: FastAPI app initialization, rate limiting configuration, and router setup
- **`schemas.py`**: Pydantic models for data validation and serialization
- **`routes.py`**: API endpoint definitions with rate limiting decorators
- **`services.py`**: Business logic, external API integration, and data processing

## 🔧 Configuration

### Rate Limiting
- Root endpoint (`/`): 10 requests per minute
- User info endpoint (`/me`): 5 requests per minute
- Rate limits are applied per IP address

### Logging
- Logs are output to console with INFO level
- Comprehensive logging for requests, responses, and errors
- External API calls are logged with status codes

## 🧪 Testing the API

### Using curl

**Test the root endpoint:**
```bash
curl http://localhost:8000/
```

**Test the user info endpoint:**
```bash
curl http://localhost:8000/me
```

### Using the Interactive Docs
Visit http://localhost:8000/docs to test the API endpoints directly in your browser.

### Testing Rate Limiting
Make multiple requests quickly to see rate limiting in action:
```bash
for i in {1..6}; do curl http://localhost:8000/me; echo; done
```

## 📦 Dependencies

- **FastAPI**: Web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **Pydantic**: Data validation and settings management
- **httpx**: HTTP client for making external API calls
- **slowapi**: Rate limiting for FastAPI applications

## 🚨 Error Handling

The application includes comprehensive error handling:

- **HTTP Request Errors**: Handles failures when calling external APIs
- **Rate Limit Exceeded**: Returns 429 status with retry information
- **Unexpected Errors**: Catches and logs unexpected exceptions
- **Validation Errors**: Pydantic automatically validates request/response data

## 🔍 Monitoring & Logging

The application logs:
- Request/response information
- External API calls and responses
- Error details with stack traces
- Rate limiting events
- Application startup/shutdown

## 🚀 Deployment Considerations

For production deployment:

1. **Environment Variables**: Set appropriate log levels and rate limits
2. **Reverse Proxy**: Use nginx or similar for production
3. **Process Manager**: Use systemd, supervisor, or similar
4. **Monitoring**: Implement proper monitoring and alerting
5. **Rate Limiting Storage**: Consider Redis for distributed rate limiting

## 👨‍💻 Author

**Abdulazeez Abdulhammed**
- Email: abdulazeezabdulhammed001@gmail.com
- Stack: Backend Development

## 📄 License

This project is part of the HNG Internship Stage 0 Task.


