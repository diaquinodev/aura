from decimal import Decimal

from pydantic import BaseModel


class InvoiceItem(BaseModel):
    item_code: str
    quantity: int
    unit_price: Decimal
    declared_total: Decimal


class Invoice(BaseModel):
    supplier_id: str
    invoice_number: str
    po_number: str
    total: Decimal
    items: list[InvoiceItem]