# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types import ReviewRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReviews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: TmdbClient) -> None:
        review = client.reviews.retrieve(
            "review_id",
        )
        assert_matches_type(ReviewRetrieveResponse, review, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TmdbClient) -> None:
        response = client.reviews.with_raw_response.retrieve(
            "review_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = response.parse()
        assert_matches_type(ReviewRetrieveResponse, review, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TmdbClient) -> None:
        with client.reviews.with_streaming_response.retrieve(
            "review_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = response.parse()
            assert_matches_type(ReviewRetrieveResponse, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: TmdbClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `review_id` but received ''"):
            client.reviews.with_raw_response.retrieve(
                "",
            )


class TestAsyncReviews:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTmdbClient) -> None:
        review = await async_client.reviews.retrieve(
            "review_id",
        )
        assert_matches_type(ReviewRetrieveResponse, review, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.reviews.with_raw_response.retrieve(
            "review_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review = await response.parse()
        assert_matches_type(ReviewRetrieveResponse, review, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.reviews.with_streaming_response.retrieve(
            "review_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review = await response.parse()
            assert_matches_type(ReviewRetrieveResponse, review, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTmdbClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `review_id` but received ''"):
            await async_client.reviews.with_raw_response.retrieve(
                "",
            )
