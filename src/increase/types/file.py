# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    created_at: datetime
    """The time the File was created."""

    description: Optional[str]
    """A description of the File."""

    direction: Literal["to_increase", "from_increase"]
    """Whether the File was generated by Increase or by you and sent to Increase."""

    download_url: Optional[str]
    """A URL from where the File can be downloaded at this point in time.

    The location of this URL may change over time.
    """

    filename: Optional[str]
    """The filename that was provided upon upload or generated by Increase."""

    id: str
    """The File's identifier."""

    purpose: Literal[
        "check_image_front",
        "check_image_back",
        "form_1099_int",
        "form_ss_4",
        "identity_document",
        "increase_statement",
        "other",
        "trust_formation_document",
        "digital_wallet_artwork",
        "digital_wallet_app_icon",
        "entity_supplemental_document",
        "export",
    ]
    """What the File will be used for.

    We may add additional possible values for this enum over time; your application
    should be able to handle such additions gracefully.
    """

    type: Literal["file"]
    """A constant representing the object's type.

    For this resource it will always be `file`.
    """
