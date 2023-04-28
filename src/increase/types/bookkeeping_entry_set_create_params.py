# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BookkeepingEntrySetCreateParams", "Entry"]


class Entry(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the Bookkeeping Account impacted by this entry."""

    amount: Required[int]
    """The entry amount in the minor unit of the account currency.

    For dollars, for example, this is cents. Debit entries have positive amounts;
    credit entries have negative amounts.
    """


class BookkeepingEntrySetCreateParams(TypedDict, total=False):
    entries: Required[List[Entry]]
    """The bookkeeping entries."""

    date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The date of the transaction.

    If `transaction_id` is provided, this must match the `created_at` field on that
    resource.
    """

    transaction_id: str
    """The identifier of the Transaction related to this entry set, if any."""