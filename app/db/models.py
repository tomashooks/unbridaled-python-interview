from sqlalchemy import Column, Integer, String, Boolean, Float, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    uom = Column(String)  # must be id mapped to string via Enum or another table
    category_name = Column(String)  # must be id mapped to string via Enum or another table
    is_producible = Column(Boolean, default=False)
    is_purchasable = Column(Boolean, default=False)
    type = Column(String, default="product")  # must be id mapped to string via Enum or another table
    additional_info = Column(String)
    purchase_uom = Column(String, default=None)  # must be id mapped to string via Enum or another table
    purchase_uom_conversion_rate = Column(Float)
    batch_tracked = Column(Boolean, default=False)
    variants = relationship("ProductVariant")
    created_at = Column(TIMESTAMP, server_default=func.now())  # Hi ActiveRecord! :)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())


class ProductVariant(Base):
    __tablename__ = "product_variants"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True)
    product_id = Column("Product", ForeignKey("products.id"))
    type = Column(String, default="product")  # must be id mapped to string via Enum or another table
    sales_price = Column(Float)
    purchase_price = Column(Float)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    config_attributes = relationship("ProductVariantAttributes", back_populates="product_variant")


class ProductVariantAttributes(Base):
    __tablename__ = "product_variant_attributes"

    id = Column(Integer, primary_key=True, index=True)
    product_variant_id = Column(Integer, ForeignKey("product_variants.id"))
    product_variant = relationship("ProductVariant", back_populates="config_attributes")
    config_name = Column(String)
    config_value = Column(String)
