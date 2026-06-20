from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health():
    return {
        "status": "ok",
        "application": "Rabeeh Builder",
        "version": "0.1.0",
    }