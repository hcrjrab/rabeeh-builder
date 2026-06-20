from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class RabeehException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(RabeehException)
    async def rabeeh_exception_handler(
        request: Request,
        exc: RabeehException,
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": exc.message,
            },
        )