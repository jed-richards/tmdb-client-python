# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types.tv_shows import EpisodeGroupRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEpisodeGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: TmdbClient) -> None:
        episode_group = client.tv_shows.episode_groups.retrieve(
            0,
        )
        assert_matches_type(EpisodeGroupRetrieveResponse, episode_group, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TmdbClient) -> None:
        response = client.tv_shows.episode_groups.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        episode_group = response.parse()
        assert_matches_type(EpisodeGroupRetrieveResponse, episode_group, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TmdbClient) -> None:
        with client.tv_shows.episode_groups.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            episode_group = response.parse()
            assert_matches_type(EpisodeGroupRetrieveResponse, episode_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEpisodeGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTmdbClient) -> None:
        episode_group = await async_client.tv_shows.episode_groups.retrieve(
            0,
        )
        assert_matches_type(EpisodeGroupRetrieveResponse, episode_group, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.tv_shows.episode_groups.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        episode_group = await response.parse()
        assert_matches_type(EpisodeGroupRetrieveResponse, episode_group, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.tv_shows.episode_groups.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            episode_group = await response.parse()
            assert_matches_type(EpisodeGroupRetrieveResponse, episode_group, path=["response"])

        assert cast(Any, response.is_closed) is True
