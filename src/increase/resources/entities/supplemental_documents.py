# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations


from ..._types import Body, Headers, Query
from ..._base_client import make_request_options
from ..._resource import SyncAPIResource, AsyncAPIResource

from ...types import shared

__all__ = ["SupplementalDocuments", "AsyncSupplementalDocuments"]


class SupplementalDocuments(SyncAPIResource):
    def create(
        self,
        entity_id: str,
        *,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> shared.Entity:
        """
        Args:
          file_id: The identifier of the File containing the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            f"/entities/{entity_id}/supplemental_documents",
            body={"file_id": file_id},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=shared.Entity,
        )


class AsyncSupplementalDocuments(AsyncAPIResource):
    async def create(
        self,
        entity_id: str,
        *,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> shared.Entity:
        """
        Args:
          file_id: The identifier of the File containing the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            f"/entities/{entity_id}/supplemental_documents",
            body={"file_id": file_id},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=shared.Entity,
        )
