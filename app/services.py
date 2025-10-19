import httpx
import logging
from datetime import datetime, UTC
from .schemas import User, GetMeResponse

logger = logging.getLogger(__name__)


async def get_cat_fact() -> str:
    """
    Fetch a random cat fact from the external API.

    Returns:
        str: A random cat fact

    Raises:
        httpx.RequestError: If the external API request fails
    """
    api_url = "https://catfact.ninja/fact"

    logger.info(f"Making request to external API: {api_url}")
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        logger.info(f"External API response status: {response.status_code}")

        fact = response.json()["fact"]
        logger.info("Successfully retrieved fact from external API")

        return fact


def create_user() -> User:
    """
    Create a user object with predefined data.

    Returns:
        User: User object with predefined information
    """
    return User(
        email="abdulazeezabdulhammed001@gmail.com",
        name="Abdulazeez Abdulhammed",
        stack="backend",
    )


async def get_user_info() -> GetMeResponse:
    """
    Get user information with a random cat fact.

    Returns:
        GetMeResponse: Complete user information response

    Raises:
        httpx.RequestError: If the external API request fails
        Exception: For any other unexpected errors
    """
    try:
        # Get cat fact from external API
        fact = await get_cat_fact()

        # Create user object
        user = create_user()
        logger.info(f"User data prepared for: {user.name}")

        # Create and return response
        response_data = GetMeResponse(
            status="success",
            user=user,
            timestamp=datetime.now(UTC).isoformat(),
            fact=fact,
        )

        logger.info("User info response prepared successfully")
        return response_data

    except httpx.RequestError as exc:
        logger.error(f"HTTP request error: {exc}")
        raise
    except Exception as exc:
        logger.error(f"Unexpected error in get_user_info: {exc}")
        raise
