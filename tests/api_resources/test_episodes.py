# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types import EpisodeAccountStatesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEpisodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_account_states(self, client: TmdbClient) -> None:
        episode = client.episodes.account_states(
            episode_number=0,
            series_id=0,
            season_number=0,
        )
        assert_matches_type(EpisodeAccountStatesResponse, episode, path=["response"])

    @parametrize
    def test_method_account_states_with_all_params(self, client: TmdbClient) -> None:
        episode = client.episodes.account_states(
            episode_number=0,
            series_id=0,
            season_number=0,
            guest_session_id="guest_session_id",
            session_id="session_id",
        )
        assert_matches_type(EpisodeAccountStatesResponse, episode, path=["response"])

    @parametrize
    def test_raw_response_account_states(self, client: TmdbClient) -> None:
        response = client.episodes.with_raw_response.account_states(
            episode_number=0,
            series_id=0,
            season_number=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        episode = response.parse()
        assert_matches_type(EpisodeAccountStatesResponse, episode, path=["response"])

    @parametrize
    def test_streaming_response_account_states(self, client: TmdbClient) -> None:
        with client.episodes.with_streaming_response.account_states(
            episode_number=0,
            series_id=0,
            season_number=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            episode = response.parse()
            assert_matches_type(EpisodeAccountStatesResponse, episode, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEpisodes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_account_states(self, async_client: AsyncTmdbClient) -> None:
        episode = await async_client.episodes.account_states(
            episode_number=0,
            series_id=0,
            season_number=0,
        )
        assert_matches_type(EpisodeAccountStatesResponse, episode, path=["response"])

    @parametrize
    async def test_method_account_states_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        episode = await async_client.episodes.account_states(
            episode_number=0,
            series_id=0,
            season_number=0,
            guest_session_id="guest_session_id",
            session_id="session_id",
        )
        assert_matches_type(EpisodeAccountStatesResponse, episode, path=["response"])

    @parametrize
    async def test_raw_response_account_states(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.episodes.with_raw_response.account_states(
            episode_number=0,
            series_id=0,
            season_number=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        episode = await response.parse()
        assert_matches_type(EpisodeAccountStatesResponse, episode, path=["response"])

    @parametrize
    async def test_streaming_response_account_states(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.episodes.with_streaming_response.account_states(
            episode_number=0,
            series_id=0,
            season_number=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            episode = await response.parse()
            assert_matches_type(EpisodeAccountStatesResponse, episode, path=["response"])

        assert cast(Any, response.is_closed) is True
