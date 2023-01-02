# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from ..._types import Body, Headers, NOT_GIVEN, NotGiven, Query
from ..._base_client import make_request_options
from ..._resource import SyncAPIResource, AsyncAPIResource

from ...types.simulations.card_dispute import CardDispute

__all__ = ["CardDisputes", "AsyncCardDisputes"]


class CardDisputes(SyncAPIResource):
    def action(
        self,
        card_dispute_id: str,
        *,
        status: Literal["accepted", "rejected"],
        explanation: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CardDispute:
        """Simulates moving a card dispute into a rejected or accepted state.

        A dispute can
        only be actioned once and must have a status of `pending_reviewing`.

        Args:
          status: The status to move the dispute to.

          explanation: Why the dispute was rejected. Not required for accepting disputes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            f"/simulations/card_disputes/{card_dispute_id}/action",
            body={
                "status": status,
                "explanation": explanation,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CardDispute,
        )


class AsyncCardDisputes(AsyncAPIResource):
    async def action(
        self,
        card_dispute_id: str,
        *,
        status: Literal["accepted", "rejected"],
        explanation: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> CardDispute:
        """Simulates moving a card dispute into a rejected or accepted state.

        A dispute can
        only be actioned once and must have a status of `pending_reviewing`.

        Args:
          status: The status to move the dispute to.

          explanation: Why the dispute was rejected. Not required for accepting disputes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            f"/simulations/card_disputes/{card_dispute_id}/action",
            body={
                "status": status,
                "explanation": explanation,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=CardDispute,
        )
