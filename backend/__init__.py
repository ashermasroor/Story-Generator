from fastapi import APIRouter
from .routes import router as story_gen_router

router = APIRouter(prefix="/story_gen")
router.include_router(story_gen_router)
