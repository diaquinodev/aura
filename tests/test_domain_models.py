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


def make_invoice(**overrides):
    data = {
        "supplier_id": "SUP-001",
        "invoice_number": "F-001",
        "po_number": "PO-100",
        "total": Decimal("25.00"),
        "items": [make_item()],
    }
    data.update(overrides)
    return Invoice(**data)


def test_valid_invoice_is_accepted():
    invoice = make_invoice()

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


@pytest.mark.parametrize("field", ["supplier_id", "invoice_number", "po_number"])
@pytest.mark.parametrize("blank", ["", "   "])
def test_invoice_with_blank_identifier_is_rejected(field, blank):
    with pytest.raises(ValidationError):
        make_invoice(**{field: blank})


@pytest.mark.parametrize("field", ["unit_price", "declared_total"])
@pytest.mark.parametrize("amount", [Decimal("-1.00"), Decimal("0.00")])
def test_invoice_item_with_non_positive_money_is_rejected(field, amount):
    with pytest.raises(ValidationError):
        make_item(**{field: amount})


@pytest.mark.parametrize("amount", [Decimal("-1.00"), Decimal("0.00")])
def test_invoice_with_non_positive_total_is_rejected(amount):
    with pytest.raises(ValidationError):
        make_invoice(total=amount)


@pytest.mark.parametrize("field", ["unit_price", "declared_total"])
def test_invoice_item_with_float_money_is_rejected(field):
    with pytest.raises(ValidationError):
        make_item(**{field: 2.5})


def test_invoice_with_float_total_is_rejected():
    with pytest.raises(ValidationError):
        make_invoice(total=25.0)