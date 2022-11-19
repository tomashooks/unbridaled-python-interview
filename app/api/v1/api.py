from fastapi import APIRouter

from app.api.v1.endpoints import products

api_router = APIRouter(prefix="/v1")
api_router.include_router(products.router, prefix="/products", tags=["products"])
