from decimal import Decimal

import pytest
from pydantic import ValidationError

from aura_ops.domain import Invoice, InvoiceItem


def make_item(**overrides):
    data = {
        "item_code": "PEN",
        "quantity": 10,
        "unit_price": Decimal("2.50"),
        "declared_total": Decimal("25.00"),
    }
    data.update(overrides)
    return InvoiceItem(**data)


def test_valid_invoice_is_accepted():
    invoice = Invoice(
        supplier_id="SUP-001",
        invoice_number="F-001",
        po_number="PO-100",
        total=Decimal("25.00"),
        items=[make_item()],
    )

    assert invoice.supplier_id == "SUP-001"
    assert invoice.total == Decimal("25.00")
    assert len(invoice.items) == 1
    assert invoice.items[0].unit_price == Decimal("2.50")


def test_invoice_item_with_negative_quantity_is_rejected():
    with pytest.raises(ValidationError):
        make_item(quantity=-5)


def test_invoice_item_with_zero_quantity_is_rejected():
    with pytest.raises(ValidationError):
        make_item(quantity=0, declared_total=Decimal("0.00"))


def test_invoice_with_empty_supplier_id_is_rejected():
    with pytest.raises(ValidationError):
        Invoice(
            supplier_id="",
            invoice_number="F-001",
            po_number="PO-100",
            total=Decimal("25.00"),
            items=[make_item()],
        )