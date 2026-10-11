from decimal import Decimal

from pydantic import BaseModel, Field



class InvoiceItem(BaseModel):
    item_code: str
    quantity: int = Field(gt=0)
    unit_price: Decimal
    declared_total: Decimal


class Invoice(BaseModel):
    supplier_id: str = Field(min_length=1)
    invoice_number: str
    po_number: str
    total: Decimal
    items: list[InvoiceItem]