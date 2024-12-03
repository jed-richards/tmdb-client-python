# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types.tv.episodes import VideoListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVideos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TmdbClient) -> None:
        video = client.tv.episodes.videos.list(
            episode_number=0,
            series_id=0,
            season_number=0,
        )
        assert_matches_type(VideoListResponse, video, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TmdbClient) -> None:
        video = client.tv.episodes.videos.list(
            episode_number=0,
            series_id=0,
            season_number=0,
            include_video_language="include_video_language",
            language="language",
        )
        assert_matches_type(VideoListResponse, video, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TmdbClient) -> None:
        response = client.tv.episodes.videos.with_raw_response.list(
            episode_number=0,
            series_id=0,
            season_number=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(VideoListResponse, video, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TmdbClient) -> None:
        with client.tv.episodes.videos.with_streaming_response.list(
            episode_number=0,
            series_id=0,
            season_number=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(VideoListResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVideos:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTmdbClient) -> None:
        video = await async_client.tv.episodes.videos.list(
            episode_number=0,
            series_id=0,
            season_number=0,
        )
        assert_matches_type(VideoListResponse, video, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        video = await async_client.tv.episodes.videos.list(
            episode_number=0,
            series_id=0,
            season_number=0,
            include_video_language="include_video_language",
            language="language",
        )
        assert_matches_type(VideoListResponse, video, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.tv.episodes.videos.with_raw_response.list(
            episode_number=0,
            series_id=0,
            season_number=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(VideoListResponse, video, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.tv.episodes.videos.with_streaming_response.list(
            episode_number=0,
            series_id=0,
            season_number=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(VideoListResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True
