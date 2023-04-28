# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import BookkeepingEntry
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestBookkeepingEntries:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        bookkeeping_entry = client.bookkeeping_entries.list()
        assert_matches_type(SyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        bookkeeping_entry = client.bookkeeping_entries.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])


class TestAsyncBookkeepingEntries:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        bookkeeping_entry = await client.bookkeeping_entries.list()
        assert_matches_type(AsyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        bookkeeping_entry = await client.bookkeeping_entries.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[BookkeepingEntry], bookkeeping_entry, path=["response"])