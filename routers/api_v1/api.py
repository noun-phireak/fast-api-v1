from fastapi import APIRouter
from .authentication import auth

router = APIRouter(prefix="/api/v1")


"""
These routes are for authentication
-> login
-> register
"""
router.include_router(auth.router)
