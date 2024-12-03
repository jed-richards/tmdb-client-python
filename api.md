# Movies

Types:

```python
from tmdb_client.types import (
    MovieRetrieveResponse,
    MovieDiscoverResponse,
    MovieRatingResponse,
    MovieRatingDeleteResponse,
    MovieSearchResponse,
)
```

Methods:

- <code title="get /3/movie/{movie_id}">client.movies.<a href="./src/tmdb_client/resources/movies/movies.py">retrieve</a>(movie_id, \*\*<a href="src/tmdb_client/types/movie_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/movie_retrieve_response.py">MovieRetrieveResponse</a></code>
- <code title="get /3/discover/movie">client.movies.<a href="./src/tmdb_client/resources/movies/movies.py">discover</a>(\*\*<a href="src/tmdb_client/types/movie_discover_params.py">params</a>) -> <a href="./src/tmdb_client/types/movie_discover_response.py">MovieDiscoverResponse</a></code>
- <code title="post /3/movie/{movie_id}/rating">client.movies.<a href="./src/tmdb_client/resources/movies/movies.py">rating</a>(movie_id, \*\*<a href="src/tmdb_client/types/movie_rating_params.py">params</a>) -> <a href="./src/tmdb_client/types/movie_rating_response.py">MovieRatingResponse</a></code>
- <code title="delete /3/movie/{movie_id}/rating">client.movies.<a href="./src/tmdb_client/resources/movies/movies.py">rating_delete</a>(movie_id, \*\*<a href="src/tmdb_client/types/movie_rating_delete_params.py">params</a>) -> <a href="./src/tmdb_client/types/movie_rating_delete_response.py">MovieRatingDeleteResponse</a></code>
- <code title="get /3/search/movie">client.movies.<a href="./src/tmdb_client/resources/movies/movies.py">search</a>(\*\*<a href="src/tmdb_client/types/movie_search_params.py">params</a>) -> <a href="./src/tmdb_client/types/movie_search_response.py">MovieSearchResponse</a></code>

## Images

Types:

```python
from tmdb_client.types.movies import ImageRetrieveResponse
```

Methods:

- <code title="get /3/movie/{movie_id}/images">client.movies.images.<a href="./src/tmdb_client/resources/movies/images.py">retrieve</a>(movie_id, \*\*<a href="src/tmdb_client/types/movies/image_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/movies/image_retrieve_response.py">ImageRetrieveResponse</a></code>

## AccountStates

Types:

```python
from tmdb_client.types.movies import AccountStateRetrieveResponse
```

Methods:

- <code title="get /3/movie/{movie_id}/account_states">client.movies.account_states.<a href="./src/tmdb_client/resources/movies/account_states.py">retrieve</a>(movie_id, \*\*<a href="src/tmdb_client/types/movies/account_state_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/movies/account_state_retrieve_response.py">AccountStateRetrieveResponse</a></code>

## AlternativeTitles

Types:

```python
from tmdb_client.types.movies import AlternativeTitleRetrieveResponse
```

Methods:

- <code title="get /3/movie/{movie_id}/alternative_titles">client.movies.alternative_titles.<a href="./src/tmdb_client/resources/movies/alternative_titles.py">retrieve</a>(movie_id, \*\*<a href="src/tmdb_client/types/movies/alternative_title_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/movies/alternative_title_retrieve_response.py">AlternativeTitleRetrieveResponse</a></code>

## Changes

Types:

```python
from tmdb_client.types.movies import ChangeRetrieveResponse, ChangeListResponse
```

Methods:

- <code title="get /3/movie/{movie_id}/changes">client.movies.changes.<a href="./src/tmdb_client/resources/movies/changes.py">retrieve</a>(movie_id, \*\*<a href="src/tmdb_client/types/movies/change_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/movies/change_retrieve_response.py">ChangeRetrieveResponse</a></code>
- <code title="get /3/movie/changes">client.movies.changes.<a href="./src/tmdb_client/resources/movies/changes.py">list</a>(\*\*<a href="src/tmdb_client/types/movies/change_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/movies/change_list_response.py">ChangeListResponse</a></code>

## Credits

Types:

```python
from tmdb_client.types.movies import CreditRetrieveResponse
```

Methods:

- <code title="get /3/movie/{movie_id}/credits">client.movies.credits.<a href="./src/tmdb_client/resources/movies/credits.py">retrieve</a>(movie_id, \*\*<a href="src/tmdb_client/types/movies/credit_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/movies/credit_retrieve_response.py">CreditRetrieveResponse</a></code>

## ExternalIDs

Types:

```python
from tmdb_client.types.movies import ExternalIDRetrieveResponse
```

Methods:

- <code title="get /3/movie/{movie_id}/external_ids">client.movies.external_ids.<a href="./src/tmdb_client/resources/movies/external_ids.py">retrieve</a>(movie_id) -> <a href="./src/tmdb_client/types/movies/external_id_retrieve_response.py">ExternalIDRetrieveResponse</a></code>

## Keywords

Types:

```python
from tmdb_client.types.movies import KeywordRetrieveResponse
```

Methods:

- <code title="get /3/movie/{movie_id}/keywords">client.movies.keywords.<a href="./src/tmdb_client/resources/movies/keywords.py">retrieve</a>(movie_id) -> <a href="./src/tmdb_client/types/movies/keyword_retrieve_response.py">KeywordRetrieveResponse</a></code>

## Lists

Types:

```python
from tmdb_client.types.movies import ListRetrieveResponse
```

Methods:

- <code title="get /3/movie/{movie_id}/lists">client.movies.lists.<a href="./src/tmdb_client/resources/movies/lists.py">retrieve</a>(movie_id, \*\*<a href="src/tmdb_client/types/movies/list_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/movies/list_retrieve_response.py">ListRetrieveResponse</a></code>

## Recommendations

Types:

```python
from tmdb_client.types.movies import RecommendationRetrieveResponse
```

Methods:

- <code title="get /3/movie/{movie_id}/recommendations">client.movies.recommendations.<a href="./src/tmdb_client/resources/movies/recommendations.py">retrieve</a>(movie_id, \*\*<a href="src/tmdb_client/types/movies/recommendation_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/movies/recommendation_retrieve_response.py">object</a></code>

## ReleaseDates

Types:

```python
from tmdb_client.types.movies import ReleaseDateRetrieveResponse
```

Methods:

- <code title="get /3/movie/{movie_id}/release_dates">client.movies.release_dates.<a href="./src/tmdb_client/resources/movies/release_dates.py">retrieve</a>(movie_id) -> <a href="./src/tmdb_client/types/movies/release_date_retrieve_response.py">ReleaseDateRetrieveResponse</a></code>

## Reviews

Types:

```python
from tmdb_client.types.movies import ReviewListResponse
```

Methods:

- <code title="get /3/movie/{movie_id}/reviews">client.movies.reviews.<a href="./src/tmdb_client/resources/movies/reviews.py">list</a>(movie_id, \*\*<a href="src/tmdb_client/types/movies/review_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/movies/review_list_response.py">ReviewListResponse</a></code>

## Similar

Types:

```python
from tmdb_client.types.movies import SimilarListResponse
```

Methods:

- <code title="get /3/movie/{movie_id}/similar">client.movies.similar.<a href="./src/tmdb_client/resources/movies/similar.py">list</a>(movie_id, \*\*<a href="src/tmdb_client/types/movies/similar_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/movies/similar_list_response.py">SimilarListResponse</a></code>

## Translations

Types:

```python
from tmdb_client.types.movies import TranslationListResponse
```

Methods:

- <code title="get /3/movie/{movie_id}/translations">client.movies.translations.<a href="./src/tmdb_client/resources/movies/translations.py">list</a>(movie_id) -> <a href="./src/tmdb_client/types/movies/translation_list_response.py">TranslationListResponse</a></code>

## Videos

Types:

```python
from tmdb_client.types.movies import VideoListResponse
```

Methods:

- <code title="get /3/movie/{movie_id}/videos">client.movies.videos.<a href="./src/tmdb_client/resources/movies/videos.py">list</a>(movie_id, \*\*<a href="src/tmdb_client/types/movies/video_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/movies/video_list_response.py">VideoListResponse</a></code>

## WatchProviders

Types:

```python
from tmdb_client.types.movies import WatchProviderListResponse
```

Methods:

- <code title="get /3/movie/{movie_id}/watch/providers">client.movies.watch_providers.<a href="./src/tmdb_client/resources/movies/watch_providers.py">list</a>(movie_id) -> <a href="./src/tmdb_client/types/movies/watch_provider_list_response.py">WatchProviderListResponse</a></code>

## Popular

Types:

```python
from tmdb_client.types.movies import PopularListResponse
```

Methods:

- <code title="get /3/movie/popular">client.movies.popular.<a href="./src/tmdb_client/resources/movies/popular.py">list</a>(\*\*<a href="src/tmdb_client/types/movies/popular_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/movies/popular_list_response.py">PopularListResponse</a></code>

## TopRated

Types:

```python
from tmdb_client.types.movies import TopRatedListResponse
```

Methods:

- <code title="get /3/movie/top_rated">client.movies.top_rated.<a href="./src/tmdb_client/resources/movies/top_rated.py">list</a>(\*\*<a href="src/tmdb_client/types/movies/top_rated_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/movies/top_rated_list_response.py">TopRatedListResponse</a></code>

## Upcoming

Types:

```python
from tmdb_client.types.movies import UpcomingListResponse
```

Methods:

- <code title="get /3/movie/upcoming">client.movies.upcoming.<a href="./src/tmdb_client/resources/movies/upcoming.py">list</a>(\*\*<a href="src/tmdb_client/types/movies/upcoming_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/movies/upcoming_list_response.py">UpcomingListResponse</a></code>

## NowPlaying

Types:

```python
from tmdb_client.types.movies import NowPlayingListResponse
```

Methods:

- <code title="get /3/movie/now_playing">client.movies.now_playing.<a href="./src/tmdb_client/resources/movies/now_playing.py">list</a>(\*\*<a href="src/tmdb_client/types/movies/now_playing_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/movies/now_playing_list_response.py">NowPlayingListResponse</a></code>

## Latest

Types:

```python
from tmdb_client.types.movies import LatestRetrieveResponse
```

Methods:

- <code title="get /3/movie/latest">client.movies.latest.<a href="./src/tmdb_client/resources/movies/latest.py">retrieve</a>() -> <a href="./src/tmdb_client/types/movies/latest_retrieve_response.py">LatestRetrieveResponse</a></code>

# Tv

Types:

```python
from tmdb_client.types import TvRetrieveResponse, TvSearchResponse
```

Methods:

- <code title="get /3/tv/{series_id}">client.tv.<a href="./src/tmdb_client/resources/tv/tv.py">retrieve</a>(series_id, \*\*<a href="src/tmdb_client/types/tv_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv_retrieve_response.py">TvRetrieveResponse</a></code>
- <code title="get /3/search/tv">client.tv.<a href="./src/tmdb_client/resources/tv/tv.py">search</a>(\*\*<a href="src/tmdb_client/types/tv_search_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv_search_response.py">TvSearchResponse</a></code>

## Seasons

Types:

```python
from tmdb_client.types.tv import SeasonRetrieveResponse
```

Methods:

- <code title="get /3/tv/{series_id}/season/{season_number}">client.tv.seasons.<a href="./src/tmdb_client/resources/tv/seasons/seasons.py">retrieve</a>(season_number, \*, series_id, \*\*<a href="src/tmdb_client/types/tv/season_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv/season_retrieve_response.py">SeasonRetrieveResponse</a></code>

### Episodes

Types:

```python
from tmdb_client.types.tv.seasons import EpisodeRetrieveResponse
```

Methods:

- <code title="get /3/tv/{series_id}/season/{season_number}/episode/{episode_number}">client.tv.seasons.episodes.<a href="./src/tmdb_client/resources/tv/seasons/episodes/episodes.py">retrieve</a>(episode_number, \*, series_id, season_number, \*\*<a href="src/tmdb_client/types/tv/seasons/episode_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv/seasons/episode_retrieve_response.py">EpisodeRetrieveResponse</a></code>

#### Images

Types:

```python
from tmdb_client.types.tv.seasons.episodes import ImageRetrieveResponse
```

Methods:

- <code title="get /3/tv/{series_id}/season/{season_number}/episode/{episode_number}/images">client.tv.seasons.episodes.images.<a href="./src/tmdb_client/resources/tv/seasons/episodes/images.py">retrieve</a>(episode_number, \*, series_id, season_number, \*\*<a href="src/tmdb_client/types/tv/seasons/episodes/image_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv/seasons/episodes/image_retrieve_response.py">ImageRetrieveResponse</a></code>

#### Credits

Types:

```python
from tmdb_client.types.tv.seasons.episodes import CreditRetrieveResponse
```

Methods:

- <code title="get /3/tv/{series_id}/season/{season_number}/episode/{episode_number}/credits">client.tv.seasons.episodes.credits.<a href="./src/tmdb_client/resources/tv/seasons/episodes/credits.py">retrieve</a>(episode_number, \*, series_id, season_number, \*\*<a href="src/tmdb_client/types/tv/seasons/episodes/credit_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv/seasons/episodes/credit_retrieve_response.py">CreditRetrieveResponse</a></code>

#### ExternalIDs

Types:

```python
from tmdb_client.types.tv.seasons.episodes import ExternalIDListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/season/{season_number}/episode/{episode_number}/external_ids">client.tv.seasons.episodes.external_ids.<a href="./src/tmdb_client/resources/tv/seasons/episodes/external_ids.py">list</a>(episode_number, \*, series_id, season_number) -> <a href="./src/tmdb_client/types/tv/seasons/episodes/external_id_list_response.py">ExternalIDListResponse</a></code>

#### Translations

Types:

```python
from tmdb_client.types.tv.seasons.episodes import TranslationListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/season/{season_number}/episode/{episode_number}/translations">client.tv.seasons.episodes.translations.<a href="./src/tmdb_client/resources/tv/seasons/episodes/translations.py">list</a>(episode_number, \*, series_id, season_number) -> <a href="./src/tmdb_client/types/tv/seasons/episodes/translation_list_response.py">TranslationListResponse</a></code>

### Images

Types:

```python
from tmdb_client.types.tv.seasons import ImageRetrieveResponse
```

Methods:

- <code title="get /3/tv/{series_id}/season/{season_number}/images">client.tv.seasons.images.<a href="./src/tmdb_client/resources/tv/seasons/images.py">retrieve</a>(season_number, \*, series_id, \*\*<a href="src/tmdb_client/types/tv/seasons/image_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv/seasons/image_retrieve_response.py">ImageRetrieveResponse</a></code>

### AccountStates

Types:

```python
from tmdb_client.types.tv.seasons import AccountStateRetrieveResponse
```

Methods:

- <code title="get /3/tv/{series_id}/season/{season_number}/account_states">client.tv.seasons.account_states.<a href="./src/tmdb_client/resources/tv/seasons/account_states.py">retrieve</a>(season_number, \*, series_id, \*\*<a href="src/tmdb_client/types/tv/seasons/account_state_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv/seasons/account_state_retrieve_response.py">AccountStateRetrieveResponse</a></code>

### AggregateCredits

Types:

```python
from tmdb_client.types.tv.seasons import AggregateCreditRetrieveResponse
```

Methods:

- <code title="get /3/tv/{series_id}/season/{season_number}/aggregate_credits">client.tv.seasons.aggregate_credits.<a href="./src/tmdb_client/resources/tv/seasons/aggregate_credits.py">retrieve</a>(season_number, \*, series_id, \*\*<a href="src/tmdb_client/types/tv/seasons/aggregate_credit_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv/seasons/aggregate_credit_retrieve_response.py">AggregateCreditRetrieveResponse</a></code>

### Changes

Types:

```python
from tmdb_client.types.tv.seasons import ChangeRetrieveResponse
```

Methods:

- <code title="get /3/tv/season/{season_id}/changes">client.tv.seasons.changes.<a href="./src/tmdb_client/resources/tv/seasons/changes.py">retrieve</a>(season_id, \*\*<a href="src/tmdb_client/types/tv/seasons/change_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv/seasons/change_retrieve_response.py">ChangeRetrieveResponse</a></code>

### Credits

Types:

```python
from tmdb_client.types.tv.seasons import CreditRetrieveResponse
```

Methods:

- <code title="get /3/tv/{series_id}/season/{season_number}/credits">client.tv.seasons.credits.<a href="./src/tmdb_client/resources/tv/seasons/credits.py">retrieve</a>(season_number, \*, series_id, \*\*<a href="src/tmdb_client/types/tv/seasons/credit_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv/seasons/credit_retrieve_response.py">CreditRetrieveResponse</a></code>

### ExternalIDs

Types:

```python
from tmdb_client.types.tv.seasons import ExternalIDListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/season/{season_number}/external_ids">client.tv.seasons.external_ids.<a href="./src/tmdb_client/resources/tv/seasons/external_ids.py">list</a>(season_number, \*, series_id) -> <a href="./src/tmdb_client/types/tv/seasons/external_id_list_response.py">ExternalIDListResponse</a></code>

### Translations

Types:

```python
from tmdb_client.types.tv.seasons import TranslationListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/season/{season_number}/translations">client.tv.seasons.translations.<a href="./src/tmdb_client/resources/tv/seasons/translations.py">list</a>(season_number, \*, series_id) -> <a href="./src/tmdb_client/types/tv/seasons/translation_list_response.py">TranslationListResponse</a></code>

### Videos

Types:

```python
from tmdb_client.types.tv.seasons import VideoListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/season/{season_number}/videos">client.tv.seasons.videos.<a href="./src/tmdb_client/resources/tv/seasons/videos.py">list</a>(season_number, \*, series_id, \*\*<a href="src/tmdb_client/types/tv/seasons/video_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv/seasons/video_list_response.py">VideoListResponse</a></code>

### WatchProviders

Types:

```python
from tmdb_client.types.tv.seasons import WatchProviderListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/season/{season_number}/watch/providers">client.tv.seasons.watch_providers.<a href="./src/tmdb_client/resources/tv/seasons/watch_providers.py">list</a>(season_number, \*, series_id, \*\*<a href="src/tmdb_client/types/tv/seasons/watch_provider_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv/seasons/watch_provider_list_response.py">WatchProviderListResponse</a></code>

## Images

Types:

```python
from tmdb_client.types.tv import ImageRetrieveResponse
```

Methods:

- <code title="get /3/tv/{series_id}/images">client.tv.images.<a href="./src/tmdb_client/resources/tv/images.py">retrieve</a>(series_id, \*\*<a href="src/tmdb_client/types/tv/image_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv/image_retrieve_response.py">ImageRetrieveResponse</a></code>

## AccountStates

Types:

```python
from tmdb_client.types.tv import AccountStateRetrieveResponse
```

Methods:

- <code title="get /3/tv/{series_id}/account_states">client.tv.account_states.<a href="./src/tmdb_client/resources/tv/account_states.py">retrieve</a>(series_id, \*\*<a href="src/tmdb_client/types/tv/account_state_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv/account_state_retrieve_response.py">AccountStateRetrieveResponse</a></code>

## Episodes

### Videos

Types:

```python
from tmdb_client.types.tv.episodes import VideoListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/season/{season_number}/episode/{episode_number}/videos">client.tv.episodes.videos.<a href="./src/tmdb_client/resources/tv/episodes/videos.py">list</a>(episode_number, \*, series_id, season_number, \*\*<a href="src/tmdb_client/types/tv/episodes/video_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv/episodes/video_list_response.py">VideoListResponse</a></code>

### Rating

Types:

```python
from tmdb_client.types.tv.episodes import RatingDeleteResponse
```

Methods:

- <code title="delete /3/tv/{series_id}/season/{season_number}/episode/{episode_number}/rating">client.tv.episodes.rating.<a href="./src/tmdb_client/resources/tv/episodes/rating.py">delete</a>(episode_number, \*, series_id, season_number, \*\*<a href="src/tmdb_client/types/tv/episodes/rating_delete_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv/episodes/rating_delete_response.py">RatingDeleteResponse</a></code>

## Changes

Types:

```python
from tmdb_client.types.tv import ChangeListResponse
```

Methods:

- <code title="get /3/tv/changes">client.tv.changes.<a href="./src/tmdb_client/resources/tv/changes.py">list</a>(\*\*<a href="src/tmdb_client/types/tv/change_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv/change_list_response.py">ChangeListResponse</a></code>

## Episode

### Changes

Types:

```python
from tmdb_client.types.tv.episode import ChangeListResponse
```

Methods:

- <code title="get /3/tv/episode/{episode_id}/changes">client.tv.episode.changes.<a href="./src/tmdb_client/resources/tv/episode/changes.py">list</a>(episode_id) -> <a href="./src/tmdb_client/types/tv/episode/change_list_response.py">ChangeListResponse</a></code>

## EpisodeGroup

Types:

```python
from tmdb_client.types.tv import EpisodeGroupRetrieveResponse
```

Methods:

- <code title="get /3/tv/episode_group/{tv_episode_group_id}">client.tv.episode_group.<a href="./src/tmdb_client/resources/tv/episode_group.py">retrieve</a>(tv_episode_group_id) -> <a href="./src/tmdb_client/types/tv/episode_group_retrieve_response.py">EpisodeGroupRetrieveResponse</a></code>

# Search

Types:

```python
from tmdb_client.types import SearchCollectionResponse, SearchCompanyResponse, SearchMultiResponse
```

Methods:

- <code title="get /3/search/collection">client.search.<a href="./src/tmdb_client/resources/search.py">collection</a>(\*\*<a href="src/tmdb_client/types/search_collection_params.py">params</a>) -> <a href="./src/tmdb_client/types/search_collection_response.py">SearchCollectionResponse</a></code>
- <code title="get /3/search/company">client.search.<a href="./src/tmdb_client/resources/search.py">company</a>(\*\*<a href="src/tmdb_client/types/search_company_params.py">params</a>) -> <a href="./src/tmdb_client/types/search_company_response.py">SearchCompanyResponse</a></code>
- <code title="get /3/search/multi">client.search.<a href="./src/tmdb_client/resources/search.py">multi</a>(\*\*<a href="src/tmdb_client/types/search_multi_params.py">params</a>) -> <a href="./src/tmdb_client/types/search_multi_response.py">SearchMultiResponse</a></code>

# People

Types:

```python
from tmdb_client.types import (
    PersonRetrieveResponse,
    PersonExternalIDsResponse,
    PersonSearchResponse,
    PersonTaggedImagesResponse,
    PersonTranslationsResponse,
)
```

Methods:

- <code title="get /3/person/{person_id}">client.people.<a href="./src/tmdb_client/resources/people/people.py">retrieve</a>(person_id, \*\*<a href="src/tmdb_client/types/person_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/person_retrieve_response.py">PersonRetrieveResponse</a></code>
- <code title="get /3/person/{person_id}/external_ids">client.people.<a href="./src/tmdb_client/resources/people/people.py">external_ids</a>(person_id) -> <a href="./src/tmdb_client/types/person_external_ids_response.py">PersonExternalIDsResponse</a></code>
- <code title="get /3/search/person">client.people.<a href="./src/tmdb_client/resources/people/people.py">search</a>(\*\*<a href="src/tmdb_client/types/person_search_params.py">params</a>) -> <a href="./src/tmdb_client/types/person_search_response.py">PersonSearchResponse</a></code>
- <code title="get /3/person/{person_id}/tagged_images">client.people.<a href="./src/tmdb_client/resources/people/people.py">tagged_images</a>(person_id, \*\*<a href="src/tmdb_client/types/person_tagged_images_params.py">params</a>) -> <a href="./src/tmdb_client/types/person_tagged_images_response.py">PersonTaggedImagesResponse</a></code>
- <code title="get /3/person/{person_id}/translations">client.people.<a href="./src/tmdb_client/resources/people/people.py">translations</a>(person_id) -> <a href="./src/tmdb_client/types/person_translations_response.py">PersonTranslationsResponse</a></code>

## Changes

Types:

```python
from tmdb_client.types.people import ChangeListResponse
```

Methods:

- <code title="get /3/person/changes">client.people.changes.<a href="./src/tmdb_client/resources/people/changes.py">list</a>(\*\*<a href="src/tmdb_client/types/people/change_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/people/change_list_response.py">ChangeListResponse</a></code>

## Images

Types:

```python
from tmdb_client.types.people import ImageListResponse
```

Methods:

- <code title="get /3/person/{person_id}/images">client.people.images.<a href="./src/tmdb_client/resources/people/images.py">list</a>(person_id) -> <a href="./src/tmdb_client/types/people/image_list_response.py">ImageListResponse</a></code>

## MovieCredits

Types:

```python
from tmdb_client.types.people import MovieCreditListResponse
```

Methods:

- <code title="get /3/person/{person_id}/movie_credits">client.people.movie_credits.<a href="./src/tmdb_client/resources/people/movie_credits.py">list</a>(person_id, \*\*<a href="src/tmdb_client/types/people/movie_credit_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/people/movie_credit_list_response.py">MovieCreditListResponse</a></code>

## TvCredits

Types:

```python
from tmdb_client.types.people import TvCreditListResponse
```

Methods:

- <code title="get /3/person/{person_id}/tv_credits">client.people.tv_credits.<a href="./src/tmdb_client/resources/people/tv_credits.py">list</a>(person_id, \*\*<a href="src/tmdb_client/types/people/tv_credit_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/people/tv_credit_list_response.py">TvCreditListResponse</a></code>

## CombinedCredits

Types:

```python
from tmdb_client.types.people import CombinedCreditListResponse
```

Methods:

- <code title="get /3/person/{person_id}/combined_credits">client.people.combined_credits.<a href="./src/tmdb_client/resources/people/combined_credits.py">list</a>(person_id, \*\*<a href="src/tmdb_client/types/people/combined_credit_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/people/combined_credit_list_response.py">CombinedCreditListResponse</a></code>

## Popular

Types:

```python
from tmdb_client.types.people import PopularListResponse
```

Methods:

- <code title="get /3/person/popular">client.people.popular.<a href="./src/tmdb_client/resources/people/popular.py">list</a>(\*\*<a href="src/tmdb_client/types/people/popular_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/people/popular_list_response.py">PopularListResponse</a></code>

# Configuration

Types:

```python
from tmdb_client.types import ConfigurationRetrieveResponse
```

Methods:

- <code title="get /3/configuration">client.configuration.<a href="./src/tmdb_client/resources/configuration/configuration.py">retrieve</a>() -> <a href="./src/tmdb_client/types/configuration_retrieve_response.py">ConfigurationRetrieveResponse</a></code>

## Countries

Types:

```python
from tmdb_client.types.configuration import CountryListResponse
```

Methods:

- <code title="get /3/configuration/countries">client.configuration.countries.<a href="./src/tmdb_client/resources/configuration/countries.py">list</a>(\*\*<a href="src/tmdb_client/types/configuration/country_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/configuration/country_list_response.py">CountryListResponse</a></code>

## Jobs

Types:

```python
from tmdb_client.types.configuration import JobListResponse
```

Methods:

- <code title="get /3/configuration/jobs">client.configuration.jobs.<a href="./src/tmdb_client/resources/configuration/jobs.py">list</a>() -> <a href="./src/tmdb_client/types/configuration/job_list_response.py">JobListResponse</a></code>

## Languages

Types:

```python
from tmdb_client.types.configuration import LanguageListResponse
```

Methods:

- <code title="get /3/configuration/languages">client.configuration.languages.<a href="./src/tmdb_client/resources/configuration/languages.py">list</a>() -> <a href="./src/tmdb_client/types/configuration/language_list_response.py">LanguageListResponse</a></code>

## PrimaryTranslations

Types:

```python
from tmdb_client.types.configuration import PrimaryTranslationListResponse
```

Methods:

- <code title="get /3/configuration/primary_translations">client.configuration.primary_translations.<a href="./src/tmdb_client/resources/configuration/primary_translations.py">list</a>() -> <a href="./src/tmdb_client/types/configuration/primary_translation_list_response.py">PrimaryTranslationListResponse</a></code>

## Timezones

Types:

```python
from tmdb_client.types.configuration import TimezoneListResponse
```

Methods:

- <code title="get /3/configuration/timezones">client.configuration.timezones.<a href="./src/tmdb_client/resources/configuration/timezones.py">list</a>() -> <a href="./src/tmdb_client/types/configuration/timezone_list_response.py">TimezoneListResponse</a></code>

# DiscoverTv

Types:

```python
from tmdb_client.types import DiscoverTvListResponse
```

Methods:

- <code title="get /3/discover/tv">client.discover_tv.<a href="./src/tmdb_client/resources/discover_tv.py">list</a>(\*\*<a href="src/tmdb_client/types/discover_tv_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/discover_tv_list_response.py">DiscoverTvListResponse</a></code>

# Trending

Types:

```python
from tmdb_client.types import TrendingListResponse
```

Methods:

- <code title="get /3/trending/all/{time_window}">client.trending.<a href="./src/tmdb_client/resources/trending.py">list</a>(time_window, \*\*<a href="src/tmdb_client/types/trending_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/trending_list_response.py">TrendingListResponse</a></code>

# TrendingMovies

Types:

```python
from tmdb_client.types import TrendingMovieListResponse
```

Methods:

- <code title="get /3/trending/movie/{time_window}">client.trending_movies.<a href="./src/tmdb_client/resources/trending_movies.py">list</a>(time_window, \*\*<a href="src/tmdb_client/types/trending_movie_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/trending_movie_list_response.py">TrendingMovieListResponse</a></code>

# TrendingTvShows

Types:

```python
from tmdb_client.types import TrendingTvShowListResponse
```

Methods:

- <code title="get /3/trending/tv/{time_window}">client.trending_tv_shows.<a href="./src/tmdb_client/resources/trending_tv_shows.py">list</a>(time_window, \*\*<a href="src/tmdb_client/types/trending_tv_show_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/trending_tv_show_list_response.py">TrendingTvShowListResponse</a></code>

# Episodes

Types:

```python
from tmdb_client.types import EpisodeAccountStatesResponse
```

Methods:

- <code title="get /3/tv/{series_id}/season/{season_number}/episode/{episode_number}/account_states">client.episodes.<a href="./src/tmdb_client/resources/episodes.py">account_states</a>(episode_number, \*, series_id, season_number, \*\*<a href="src/tmdb_client/types/episode_account_states_params.py">params</a>) -> <a href="./src/tmdb_client/types/episode_account_states_response.py">EpisodeAccountStatesResponse</a></code>

# TrendingPeople

Types:

```python
from tmdb_client.types import TrendingPersonListResponse
```

Methods:

- <code title="get /3/trending/person/{time_window}">client.trending_people.<a href="./src/tmdb_client/resources/trending_people.py">list</a>(time_window, \*\*<a href="src/tmdb_client/types/trending_person_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/trending_person_list_response.py">TrendingPersonListResponse</a></code>

# Authentication

Types:

```python
from tmdb_client.types import AuthenticationTestKeyResponse
```

Methods:

- <code title="get /3/authentication">client.authentication.<a href="./src/tmdb_client/resources/authentication/authentication.py">test_key</a>() -> <a href="./src/tmdb_client/types/authentication_test_key_response.py">AuthenticationTestKeyResponse</a></code>

## GuestSession

Types:

```python
from tmdb_client.types.authentication import GuestSessionNewResponse
```

Methods:

- <code title="get /3/authentication/guest_session/new">client.authentication.guest_session.<a href="./src/tmdb_client/resources/authentication/guest_session.py">new</a>() -> <a href="./src/tmdb_client/types/authentication/guest_session_new_response.py">GuestSessionNewResponse</a></code>

## Token

Types:

```python
from tmdb_client.types.authentication import TokenNewResponse, TokenValidateWithLoginResponse
```

Methods:

- <code title="get /3/authentication/token/new">client.authentication.token.<a href="./src/tmdb_client/resources/authentication/token.py">new</a>() -> <a href="./src/tmdb_client/types/authentication/token_new_response.py">TokenNewResponse</a></code>
- <code title="post /3/authentication/token/validate_with_login">client.authentication.token.<a href="./src/tmdb_client/resources/authentication/token.py">validate_with_login</a>(\*\*<a href="src/tmdb_client/types/authentication/token_validate_with_login_params.py">params</a>) -> <a href="./src/tmdb_client/types/authentication/token_validate_with_login_response.py">TokenValidateWithLoginResponse</a></code>

## Session

Types:

```python
from tmdb_client.types.authentication import (
    SessionDeleteResponse,
    SessionConvertResponse,
    SessionNewResponse,
)
```

Methods:

- <code title="delete /3/authentication/session">client.authentication.session.<a href="./src/tmdb_client/resources/authentication/session.py">delete</a>(\*\*<a href="src/tmdb_client/types/authentication/session_delete_params.py">params</a>) -> <a href="./src/tmdb_client/types/authentication/session_delete_response.py">SessionDeleteResponse</a></code>
- <code title="post /3/authentication/session/convert/4">client.authentication.session.<a href="./src/tmdb_client/resources/authentication/session.py">convert</a>(\*\*<a href="src/tmdb_client/types/authentication/session_convert_params.py">params</a>) -> <a href="./src/tmdb_client/types/authentication/session_convert_response.py">SessionConvertResponse</a></code>
- <code title="post /3/authentication/session/new">client.authentication.session.<a href="./src/tmdb_client/resources/authentication/session.py">new</a>(\*\*<a href="src/tmdb_client/types/authentication/session_new_params.py">params</a>) -> <a href="./src/tmdb_client/types/authentication/session_new_response.py">SessionNewResponse</a></code>

# Find

Types:

```python
from tmdb_client.types import FindRetrieveResponse
```

Methods:

- <code title="get /3/find/{external_id}">client.find.<a href="./src/tmdb_client/resources/find.py">retrieve</a>(external_id, \*\*<a href="src/tmdb_client/types/find_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/find_retrieve_response.py">FindRetrieveResponse</a></code>

# TvShows

## Changes

Types:

```python
from tmdb_client.types.tv_shows import ChangeListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/changes">client.tv_shows.changes.<a href="./src/tmdb_client/resources/tv_shows/changes.py">list</a>(series_id, \*\*<a href="src/tmdb_client/types/tv_shows/change_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv_shows/change_list_response.py">ChangeListResponse</a></code>

## AiringToday

Types:

```python
from tmdb_client.types.tv_shows import AiringTodayListResponse
```

Methods:

- <code title="get /3/tv/airing_today">client.tv_shows.airing_today.<a href="./src/tmdb_client/resources/tv_shows/airing_today.py">list</a>(\*\*<a href="src/tmdb_client/types/tv_shows/airing_today_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv_shows/airing_today_list_response.py">AiringTodayListResponse</a></code>

## OnTheAir

Types:

```python
from tmdb_client.types.tv_shows import OnTheAirListResponse
```

Methods:

- <code title="get /3/tv/on_the_air">client.tv_shows.on_the_air.<a href="./src/tmdb_client/resources/tv_shows/on_the_air.py">list</a>(\*\*<a href="src/tmdb_client/types/tv_shows/on_the_air_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv_shows/on_the_air_list_response.py">OnTheAirListResponse</a></code>

## Popular

Types:

```python
from tmdb_client.types.tv_shows import PopularListResponse
```

Methods:

- <code title="get /3/tv/popular">client.tv_shows.popular.<a href="./src/tmdb_client/resources/tv_shows/popular.py">list</a>(\*\*<a href="src/tmdb_client/types/tv_shows/popular_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv_shows/popular_list_response.py">PopularListResponse</a></code>

## TopRated

Types:

```python
from tmdb_client.types.tv_shows import TopRatedListResponse
```

Methods:

- <code title="get /3/tv/top_rated">client.tv_shows.top_rated.<a href="./src/tmdb_client/resources/tv_shows/top_rated.py">list</a>(\*\*<a href="src/tmdb_client/types/tv_shows/top_rated_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv_shows/top_rated_list_response.py">TopRatedListResponse</a></code>

## Latest

Types:

```python
from tmdb_client.types.tv_shows import LatestRetrieveResponse
```

Methods:

- <code title="get /3/tv/latest">client.tv_shows.latest.<a href="./src/tmdb_client/resources/tv_shows/latest.py">retrieve</a>() -> <a href="./src/tmdb_client/types/tv_shows/latest_retrieve_response.py">LatestRetrieveResponse</a></code>

## AggregateCredits

Types:

```python
from tmdb_client.types.tv_shows import AggregateCreditRetrieveResponse
```

Methods:

- <code title="get /3/tv/{series_id}/aggregate_credits">client.tv_shows.aggregate_credits.<a href="./src/tmdb_client/resources/tv_shows/aggregate_credits.py">retrieve</a>(series_id, \*\*<a href="src/tmdb_client/types/tv_shows/aggregate_credit_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv_shows/aggregate_credit_retrieve_response.py">AggregateCreditRetrieveResponse</a></code>

## AlternativeTitles

Types:

```python
from tmdb_client.types.tv_shows import AlternativeTitleRetrieveResponse
```

Methods:

- <code title="get /3/tv/{series_id}/alternative_titles">client.tv_shows.alternative_titles.<a href="./src/tmdb_client/resources/tv_shows/alternative_titles.py">retrieve</a>(series_id) -> <a href="./src/tmdb_client/types/tv_shows/alternative_title_retrieve_response.py">AlternativeTitleRetrieveResponse</a></code>

## ContentRatings

Types:

```python
from tmdb_client.types.tv_shows import ContentRatingRetrieveResponse
```

Methods:

- <code title="get /3/tv/{series_id}/content_ratings">client.tv_shows.content_ratings.<a href="./src/tmdb_client/resources/tv_shows/content_ratings.py">retrieve</a>(series_id) -> <a href="./src/tmdb_client/types/tv_shows/content_rating_retrieve_response.py">ContentRatingRetrieveResponse</a></code>

## Credits

Types:

```python
from tmdb_client.types.tv_shows import CreditRetrieveResponse
```

Methods:

- <code title="get /3/tv/{series_id}/credits">client.tv_shows.credits.<a href="./src/tmdb_client/resources/tv_shows/credits.py">retrieve</a>(series_id, \*\*<a href="src/tmdb_client/types/tv_shows/credit_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv_shows/credit_retrieve_response.py">CreditRetrieveResponse</a></code>

## EpisodeGroups

Types:

```python
from tmdb_client.types.tv_shows import EpisodeGroupRetrieveResponse
```

Methods:

- <code title="get /3/tv/{series_id}/episode_groups">client.tv_shows.episode_groups.<a href="./src/tmdb_client/resources/tv_shows/episode_groups.py">retrieve</a>(series_id) -> <a href="./src/tmdb_client/types/tv_shows/episode_group_retrieve_response.py">EpisodeGroupRetrieveResponse</a></code>

## ExternalIDs

Types:

```python
from tmdb_client.types.tv_shows import ExternalIDListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/external_ids">client.tv_shows.external_ids.<a href="./src/tmdb_client/resources/tv_shows/external_ids.py">list</a>(series_id) -> <a href="./src/tmdb_client/types/tv_shows/external_id_list_response.py">ExternalIDListResponse</a></code>

## Keywords

Types:

```python
from tmdb_client.types.tv_shows import KeywordListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/keywords">client.tv_shows.keywords.<a href="./src/tmdb_client/resources/tv_shows/keywords.py">list</a>(series_id) -> <a href="./src/tmdb_client/types/tv_shows/keyword_list_response.py">KeywordListResponse</a></code>

## Recommendations

Types:

```python
from tmdb_client.types.tv_shows import RecommendationListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/recommendations">client.tv_shows.recommendations.<a href="./src/tmdb_client/resources/tv_shows/recommendations.py">list</a>(series_id, \*\*<a href="src/tmdb_client/types/tv_shows/recommendation_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv_shows/recommendation_list_response.py">RecommendationListResponse</a></code>

## Reviews

Types:

```python
from tmdb_client.types.tv_shows import ReviewListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/reviews">client.tv_shows.reviews.<a href="./src/tmdb_client/resources/tv_shows/reviews.py">list</a>(series_id, \*\*<a href="src/tmdb_client/types/tv_shows/review_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv_shows/review_list_response.py">ReviewListResponse</a></code>

## ScreenedTheatrically

Types:

```python
from tmdb_client.types.tv_shows import ScreenedTheatricallyListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/screened_theatrically">client.tv_shows.screened_theatrically.<a href="./src/tmdb_client/resources/tv_shows/screened_theatrically.py">list</a>(series_id) -> <a href="./src/tmdb_client/types/tv_shows/screened_theatrically_list_response.py">ScreenedTheatricallyListResponse</a></code>

## Similar

Types:

```python
from tmdb_client.types.tv_shows import SimilarListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/similar">client.tv_shows.similar.<a href="./src/tmdb_client/resources/tv_shows/similar.py">list</a>(series_id, \*\*<a href="src/tmdb_client/types/tv_shows/similar_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv_shows/similar_list_response.py">SimilarListResponse</a></code>

## Translations

Types:

```python
from tmdb_client.types.tv_shows import TranslationListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/translations">client.tv_shows.translations.<a href="./src/tmdb_client/resources/tv_shows/translations.py">list</a>(series_id) -> <a href="./src/tmdb_client/types/tv_shows/translation_list_response.py">TranslationListResponse</a></code>

## Videos

Types:

```python
from tmdb_client.types.tv_shows import VideoListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/videos">client.tv_shows.videos.<a href="./src/tmdb_client/resources/tv_shows/videos.py">list</a>(series_id, \*\*<a href="src/tmdb_client/types/tv_shows/video_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv_shows/video_list_response.py">VideoListResponse</a></code>

## WatchProviders

Types:

```python
from tmdb_client.types.tv_shows import WatchProviderListResponse
```

Methods:

- <code title="get /3/tv/{series_id}/watch/providers">client.tv_shows.watch_providers.<a href="./src/tmdb_client/resources/tv_shows/watch_providers.py">list</a>(series_id) -> <a href="./src/tmdb_client/types/tv_shows/watch_provider_list_response.py">WatchProviderListResponse</a></code>

## Rating

Types:

```python
from tmdb_client.types.tv_shows import RatingDeleteResponse, RatingRateResponse
```

Methods:

- <code title="delete /3/tv/{series_id}/rating">client.tv_shows.rating.<a href="./src/tmdb_client/resources/tv_shows/rating.py">delete</a>(series_id, \*\*<a href="src/tmdb_client/types/tv_shows/rating_delete_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv_shows/rating_delete_response.py">RatingDeleteResponse</a></code>
- <code title="post /3/tv/{series_id}/rating">client.tv_shows.rating.<a href="./src/tmdb_client/resources/tv_shows/rating.py">rate</a>(series_id, \*\*<a href="src/tmdb_client/types/tv_shows/rating_rate_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv_shows/rating_rate_response.py">RatingRateResponse</a></code>

# Accounts

Types:

```python
from tmdb_client.types import AccountRetrieveResponse
```

Methods:

- <code title="get /3/account/{account_id}">client.accounts.<a href="./src/tmdb_client/resources/accounts/accounts.py">retrieve</a>(account_id, \*\*<a href="src/tmdb_client/types/account_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/account_retrieve_response.py">AccountRetrieveResponse</a></code>

## Lists

Types:

```python
from tmdb_client.types.accounts import ListListResponse
```

Methods:

- <code title="get /3/account/{account_id}/lists">client.accounts.lists.<a href="./src/tmdb_client/resources/accounts/lists.py">list</a>(account_id, \*\*<a href="src/tmdb_client/types/accounts/list_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/accounts/list_list_response.py">ListListResponse</a></code>

## Favorite

Types:

```python
from tmdb_client.types.accounts import FavoriteCreateResponse
```

Methods:

- <code title="post /3/account/{account_id}/favorite">client.accounts.favorite.<a href="./src/tmdb_client/resources/accounts/favorite/favorite.py">create</a>(account_id, \*\*<a href="src/tmdb_client/types/accounts/favorite_create_params.py">params</a>) -> <a href="./src/tmdb_client/types/accounts/favorite_create_response.py">FavoriteCreateResponse</a></code>

### Movies

Types:

```python
from tmdb_client.types.accounts.favorite import MovieListResponse
```

Methods:

- <code title="get /3/account/{account_id}/favorite/movies">client.accounts.favorite.movies.<a href="./src/tmdb_client/resources/accounts/favorite/movies.py">list</a>(account_id, \*\*<a href="src/tmdb_client/types/accounts/favorite/movie_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/accounts/favorite/movie_list_response.py">MovieListResponse</a></code>

### Tv

Types:

```python
from tmdb_client.types.accounts.favorite import TvListResponse
```

Methods:

- <code title="get /3/account/{account_id}/favorite/tv">client.accounts.favorite.tv.<a href="./src/tmdb_client/resources/accounts/favorite/tv.py">list</a>(account_id, \*\*<a href="src/tmdb_client/types/accounts/favorite/tv_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/accounts/favorite/tv_list_response.py">TvListResponse</a></code>

## Rated

### Movies

Types:

```python
from tmdb_client.types.accounts.rated import MovieListResponse
```

Methods:

- <code title="get /3/account/{account_id}/rated/movies">client.accounts.rated.movies.<a href="./src/tmdb_client/resources/accounts/rated/movies.py">list</a>(account_id, \*\*<a href="src/tmdb_client/types/accounts/rated/movie_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/accounts/rated/movie_list_response.py">MovieListResponse</a></code>

### Tv

Types:

```python
from tmdb_client.types.accounts.rated import TvListResponse
```

Methods:

- <code title="get /3/account/{account_id}/rated/tv">client.accounts.rated.tv.<a href="./src/tmdb_client/resources/accounts/rated/tv.py">list</a>(account_id, \*\*<a href="src/tmdb_client/types/accounts/rated/tv_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/accounts/rated/tv_list_response.py">TvListResponse</a></code>

### TvEpisodes

Types:

```python
from tmdb_client.types.accounts.rated import TvEpisodeListResponse
```

Methods:

- <code title="get /3/account/{account_id}/rated/tv/episodes">client.accounts.rated.tv_episodes.<a href="./src/tmdb_client/resources/accounts/rated/tv_episodes.py">list</a>(account_id, \*\*<a href="src/tmdb_client/types/accounts/rated/tv_episode_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/accounts/rated/tv_episode_list_response.py">TvEpisodeListResponse</a></code>

## WatchlistMovies

Types:

```python
from tmdb_client.types.accounts import WatchlistMovieListResponse
```

Methods:

- <code title="get /3/account/{account_id}/watchlist/movies">client.accounts.watchlist_movies.<a href="./src/tmdb_client/resources/accounts/watchlist_movies.py">list</a>(account_id, \*\*<a href="src/tmdb_client/types/accounts/watchlist_movie_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/accounts/watchlist_movie_list_response.py">WatchlistMovieListResponse</a></code>

## WatchlistTv

Types:

```python
from tmdb_client.types.accounts import WatchlistTvListResponse
```

Methods:

- <code title="get /3/account/{account_id}/watchlist/tv">client.accounts.watchlist_tv.<a href="./src/tmdb_client/resources/accounts/watchlist_tv.py">list</a>(account_id, \*\*<a href="src/tmdb_client/types/accounts/watchlist_tv_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/accounts/watchlist_tv_list_response.py">WatchlistTvListResponse</a></code>

## Watchlist

Types:

```python
from tmdb_client.types.accounts import WatchlistCreateResponse
```

Methods:

- <code title="post /3/account/{account_id}/watchlist">client.accounts.watchlist.<a href="./src/tmdb_client/resources/accounts/watchlist.py">create</a>(account_id, \*\*<a href="src/tmdb_client/types/accounts/watchlist_create_params.py">params</a>) -> <a href="./src/tmdb_client/types/accounts/watchlist_create_response.py">WatchlistCreateResponse</a></code>

# Certifications

## Movie

Types:

```python
from tmdb_client.types.certifications import MovieListResponse
```

Methods:

- <code title="get /3/certification/movie/list">client.certifications.movie.<a href="./src/tmdb_client/resources/certifications/movie.py">list</a>() -> <a href="./src/tmdb_client/types/certifications/movie_list_response.py">MovieListResponse</a></code>

## Tv

Types:

```python
from tmdb_client.types.certifications import TvListResponse
```

Methods:

- <code title="get /3/certification/tv/list">client.certifications.tv.<a href="./src/tmdb_client/resources/certifications/tv.py">list</a>() -> <a href="./src/tmdb_client/types/certifications/tv_list_response.py">TvListResponse</a></code>

# Collections

Types:

```python
from tmdb_client.types import CollectionRetrieveResponse
```

Methods:

- <code title="get /3/collection/{collection_id}">client.collections.<a href="./src/tmdb_client/resources/collections/collections.py">retrieve</a>(collection_id, \*\*<a href="src/tmdb_client/types/collection_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/collection_retrieve_response.py">CollectionRetrieveResponse</a></code>

## Images

Types:

```python
from tmdb_client.types.collections import ImageListResponse
```

Methods:

- <code title="get /3/collection/{collection_id}/images">client.collections.images.<a href="./src/tmdb_client/resources/collections/images.py">list</a>(collection_id, \*\*<a href="src/tmdb_client/types/collections/image_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/collections/image_list_response.py">ImageListResponse</a></code>

## Translations

Types:

```python
from tmdb_client.types.collections import TranslationListResponse
```

Methods:

- <code title="get /3/collection/{collection_id}/translations">client.collections.translations.<a href="./src/tmdb_client/resources/collections/translations.py">list</a>(collection_id) -> <a href="./src/tmdb_client/types/collections/translation_list_response.py">TranslationListResponse</a></code>

# Companies

Types:

```python
from tmdb_client.types import CompanyRetrieveResponse
```

Methods:

- <code title="get /3/company/{company_id}">client.companies.<a href="./src/tmdb_client/resources/companies/companies.py">retrieve</a>(company_id) -> <a href="./src/tmdb_client/types/company_retrieve_response.py">CompanyRetrieveResponse</a></code>

## AlternativeNames

Types:

```python
from tmdb_client.types.companies import AlternativeNameListResponse
```

Methods:

- <code title="get /3/company/{company_id}/alternative_names">client.companies.alternative_names.<a href="./src/tmdb_client/resources/companies/alternative_names.py">list</a>(company_id) -> <a href="./src/tmdb_client/types/companies/alternative_name_list_response.py">AlternativeNameListResponse</a></code>

## Images

Types:

```python
from tmdb_client.types.companies import ImageListResponse
```

Methods:

- <code title="get /3/company/{company_id}/images">client.companies.images.<a href="./src/tmdb_client/resources/companies/images.py">list</a>(company_id) -> <a href="./src/tmdb_client/types/companies/image_list_response.py">ImageListResponse</a></code>

# Credits

Types:

```python
from tmdb_client.types import CreditRetrieveResponse
```

Methods:

- <code title="get /3/credit/{credit_id}">client.credits.<a href="./src/tmdb_client/resources/credits.py">retrieve</a>(credit_id) -> <a href="./src/tmdb_client/types/credit_retrieve_response.py">CreditRetrieveResponse</a></code>

# Genres

## Movies

Types:

```python
from tmdb_client.types.genres import MovieListResponse
```

Methods:

- <code title="get /3/genre/movie/list">client.genres.movies.<a href="./src/tmdb_client/resources/genres/movies.py">list</a>(\*\*<a href="src/tmdb_client/types/genres/movie_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/genres/movie_list_response.py">MovieListResponse</a></code>

## Tv

Types:

```python
from tmdb_client.types.genres import TvListResponse
```

Methods:

- <code title="get /3/genre/tv/list">client.genres.tv.<a href="./src/tmdb_client/resources/genres/tv.py">list</a>(\*\*<a href="src/tmdb_client/types/genres/tv_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/genres/tv_list_response.py">TvListResponse</a></code>

# GuestSessions

## Rated

### Movies

Types:

```python
from tmdb_client.types.guest_sessions.rated import MovieListResponse
```

Methods:

- <code title="get /3/guest_session/{guest_session_id}/rated/movies">client.guest_sessions.rated.movies.<a href="./src/tmdb_client/resources/guest_sessions/rated/movies.py">list</a>(guest_session_id, \*\*<a href="src/tmdb_client/types/guest_sessions/rated/movie_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/guest_sessions/rated/movie_list_response.py">MovieListResponse</a></code>

### Tv

Types:

```python
from tmdb_client.types.guest_sessions.rated import TvListResponse
```

Methods:

- <code title="get /3/guest_session/{guest_session_id}/rated/tv">client.guest_sessions.rated.tv.<a href="./src/tmdb_client/resources/guest_sessions/rated/tv.py">list</a>(guest_session_id, \*\*<a href="src/tmdb_client/types/guest_sessions/rated/tv_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/guest_sessions/rated/tv_list_response.py">TvListResponse</a></code>

## TvEpisodes

Types:

```python
from tmdb_client.types.guest_sessions import TvEpisodeListResponse
```

Methods:

- <code title="get /3/guest_session/{guest_session_id}/rated/tv/episodes">client.guest_sessions.tv_episodes.<a href="./src/tmdb_client/resources/guest_sessions/tv_episodes.py">list</a>(guest_session_id, \*\*<a href="src/tmdb_client/types/guest_sessions/tv_episode_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/guest_sessions/tv_episode_list_response.py">TvEpisodeListResponse</a></code>

# WatchProviders

## Regions

Types:

```python
from tmdb_client.types.watch_providers import RegionListResponse
```

Methods:

- <code title="get /3/watch/providers/regions">client.watch_providers.regions.<a href="./src/tmdb_client/resources/watch_providers/regions.py">list</a>(\*\*<a href="src/tmdb_client/types/watch_providers/region_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/watch_providers/region_list_response.py">RegionListResponse</a></code>

## Movies

Types:

```python
from tmdb_client.types.watch_providers import MovieListResponse
```

Methods:

- <code title="get /3/watch/providers/movie">client.watch_providers.movies.<a href="./src/tmdb_client/resources/watch_providers/movies.py">list</a>(\*\*<a href="src/tmdb_client/types/watch_providers/movie_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/watch_providers/movie_list_response.py">MovieListResponse</a></code>

## TvShows

Types:

```python
from tmdb_client.types.watch_providers import TvShowListResponse
```

Methods:

- <code title="get /3/watch/providers/tv">client.watch_providers.tv_shows.<a href="./src/tmdb_client/resources/watch_providers/tv_shows.py">list</a>(\*\*<a href="src/tmdb_client/types/watch_providers/tv_show_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/watch_providers/tv_show_list_response.py">TvShowListResponse</a></code>

# Keywords

Types:

```python
from tmdb_client.types import KeywordRetrieveResponse, KeywordSearchResponse
```

Methods:

- <code title="get /3/keyword/{keyword_id}">client.keywords.<a href="./src/tmdb_client/resources/keywords/keywords.py">retrieve</a>(keyword_id) -> <a href="./src/tmdb_client/types/keyword_retrieve_response.py">KeywordRetrieveResponse</a></code>
- <code title="get /3/search/keyword">client.keywords.<a href="./src/tmdb_client/resources/keywords/keywords.py">search</a>(\*\*<a href="src/tmdb_client/types/keyword_search_params.py">params</a>) -> <a href="./src/tmdb_client/types/keyword_search_response.py">KeywordSearchResponse</a></code>

## Movies

Types:

```python
from tmdb_client.types.keywords import MovieListResponse
```

Methods:

- <code title="get /3/keyword/{keyword_id}/movies">client.keywords.movies.<a href="./src/tmdb_client/resources/keywords/movies.py">list</a>(keyword_id, \*\*<a href="src/tmdb_client/types/keywords/movie_list_params.py">params</a>) -> <a href="./src/tmdb_client/types/keywords/movie_list_response.py">MovieListResponse</a></code>

# Lists

Types:

```python
from tmdb_client.types import (
    ListCreateResponse,
    ListRetrieveResponse,
    ListDeleteResponse,
    ListAddItemResponse,
    ListClearResponse,
    ListItemStatusResponse,
    ListRemoveItemResponse,
)
```

Methods:

- <code title="post /3/list">client.lists.<a href="./src/tmdb_client/resources/lists.py">create</a>(\*\*<a href="src/tmdb_client/types/list_create_params.py">params</a>) -> <a href="./src/tmdb_client/types/list_create_response.py">ListCreateResponse</a></code>
- <code title="get /3/list/{list_id}">client.lists.<a href="./src/tmdb_client/resources/lists.py">retrieve</a>(list_id, \*\*<a href="src/tmdb_client/types/list_retrieve_params.py">params</a>) -> <a href="./src/tmdb_client/types/list_retrieve_response.py">ListRetrieveResponse</a></code>
- <code title="delete /3/list/{list_id}">client.lists.<a href="./src/tmdb_client/resources/lists.py">delete</a>(list_id, \*\*<a href="src/tmdb_client/types/list_delete_params.py">params</a>) -> <a href="./src/tmdb_client/types/list_delete_response.py">ListDeleteResponse</a></code>
- <code title="post /3/list/{list_id}/add_item">client.lists.<a href="./src/tmdb_client/resources/lists.py">add_item</a>(list_id, \*\*<a href="src/tmdb_client/types/list_add_item_params.py">params</a>) -> <a href="./src/tmdb_client/types/list_add_item_response.py">ListAddItemResponse</a></code>
- <code title="post /3/list/{list_id}/clear">client.lists.<a href="./src/tmdb_client/resources/lists.py">clear</a>(list_id, \*\*<a href="src/tmdb_client/types/list_clear_params.py">params</a>) -> <a href="./src/tmdb_client/types/list_clear_response.py">ListClearResponse</a></code>
- <code title="get /3/list/{list_id}/item_status">client.lists.<a href="./src/tmdb_client/resources/lists.py">item_status</a>(list_id, \*\*<a href="src/tmdb_client/types/list_item_status_params.py">params</a>) -> <a href="./src/tmdb_client/types/list_item_status_response.py">ListItemStatusResponse</a></code>
- <code title="post /3/list/{list_id}/remove_item">client.lists.<a href="./src/tmdb_client/resources/lists.py">remove_item</a>(list_id, \*\*<a href="src/tmdb_client/types/list_remove_item_params.py">params</a>) -> <a href="./src/tmdb_client/types/list_remove_item_response.py">ListRemoveItemResponse</a></code>

# Networks

Types:

```python
from tmdb_client.types import NetworkRetrieveResponse
```

Methods:

- <code title="get /3/network/{network_id}">client.networks.<a href="./src/tmdb_client/resources/networks/networks.py">retrieve</a>(network_id) -> <a href="./src/tmdb_client/types/network_retrieve_response.py">NetworkRetrieveResponse</a></code>

## AlternativeNames

Types:

```python
from tmdb_client.types.networks import AlternativeNameListResponse
```

Methods:

- <code title="get /3/network/{network_id}/alternative_names">client.networks.alternative_names.<a href="./src/tmdb_client/resources/networks/alternative_names.py">list</a>(network_id) -> <a href="./src/tmdb_client/types/networks/alternative_name_list_response.py">AlternativeNameListResponse</a></code>

## Images

Types:

```python
from tmdb_client.types.networks import ImageListResponse
```

Methods:

- <code title="get /3/network/{network_id}/images">client.networks.images.<a href="./src/tmdb_client/resources/networks/images.py">list</a>(network_id) -> <a href="./src/tmdb_client/types/networks/image_list_response.py">ImageListResponse</a></code>

# Reviews

Types:

```python
from tmdb_client.types import ReviewRetrieveResponse
```

Methods:

- <code title="get /3/review/{review_id}">client.reviews.<a href="./src/tmdb_client/resources/reviews.py">retrieve</a>(review_id) -> <a href="./src/tmdb_client/types/review_retrieve_response.py">ReviewRetrieveResponse</a></code>

# Person

## Latest

Types:

```python
from tmdb_client.types.person import LatestRetrieveResponse
```

Methods:

- <code title="get /3/person/latest">client.person.latest.<a href="./src/tmdb_client/resources/person/latest.py">retrieve</a>() -> <a href="./src/tmdb_client/types/person/latest_retrieve_response.py">LatestRetrieveResponse</a></code>

# TvSeries

Types:

```python
from tmdb_client.types import TvSeryListsResponse
```

Methods:

- <code title="get /3/tv/{series_id}/lists">client.tv_series.<a href="./src/tmdb_client/resources/tv_series.py">lists</a>(series_id, \*\*<a href="src/tmdb_client/types/tv_sery_lists_params.py">params</a>) -> <a href="./src/tmdb_client/types/tv_sery_lists_response.py">TvSeryListsResponse</a></code>
