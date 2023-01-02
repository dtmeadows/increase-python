# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease

from increase.types.simulations.card_dispute import CardDispute

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCardDisputes:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_action(self, client: Increase) -> None:
        resource = client.simulations.card_disputes.action(
            "string",
            status="accepted",
        )
        assert isinstance(resource, CardDispute)

    @parametrize
    def test_method_action_with_all_params(self, client: Increase) -> None:
        resource = client.simulations.card_disputes.action(
            "string",
            status="accepted",
            explanation="x",
        )
        assert isinstance(resource, CardDispute)


class TestAsyncCardDisputes:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_action(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.card_disputes.action(
            "string",
            status="accepted",
        )
        assert isinstance(resource, CardDispute)

    @parametrize
    async def test_method_action_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.card_disputes.action(
            "string",
            status="accepted",
            explanation="x",
        )
        assert isinstance(resource, CardDispute)
