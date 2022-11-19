from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.api.errors.error_formatters import integrity_error_formatter
from app.db.database import get_db
from app.schemas import CreateProductRequest, CreateProductResponse, BadRequestResponse
from app.services.products import ProductsService

router = APIRouter()


@router.post(
    "/create",
    response_model=CreateProductResponse,
    responses={
        400: {"model": BadRequestResponse}
    }
)
async def product_create(product: CreateProductRequest, db: Session = Depends(get_db)):
    try:
        product_result = await ProductsService.create_product(product, db)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=integrity_error_formatter(e))

    return product_result
