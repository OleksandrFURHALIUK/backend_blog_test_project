import uvicorn

from src.core.app import create_app
from src.core.settings import settings

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, reload=True, port=settings.LISTEN_PORT, workers=1)
