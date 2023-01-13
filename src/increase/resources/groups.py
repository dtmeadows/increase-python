# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .._types import Body, Query, Headers
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types.group import Group
from .._base_client import make_request_options

__all__ = ["Groups", "AsyncGroups"]


class Groups(SyncAPIResource):
    def retrieve_details(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Group:
        """Returns details for the currently authenticated Group."""
        return self._get(
            "/groups/current",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Group,
        )


class AsyncGroups(AsyncAPIResource):
    async def retrieve_details(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Group:
        """Returns details for the currently authenticated Group."""
        return await self._get(
            "/groups/current",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Group,
        )