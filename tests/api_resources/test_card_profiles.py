# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CardProfile
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestCardProfiles:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        card_profile = client.card_profiles.create(
            description="My Card Profile",
            digital_wallets={
                "issuer_name": "MyBank",
                "card_description": "MyBank Signature Card",
                "background_image_file_id": "file_1ai913suu1zfn1pdetru",
                "app_icon_file_id": "file_8zxqkwlh43wo144u8yec",
            },
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        card_profile = client.card_profiles.create(
            description="My Card Profile",
            digital_wallets={
                "text_color": {
                    "red": 26,
                    "green": 43,
                    "blue": 59,
                },
                "issuer_name": "MyBank",
                "card_description": "MyBank Signature Card",
                "contact_website": "https://example.com",
                "contact_email": "user@example.com",
                "contact_phone": "+18885551212",
                "background_image_file_id": "file_1ai913suu1zfn1pdetru",
                "app_icon_file_id": "file_8zxqkwlh43wo144u8yec",
            },
            physical_cards={
                "contact_phone": "x",
                "front_image_file_id": "string",
                "carrier_image_file_id": "string",
            },
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.card_profiles.with_raw_response.create(
            description="My Card Profile",
            digital_wallets={
                "issuer_name": "MyBank",
                "card_description": "MyBank Signature Card",
                "background_image_file_id": "file_1ai913suu1zfn1pdetru",
                "app_icon_file_id": "file_8zxqkwlh43wo144u8yec",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_profile = response.parse()
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.card_profiles.with_streaming_response.create(
            description="My Card Profile",
            digital_wallets={
                "issuer_name": "MyBank",
                "card_description": "MyBank Signature Card",
                "background_image_file_id": "file_1ai913suu1zfn1pdetru",
                "app_icon_file_id": "file_8zxqkwlh43wo144u8yec",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_profile = response.parse()
            assert_matches_type(CardProfile, card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        card_profile = client.card_profiles.retrieve(
            "string",
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.card_profiles.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_profile = response.parse()
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.card_profiles.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_profile = response.parse()
            assert_matches_type(CardProfile, card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        card_profile = client.card_profiles.list()
        assert_matches_type(SyncPage[CardProfile], card_profile, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        card_profile = client.card_profiles.list(
            cursor="string",
            limit=1,
            physical_cards_status={"in": ["not_eligible", "rejected", "pending_creating"]},
            status={"in": ["pending", "rejected", "active"]},
        )
        assert_matches_type(SyncPage[CardProfile], card_profile, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.card_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_profile = response.parse()
        assert_matches_type(SyncPage[CardProfile], card_profile, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.card_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_profile = response.parse()
            assert_matches_type(SyncPage[CardProfile], card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Increase) -> None:
        card_profile = client.card_profiles.archive(
            "string",
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Increase) -> None:
        response = client.card_profiles.with_raw_response.archive(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_profile = response.parse()
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Increase) -> None:
        with client.card_profiles.with_streaming_response.archive(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_profile = response.parse()
            assert_matches_type(CardProfile, card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCardProfiles:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        card_profile = await client.card_profiles.create(
            description="My Card Profile",
            digital_wallets={
                "issuer_name": "MyBank",
                "card_description": "MyBank Signature Card",
                "background_image_file_id": "file_1ai913suu1zfn1pdetru",
                "app_icon_file_id": "file_8zxqkwlh43wo144u8yec",
            },
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        card_profile = await client.card_profiles.create(
            description="My Card Profile",
            digital_wallets={
                "text_color": {
                    "red": 26,
                    "green": 43,
                    "blue": 59,
                },
                "issuer_name": "MyBank",
                "card_description": "MyBank Signature Card",
                "contact_website": "https://example.com",
                "contact_email": "user@example.com",
                "contact_phone": "+18885551212",
                "background_image_file_id": "file_1ai913suu1zfn1pdetru",
                "app_icon_file_id": "file_8zxqkwlh43wo144u8yec",
            },
            physical_cards={
                "contact_phone": "x",
                "front_image_file_id": "string",
                "carrier_image_file_id": "string",
            },
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.card_profiles.with_raw_response.create(
            description="My Card Profile",
            digital_wallets={
                "issuer_name": "MyBank",
                "card_description": "MyBank Signature Card",
                "background_image_file_id": "file_1ai913suu1zfn1pdetru",
                "app_icon_file_id": "file_8zxqkwlh43wo144u8yec",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_profile = response.parse()
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncIncrease) -> None:
        async with client.card_profiles.with_streaming_response.create(
            description="My Card Profile",
            digital_wallets={
                "issuer_name": "MyBank",
                "card_description": "MyBank Signature Card",
                "background_image_file_id": "file_1ai913suu1zfn1pdetru",
                "app_icon_file_id": "file_8zxqkwlh43wo144u8yec",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_profile = await response.parse()
            assert_matches_type(CardProfile, card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        card_profile = await client.card_profiles.retrieve(
            "string",
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.card_profiles.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_profile = response.parse()
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncIncrease) -> None:
        async with client.card_profiles.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_profile = await response.parse()
            assert_matches_type(CardProfile, card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        card_profile = await client.card_profiles.list()
        assert_matches_type(AsyncPage[CardProfile], card_profile, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        card_profile = await client.card_profiles.list(
            cursor="string",
            limit=1,
            physical_cards_status={"in": ["not_eligible", "rejected", "pending_creating"]},
            status={"in": ["pending", "rejected", "active"]},
        )
        assert_matches_type(AsyncPage[CardProfile], card_profile, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.card_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_profile = response.parse()
        assert_matches_type(AsyncPage[CardProfile], card_profile, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.card_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_profile = await response.parse()
            assert_matches_type(AsyncPage[CardProfile], card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, client: AsyncIncrease) -> None:
        card_profile = await client.card_profiles.archive(
            "string",
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, client: AsyncIncrease) -> None:
        response = await client.card_profiles.with_raw_response.archive(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_profile = response.parse()
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, client: AsyncIncrease) -> None:
        async with client.card_profiles.with_streaming_response.archive(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_profile = await response.parse()
            assert_matches_type(CardProfile, card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True
