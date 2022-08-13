# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.check_deposit import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCheckDeposits:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        resource = client.check_deposits.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "amount": 1000,
                "currency": "USD",
                "front_image_file_id": "file_hkv175ovmc2tb2v2zbrm",
                "back_image_file_id": "file_26khfk98mzfz90a11oqx",
            },
        )
        assert isinstance(resource, CheckDeposit)

    @parametrize
    def test_method_create_with_optional_params(self, client: Increase) -> None:
        resource = client.check_deposits.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "amount": 1000,
                "currency": "USD",
                "front_image_file_id": "file_hkv175ovmc2tb2v2zbrm",
                "back_image_file_id": "file_26khfk98mzfz90a11oqx",
            },
        )
        assert isinstance(resource, CheckDeposit)

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        resource = client.check_deposits.retrieve(
            "string",
        )
        assert isinstance(resource, CheckDeposit)

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        resource = client.check_deposits.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_optional_params(self, client: Increase) -> None:
        resource = client.check_deposits.list(
            {
                "cursor": "string",
                "limit": 0,
                "account_id": "string",
                "created_at": {
                    "after": "2019-12-27T18:11:19.117Z",
                    "before": "2019-12-27T18:11:19.117Z",
                    "on_or_after": "2019-12-27T18:11:19.117Z",
                    "on_or_before": "2019-12-27T18:11:19.117Z",
                },
            },
        )
        assert isinstance(resource, SyncPage)


class TestAsyncCheckDeposits:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        resource = await client.check_deposits.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "amount": 1000,
                "currency": "USD",
                "front_image_file_id": "file_hkv175ovmc2tb2v2zbrm",
                "back_image_file_id": "file_26khfk98mzfz90a11oqx",
            },
        )
        assert isinstance(resource, CheckDeposit)

    @parametrize
    async def test_method_create_with_optional_params(self, client: AsyncIncrease) -> None:
        resource = await client.check_deposits.create(
            {
                "account_id": "account_in71c4amph0vgo2qllky",
                "amount": 1000,
                "currency": "USD",
                "front_image_file_id": "file_hkv175ovmc2tb2v2zbrm",
                "back_image_file_id": "file_26khfk98mzfz90a11oqx",
            },
        )
        assert isinstance(resource, CheckDeposit)

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        resource = await client.check_deposits.retrieve(
            "string",
        )
        assert isinstance(resource, CheckDeposit)

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        resource = await client.check_deposits.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_optional_params(self, client: AsyncIncrease) -> None:
        resource = await client.check_deposits.list(
            {
                "cursor": "string",
                "limit": 0,
                "account_id": "string",
                "created_at": {
                    "after": "2019-12-27T18:11:19.117Z",
                    "before": "2019-12-27T18:11:19.117Z",
                    "on_or_after": "2019-12-27T18:11:19.117Z",
                    "on_or_before": "2019-12-27T18:11:19.117Z",
                },
            },
        )
        assert isinstance(resource, AsyncPage)
