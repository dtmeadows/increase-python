# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.account import Account
from ..types.account_list_params import AccountListParams
from ..types.account_create_params import AccountCreateParams
from ..types.account_update_params import AccountUpdateParams

__all__ = ["Accounts", "AsyncAccounts"]


class Accounts(SyncAPIResource):
    def create(
        self,
        body: AccountCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Account:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/accounts",
            body=maybe_transform(body, AccountCreateParams),
            options=options,
            cast_to=Account,
        )

    def retrieve(
        self,
        account_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Account:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/accounts/{account_id}",
            options=options,
            cast_to=Account,
        )

    def update(
        self,
        account_id: str,
        body: AccountUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Account:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._patch(
            f"/accounts/{account_id}",
            body=maybe_transform(body, AccountUpdateParams),
            options=options,
            cast_to=Account,
        )

    def list(
        self,
        query: AccountListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Account]:
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, AccountListParams))
        return self._get_api_list(
            "/accounts",
            page=SyncPage[Account],
            options=options,
            model=Account,
        )

    def close(
        self,
        account_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Account:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            f"/accounts/{account_id}/close",
            options=options,
            cast_to=Account,
        )


class AsyncAccounts(AsyncAPIResource):
    async def create(
        self,
        body: AccountCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Account:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/accounts",
            body=maybe_transform(body, AccountCreateParams),
            options=options,
            cast_to=Account,
        )

    async def retrieve(
        self,
        account_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Account:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/accounts/{account_id}",
            options=options,
            cast_to=Account,
        )

    async def update(
        self,
        account_id: str,
        body: AccountUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Account:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._patch(
            f"/accounts/{account_id}",
            body=maybe_transform(body, AccountUpdateParams),
            options=options,
            cast_to=Account,
        )

    def list(
        self,
        query: AccountListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Account, AsyncPage[Account]]:
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, AccountListParams))
        return self._get_api_list(
            "/accounts",
            page=AsyncPage[Account],
            options=options,
            model=Account,
        )

    async def close(
        self,
        account_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Account:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            f"/accounts/{account_id}/close",
            options=options,
            cast_to=Account,
        )
