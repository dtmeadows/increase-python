# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.account_number import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccountNumbers:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create(self) -> None:
        resource = self.client.account_numbers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "name": "Rent payments",
            },
        )
        assert isinstance(resource, AccountNumber)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.account_numbers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "name": "Rent payments",
            },
        )
        assert isinstance(resource, AccountNumber)

    def test_method_retrieve(self) -> None:
        resource = self.client.account_numbers.retrieve(
            "string",
        )
        assert isinstance(resource, AccountNumber)

    def test_method_update(self) -> None:
        resource = self.client.account_numbers.update(
            "string",
            {},
        )
        assert isinstance(resource, AccountNumber)

    def test_method_update_with_optional_params(self) -> None:
        resource = self.client.account_numbers.update(
            "string",
            {
                "name": "x",
                "status": "disabled",
            },
        )
        assert isinstance(resource, AccountNumber)

    def test_method_list(self) -> None:
        resource = self.client.account_numbers.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.account_numbers.list(
            {
                "cursor": "string",
                "limit": 0,
                "status": "active",
                "account_id": "string",
            },
        )
        assert isinstance(resource, SyncPage)


class TestAsyncAccountNumbers:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.account_numbers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "name": "Rent payments",
            },
        )
        assert isinstance(resource, AccountNumber)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.account_numbers.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "name": "Rent payments",
            },
        )
        assert isinstance(resource, AccountNumber)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.account_numbers.retrieve(
            "string",
        )
        assert isinstance(resource, AccountNumber)

    async def test_method_update(self) -> None:
        resource = await self.client.account_numbers.update(
            "string",
            {},
        )
        assert isinstance(resource, AccountNumber)

    async def test_method_update_with_optional_params(self) -> None:
        resource = await self.client.account_numbers.update(
            "string",
            {
                "name": "x",
                "status": "disabled",
            },
        )
        assert isinstance(resource, AccountNumber)

    async def test_method_list(self) -> None:
        resource = await self.client.account_numbers.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.account_numbers.list(
            {
                "cursor": "string",
                "limit": 0,
                "status": "active",
                "account_id": "string",
            },
        )
        assert isinstance(resource, AsyncPage)
