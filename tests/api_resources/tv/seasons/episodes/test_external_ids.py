# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types.tv.seasons.episodes import ExternalIDListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalIDs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TmdbClient) -> None:
        external_id = client.tv.seasons.episodes.external_ids.list(
            episode_number="episode_number",
            series_id=0,
            season_number=0,
        )
        assert_matches_type(ExternalIDListResponse, external_id, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TmdbClient) -> None:
        response = client.tv.seasons.episodes.external_ids.with_raw_response.list(
            episode_number="episode_number",
            series_id=0,
            season_number=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_id = response.parse()
        assert_matches_type(ExternalIDListResponse, external_id, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TmdbClient) -> None:
        with client.tv.seasons.episodes.external_ids.with_streaming_response.list(
            episode_number="episode_number",
            series_id=0,
            season_number=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_id = response.parse()
            assert_matches_type(ExternalIDListResponse, external_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: TmdbClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `episode_number` but received ''"):
            client.tv.seasons.episodes.external_ids.with_raw_response.list(
                episode_number="",
                series_id=0,
                season_number=0,
            )


class TestAsyncExternalIDs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTmdbClient) -> None:
        external_id = await async_client.tv.seasons.episodes.external_ids.list(
            episode_number="episode_number",
            series_id=0,
            season_number=0,
        )
        assert_matches_type(ExternalIDListResponse, external_id, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.tv.seasons.episodes.external_ids.with_raw_response.list(
            episode_number="episode_number",
            series_id=0,
            season_number=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_id = await response.parse()
        assert_matches_type(ExternalIDListResponse, external_id, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.tv.seasons.episodes.external_ids.with_streaming_response.list(
            episode_number="episode_number",
            series_id=0,
            season_number=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_id = await response.parse()
            assert_matches_type(ExternalIDListResponse, external_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncTmdbClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `episode_number` but received ''"):
            await async_client.tv.seasons.episodes.external_ids.with_raw_response.list(
                episode_number="",
                series_id=0,
                season_number=0,
            )
