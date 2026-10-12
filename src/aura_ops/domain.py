from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class InvoiceItem(BaseModel):
    item_code: str
    quantity: int = Field(gt=0)
    unit_price: Decimal
    declared_total: Decimal


class Invoice(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    supplier_id: str = Field(min_length=1)
    invoice_number: str = Field(min_length=1)
    po_number: str = Field(min_length=1)
    total: Decimal
    items: list[InvoiceItem]