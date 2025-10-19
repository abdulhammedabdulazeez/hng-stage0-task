from fastapi import FastAPI
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="HNG Stage 0 Task API",
    description="A simple FastAPI application that call an external api and returns a random cat fact with rate limiting and logging",
    version="1.0.0",
)


@app.get("/")
async def read_root():
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: Welcome message
    """
    return {"message": "Hello there! Thanks for checking out my API."}


@app.get("/me")
async def get_me():
    """
    Get user information with a random cat fact.

    Returns:
        dict: User information with cat fact
    """
    logger.info("GET /me endpoint accessed")

    try:
        import httpx
        from datetime import datetime, UTC

        api_url = "https://catfact.ninja/fact"
        logger.info(f"Making request to external API: {api_url}")

        async with httpx.AsyncClient() as client:
            response = await client.get(api_url)
            logger.info(f"External API response status: {response.status_code}")

            fact = response.json()["fact"]
            logger.info("Successfully retrieved fact from external API")

            user = {
                "email": "abdulazeezabdulhammed001@gmail.com",
                "name": "Abdulazeez Abdulhammed",
                "stack": "backend",
            }

            response_data = {
                "status": "success",
                "user": user,
                "timestamp": datetime.now(UTC).isoformat(),
                "fact": fact,
            }

            logger.info("GET /me response sent successfully")
            return response_data

    except Exception as exc:
        logger.error(f"Error in /me endpoint: {exc}")
        return {
            "error": "An error occurred while processing your request.",
            "message": "Please try again later.",
        }


logger.info("FastAPI application initialized successfully")

# Pxxl deployment compatibility
if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
