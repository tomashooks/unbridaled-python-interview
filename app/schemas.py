from typing import List, Union

from pydantic import BaseModel, Field, validator


class CreateProductVariantAttrsRequest(BaseModel):
    config_name: str = Field(..., example="Type")
    config_value: str = Field(..., example="Standard")


class CreateProductVariantRequest(BaseModel):
    sku: str = Field(..., example="EM")
    sales_price: float = Field(..., example=40)
    purchase_price: float = Field(..., example=0)
    type: str = "product"
    config_attributes: Union[List[CreateProductVariantAttrsRequest], None] = None


class CreateProductRequest(BaseModel):
    name: str = Field(..., example="Standard-hilt lightsaber")
    uom: str = Field(..., example="pcs")
    category_name: str = Field(..., example="lightsaber")
    is_producible: bool = False
    is_purchasable: bool = False
    type: str = "product"
    purchase_uom: str = Field(..., example="pcs")
    purchase_uom_conversion_rate: float
    batch_tracked: bool = False
    additional_info: str = None
    variants: Union[List[CreateProductVariantRequest], None] = None

    @validator("purchase_uom_conversion_rate", always=True)
    def validate_date(cls, value, values):
        if values["purchase_uom"] != "pcs":
            assert value > 0, "purchase_uom_conversion_rate must be greater 0"

        return value


class CreateProductResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True


class BadRequestResponse(BaseModel):
    errors: List[str]
