# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    list_clear_params,
    list_create_params,
    list_delete_params,
    list_add_item_params,
    list_retrieve_params,
    list_item_status_params,
    list_remove_item_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.list_clear_response import ListClearResponse
from ..types.list_create_response import ListCreateResponse
from ..types.list_delete_response import ListDeleteResponse
from ..types.list_add_item_response import ListAddItemResponse
from ..types.list_retrieve_response import ListRetrieveResponse
from ..types.list_item_status_response import ListItemStatusResponse
from ..types.list_remove_item_response import ListRemoveItemResponse

__all__ = ["ListsResource", "AsyncListsResource"]


class ListsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return ListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return ListsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        session_id: str,
        raw_body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListCreateResponse:
        """
        Create

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/3/list",
            body=maybe_transform({"raw_body": raw_body}, list_create_params.ListCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"session_id": session_id}, list_create_params.ListCreateParams),
            ),
            cast_to=ListCreateResponse,
        )

    def retrieve(
        self,
        list_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListRetrieveResponse:
        """
        Details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/list/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "language": language,
                        "page": page,
                    },
                    list_retrieve_params.ListRetrieveParams,
                ),
            ),
            cast_to=ListRetrieveResponse,
        )

    def delete(
        self,
        list_id: int,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListDeleteResponse:
        """
        Delete a list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/3/list/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"session_id": session_id}, list_delete_params.ListDeleteParams),
            ),
            cast_to=ListDeleteResponse,
        )

    def add_item(
        self,
        list_id: int,
        *,
        session_id: str,
        raw_body: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListAddItemResponse:
        """
        Add a movie to a list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/3/list/{list_id}/add_item",
            body=maybe_transform({"raw_body": raw_body}, list_add_item_params.ListAddItemParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"session_id": session_id}, list_add_item_params.ListAddItemParams),
            ),
            cast_to=ListAddItemResponse,
        )

    def clear(
        self,
        list_id: int,
        *,
        confirm: bool,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListClearResponse:
        """
        Clear all items from a list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/3/list/{list_id}/clear",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "confirm": confirm,
                        "session_id": session_id,
                    },
                    list_clear_params.ListClearParams,
                ),
            ),
            cast_to=ListClearResponse,
        )

    def item_status(
        self,
        list_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        movie_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListItemStatusResponse:
        """
        Use this method to check if an item has already been added to the list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/list/{list_id}/item_status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "language": language,
                        "movie_id": movie_id,
                    },
                    list_item_status_params.ListItemStatusParams,
                ),
            ),
            cast_to=ListItemStatusResponse,
        )

    def remove_item(
        self,
        list_id: int,
        *,
        session_id: str,
        raw_body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListRemoveItemResponse:
        """
        Remove a movie from a list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/3/list/{list_id}/remove_item",
            body=maybe_transform({"raw_body": raw_body}, list_remove_item_params.ListRemoveItemParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"session_id": session_id}, list_remove_item_params.ListRemoveItemParams),
            ),
            cast_to=ListRemoveItemResponse,
        )


class AsyncListsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncListsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        session_id: str,
        raw_body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListCreateResponse:
        """
        Create

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/3/list",
            body=await async_maybe_transform({"raw_body": raw_body}, list_create_params.ListCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"session_id": session_id}, list_create_params.ListCreateParams),
            ),
            cast_to=ListCreateResponse,
        )

    async def retrieve(
        self,
        list_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListRetrieveResponse:
        """
        Details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/list/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "language": language,
                        "page": page,
                    },
                    list_retrieve_params.ListRetrieveParams,
                ),
            ),
            cast_to=ListRetrieveResponse,
        )

    async def delete(
        self,
        list_id: int,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListDeleteResponse:
        """
        Delete a list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/3/list/{list_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"session_id": session_id}, list_delete_params.ListDeleteParams),
            ),
            cast_to=ListDeleteResponse,
        )

    async def add_item(
        self,
        list_id: int,
        *,
        session_id: str,
        raw_body: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListAddItemResponse:
        """
        Add a movie to a list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/3/list/{list_id}/add_item",
            body=await async_maybe_transform({"raw_body": raw_body}, list_add_item_params.ListAddItemParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"session_id": session_id}, list_add_item_params.ListAddItemParams),
            ),
            cast_to=ListAddItemResponse,
        )

    async def clear(
        self,
        list_id: int,
        *,
        confirm: bool,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListClearResponse:
        """
        Clear all items from a list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/3/list/{list_id}/clear",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "confirm": confirm,
                        "session_id": session_id,
                    },
                    list_clear_params.ListClearParams,
                ),
            ),
            cast_to=ListClearResponse,
        )

    async def item_status(
        self,
        list_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        movie_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListItemStatusResponse:
        """
        Use this method to check if an item has already been added to the list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/list/{list_id}/item_status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "language": language,
                        "movie_id": movie_id,
                    },
                    list_item_status_params.ListItemStatusParams,
                ),
            ),
            cast_to=ListItemStatusResponse,
        )

    async def remove_item(
        self,
        list_id: int,
        *,
        session_id: str,
        raw_body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListRemoveItemResponse:
        """
        Remove a movie from a list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/3/list/{list_id}/remove_item",
            body=await async_maybe_transform({"raw_body": raw_body}, list_remove_item_params.ListRemoveItemParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"session_id": session_id}, list_remove_item_params.ListRemoveItemParams
                ),
            ),
            cast_to=ListRemoveItemResponse,
        )


