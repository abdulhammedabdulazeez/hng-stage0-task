from fastapi import APIRouter, HTTPException, Request, status
import logging
from slowapi import Limiter
from slowapi.util import get_remote_address
from .schemas import GetMeResponse
from .services import get_user_info

logger = logging.getLogger(__name__)

# Create router instance
router = APIRouter()

# Create limiter instance for the router
limiter = Limiter(key_func=get_remote_address)


@router.get("/")
@limiter.limit("10/minute")
async def read_root(request: Request):
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: Welcome message
    """
    return {"message": "Hello there! Thanks for checking out my API."}


@router.get("/me", response_model=GetMeResponse)
@limiter.limit("5/minute")
async def get_me(request: Request):
    """
    Get user information with a random cat fact.

    Returns:
        GetMeResponse: User information with cat fact

    Raises:
        HTTPException: If there's an error fetching data
    """
    logger.info("GET /me endpoint accessed")

    try:
        response_data = await get_user_info()
        logger.info("GET /me response sent successfully")
        print(response_data)
        return response_data

    except Exception as exc:
        logger.error(f"Error in /me endpoint: {exc}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "error": "An error occurred while processing your request.",
                "message": "Please try again later.",
            },
        )
