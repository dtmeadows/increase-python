# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List
from typing_extensions import Literal

from ...types import shared, entity_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from .supplemental_documents import SupplementalDocuments, AsyncSupplementalDocuments

if TYPE_CHECKING:
    from ..._client import Increase, AsyncIncrease

__all__ = ["Entities", "AsyncEntities"]


class Entities(SyncAPIResource):
    supplemental_documents: SupplementalDocuments

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.supplemental_documents = SupplementalDocuments(client)

    def create(
        self,
        *,
        structure: Literal["corporation", "natural_person", "joint", "trust"],
        corporation: entity_create_params.Corporation | NotGiven = NOT_GIVEN,
        natural_person: entity_create_params.NaturalPerson | NotGiven = NOT_GIVEN,
        joint: entity_create_params.Joint | NotGiven = NOT_GIVEN,
        trust: entity_create_params.Trust | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        relationship: Literal["affiliated", "informational", "unaffiliated"],
        supplemental_documents: List[entity_create_params.SupplementalDocuments] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> shared.Entity:
        """
        Create an Entity

        Args:
          structure: The type of Entity to create.

          corporation: Details of the corporation entity to create. Required if `structure` is equal to
              `corporation`.

          natural_person: Details of the natural person entity to create. Required if `structure` is equal
              to `natural_person`.

          joint: Details of the joint entity to create. Required if `structure` is equal to
              `joint`.

          trust: Details of the trust entity to create. Required if `structure` is equal to
              `trust`.

          description: The description you choose to give the entity.

          relationship: The relationship between your group and the entity.

          supplemental_documents: Additional documentation associated with the entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/entities",
            body={
                "structure": structure,
                "corporation": corporation,
                "natural_person": natural_person,
                "joint": joint,
                "trust": trust,
                "description": description,
                "relationship": relationship,
                "supplemental_documents": supplemental_documents,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=shared.Entity,
        )

    def retrieve(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> shared.Entity:
        """Retrieve an Entity"""
        return self._get(
            f"/entities/{entity_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=shared.Entity,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[shared.Entity]:
        """
        List Entities

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/entities",
            page=SyncPage[shared.Entity],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                },
            ),
            model=shared.Entity,
        )


class AsyncEntities(AsyncAPIResource):
    supplemental_documents: AsyncSupplementalDocuments

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.supplemental_documents = AsyncSupplementalDocuments(client)

    async def create(
        self,
        *,
        structure: Literal["corporation", "natural_person", "joint", "trust"],
        corporation: entity_create_params.Corporation | NotGiven = NOT_GIVEN,
        natural_person: entity_create_params.NaturalPerson | NotGiven = NOT_GIVEN,
        joint: entity_create_params.Joint | NotGiven = NOT_GIVEN,
        trust: entity_create_params.Trust | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        relationship: Literal["affiliated", "informational", "unaffiliated"],
        supplemental_documents: List[entity_create_params.SupplementalDocuments] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> shared.Entity:
        """
        Create an Entity

        Args:
          structure: The type of Entity to create.

          corporation: Details of the corporation entity to create. Required if `structure` is equal to
              `corporation`.

          natural_person: Details of the natural person entity to create. Required if `structure` is equal
              to `natural_person`.

          joint: Details of the joint entity to create. Required if `structure` is equal to
              `joint`.

          trust: Details of the trust entity to create. Required if `structure` is equal to
              `trust`.

          description: The description you choose to give the entity.

          relationship: The relationship between your group and the entity.

          supplemental_documents: Additional documentation associated with the entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/entities",
            body={
                "structure": structure,
                "corporation": corporation,
                "natural_person": natural_person,
                "joint": joint,
                "trust": trust,
                "description": description,
                "relationship": relationship,
                "supplemental_documents": supplemental_documents,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=shared.Entity,
        )

    async def retrieve(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> shared.Entity:
        """Retrieve an Entity"""
        return await self._get(
            f"/entities/{entity_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=shared.Entity,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[shared.Entity, AsyncPage[shared.Entity]]:
        """
        List Entities

        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/entities",
            page=AsyncPage[shared.Entity],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                },
            ),
            model=shared.Entity,
        )