class ListsResourceWithRawResponse:
    def __init__(self, lists: ListsResource) -> None:
        self._lists = lists

        self.create = to_raw_response_wrapper(
            lists.create,
        )
        self.retrieve = to_raw_response_wrapper(
            lists.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            lists.delete,
        )
        self.add_item = to_raw_response_wrapper(
            lists.add_item,
        )
        self.clear = to_raw_response_wrapper(
            lists.clear,
        )
        self.item_status = to_raw_response_wrapper(
            lists.item_status,
        )
        self.remove_item = to_raw_response_wrapper(
            lists.remove_item,
        )


class AsyncListsResourceWithRawResponse:
    def __init__(self, lists: AsyncListsResource) -> None:
        self._lists = lists

        self.create = async_to_raw_response_wrapper(
            lists.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            lists.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            lists.delete,
        )
        self.add_item = async_to_raw_response_wrapper(
            lists.add_item,
        )
        self.clear = async_to_raw_response_wrapper(
            lists.clear,
        )
        self.item_status = async_to_raw_response_wrapper(
            lists.item_status,
        )
        self.remove_item = async_to_raw_response_wrapper(
            lists.remove_item,
        )


class ListsResourceWithStreamingResponse:
    def __init__(self, lists: ListsResource) -> None:
        self._lists = lists

        self.create = to_streamed_response_wrapper(
            lists.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            lists.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            lists.delete,
        )
        self.add_item = to_streamed_response_wrapper(
            lists.add_item,
        )
        self.clear = to_streamed_response_wrapper(
            lists.clear,
        )
        self.item_status = to_streamed_response_wrapper(
            lists.item_status,
        )
        self.remove_item = to_streamed_response_wrapper(
            lists.remove_item,
        )


class AsyncListsResourceWithStreamingResponse:
    def __init__(self, lists: AsyncListsResource) -> None:
        self._lists = lists

        self.create = async_to_streamed_response_wrapper(
            lists.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            lists.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            lists.delete,
        )
        self.add_item = async_to_streamed_response_wrapper(
            lists.add_item,
        )
        self.clear = async_to_streamed_response_wrapper(
            lists.clear,
        )
        self.item_status = async_to_streamed_response_wrapper(
            lists.item_status,
        )
        self.remove_item = async_to_streamed_response_wrapper(
            lists.remove_item,
        )
