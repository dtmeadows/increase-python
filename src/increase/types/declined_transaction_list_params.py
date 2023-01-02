# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing_extensions import TypedDict

__all__ = ["CreatedAt", "DeclinedTransactionListParams"]


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


class DeclinedTransactionListParams(TypedDict, total=False):
    account_id: str
    """Filter Declined Transactions to ones belonging to the specified Account."""

    created_at: CreatedAt

    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """

    route_id: str
    """Filter Declined Transactions to those belonging to the specified route."""
