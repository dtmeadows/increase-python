# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BillingAddress", "DigitalWallet", "CardCreateParams"]


class BillingAddress(TypedDict, total=False):
    city: Required[str]
    """The city of the billing address."""

    line1: Required[str]
    """The first line of the billing address."""

    postal_code: Required[str]
    """The postal code of the billing address."""

    state: Required[str]
    """The US state of the billing address."""

    line2: str
    """The second line of the billing address."""


class DigitalWallet(TypedDict, total=False):
    card_profile_id: str
    """The card profile assigned to this digital card.

    Card profiles may also be assigned at the program level.
    """

    email: str
    """
    An email address that can be used to verify the cardholder via one-time passcode
    over email.
    """

    phone: str
    """
    A phone number that can be used to verify the cardholder via one-time passcode
    over SMS.
    """


class CardCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The Account the card should belong to."""

    billing_address: BillingAddress
    """The card's billing address."""

    description: str
    """The description you choose to give the card."""

    digital_wallet: DigitalWallet
    """
    The contact information used in the two-factor steps for digital wallet card
    creation. At least one field must be present to complete the digital wallet
    steps.
    """