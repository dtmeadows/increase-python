# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["TransactionListParams", "CreatedAt", "Category"]


class CreatedAt(TypedDict, total=False):
    after: str
    """
    Return results after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    before: str
    """
    Return results before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    on_or_after: str
    """
    Return results on or after this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """

    on_or_before: str
    """
    Return results on or before this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """


_CategoryReservedKeywords = TypedDict(
    "_CategoryReservedKeywords",
    {
        "in": List[
            Literal[
                "account_transfer_intention",
                "ach_check_conversion_return",
                "ach_check_conversion",
                "ach_transfer_intention",
                "ach_transfer_rejection",
                "ach_transfer_return",
                "card_dispute_acceptance",
                "card_refund",
                "card_settlement",
                "check_deposit_acceptance",
                "check_deposit_return",
                "check_transfer_intention",
                "check_transfer_return",
                "check_transfer_rejection",
                "check_transfer_stop_payment_request",
                "dispute_resolution",
                "empyreal_cash_deposit",
                "inbound_ach_transfer",
                "inbound_check",
                "inbound_international_ach_transfer",
                "inbound_real_time_payments_transfer_confirmation",
                "inbound_wire_drawdown_payment_reversal",
                "inbound_wire_drawdown_payment",
                "inbound_wire_reversal",
                "inbound_wire_transfer",
                "internal_general_ledger_transaction",
                "internal_source",
                "card_route_refund",
                "card_route_settlement",
                "real_time_payments_transfer_acknowledgement",
                "sample_funds",
                "wire_drawdown_payment_intention",
                "wire_drawdown_payment_rejection",
                "wire_transfer_intention",
                "wire_transfer_rejection",
                "other",
            ]
        ],
    },
    total=False,
)


class Category(_CategoryReservedKeywords, total=False):
    pass


class TransactionListParams(TypedDict, total=False):
    account_id: str
    """Filter Transactions for those belonging to the specified Account."""

    category: Category

    created_at: CreatedAt

    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """

    route_id: str
    """Filter Transactions for those belonging to the specified route."""
