from uvicorn import run
import agenta
import chat_service  # This will register the routes with the FastAPI application and marks as complete
import os


if __name__ == "__main__":
    run(
        "agenta:app",
        host="0.0.0.0",
        port=80,
        reload=True,
        reload_dirs=[".", "/agenta-cli"],
    )
