# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations


from .._types import Body, Headers, NOT_GIVEN, NotGiven, Query
from .._base_client import AsyncPaginator, make_request_options
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import AsyncPage, SyncPage
from ..types.declined_transaction import DeclinedTransaction
from ..types import declined_transaction_list_params

__all__ = ["DeclinedTransactions", "AsyncDeclinedTransactions"]


class DeclinedTransactions(SyncAPIResource):
    def retrieve(
        self,
        declined_transaction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> DeclinedTransaction:
        return self._get(
            f"/declined_transactions/{declined_transaction_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=DeclinedTransaction,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        route_id: str | NotGiven = NOT_GIVEN,
        created_at: declined_transaction_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[DeclinedTransaction]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter Declined Transactions to ones belonging to the specified Account.

          route_id: Filter Declined Transactions to those belonging to the specified route.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/declined_transactions",
            page=SyncPage[DeclinedTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "account_id": account_id,
                    "route_id": route_id,
                    "created_at": created_at,
                },
            ),
            model=DeclinedTransaction,
        )


class AsyncDeclinedTransactions(AsyncAPIResource):
    async def retrieve(
        self,
        declined_transaction_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> DeclinedTransaction:
        return await self._get(
            f"/declined_transactions/{declined_transaction_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=DeclinedTransaction,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        account_id: str | NotGiven = NOT_GIVEN,
        route_id: str | NotGiven = NOT_GIVEN,
        created_at: declined_transaction_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[DeclinedTransaction, AsyncPage[DeclinedTransaction]]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          account_id: Filter Declined Transactions to ones belonging to the specified Account.

          route_id: Filter Declined Transactions to those belonging to the specified route.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/declined_transactions",
            page=AsyncPage[DeclinedTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "account_id": account_id,
                    "route_id": route_id,
                    "created_at": created_at,
                },
            ),
            model=DeclinedTransaction,
        )
