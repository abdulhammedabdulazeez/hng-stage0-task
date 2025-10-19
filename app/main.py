from fastapi import FastAPI
import logging
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from .routes import router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure rate limiter
limiter = Limiter(key_func=get_remote_address)

# Create FastAPI app
app = FastAPI(
    title="HNG Stage 0 Task API",
    description="A simple FastAPI application that call an external api and returns a random cat fact with rate limiting and logging",
    version="1.0.0",
)

# Add rate limiting to the app
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Include the router
app.include_router(router)

logger.info("FastAPI application initialized successfully")
