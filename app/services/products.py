from sqlalchemy.orm import Session

from app.db.models import Product, ProductVariant, ProductVariantAttributes
from app.schemas import CreateProductRequest


class ProductsService():

    @staticmethod
    async def create_product(product: CreateProductRequest, db: Session):
        variants = []
        if product.variants:
            for item in product.variants:
                config_attributes = []
                if item.config_attributes:

                    for subitem in item.config_attributes:
                        config_attributes.append(ProductVariantAttributes(**subitem.dict()))
                variants.append(ProductVariant(
                    **item.dict(
                        exclude={"config_attributes"}
                    ),
                    config_attributes=config_attributes
                ))

        db_product = Product(**product.dict(exclude={"variants"}), variants=variants)
        db.add(db_product)
        db.commit()
        db.rollback()
        db.refresh(db_product)

        return db_product
