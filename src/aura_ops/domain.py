from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator


def reject_float(value):
    if isinstance(value, float):
        raise ValueError("money must be Decimal or string, not float")
    return value


class InvoiceItem(BaseModel):
    item_code: str
    quantity: int = Field(gt=0)
    unit_price: Decimal = Field(gt=0)
    declared_total: Decimal = Field(gt=0)

    _no_float = field_validator("unit_price", "declared_total", mode="before")(
        reject_float
    )


class Invoice(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    supplier_id: str = Field(min_length=1)
    invoice_number: str = Field(min_length=1)
    po_number: str = Field(min_length=1)
    total: Decimal = Field(gt=0)
    items: list[InvoiceItem]

    _no_float = field_validator("total", mode="before")(reject_float)