
from fastapi import FastAPI
from loguru import logger
from pydantic import ValidationError
from starlette import status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.base import RequestResponseEndpoint
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.responses import StreamingResponse

from core.settings import settings

from authors.router import router as author_router
from categories.router import router as category_router
from posts.router import router as post_router
from tags.router import router as tag_router


async def startup_event():
    logger.debug(f"Application startup event started")


async def shutdown_event():
    logger.debug(f'Application shutdown event')


class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> StreamingResponse:
        try:
            response = await call_next(request)
        except ValidationError as e:
            # logger.exception(e)
            response = JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={"detail": e.errors()})
        except ValueError as e:
            # log.exception(e)
            response = JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                    content={"detail": [{"msg": "Unknown", "loc": ["Unknown"], "type": "Unknown"}]})
        return response


def create_app() -> FastAPI:
    # exception_handlers = {404: not_found}
    api = FastAPI(
        title="Blog API",
        description='Test blog API',
        root_path="",
        openapi_url="/docs/openapi.json",
        redoc_url="/docs",
        # exception_handlers=exception_handlers
        )
    origins = ["*"]

    api.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    #api.add_middleware(ExceptionMiddleware)

    api.add_event_handler("startup", startup_event)
    api.add_event_handler("shutdown", shutdown_event)
    # init_middlewares(api)
    api.include_router(author_router)
    api.include_router(post_router)
    #api.include_router(tag_router)
    api.include_router(category_router)


    # api.db = None
    # api.include_router(report_router)
    return api
