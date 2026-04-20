# Tweeter (X.com) API for SUTRA using Official X.com APIs


```
1) get_user_profile : Retrieves details of a specific User by their username.
GET /tweet-x/users/user/{username}

https://docs.x.com/x-api/users/get-user-by-username#get-user-by-username

```

```
2) search_users : Retrieves a list of Users matching a search query.
GET /tweet-x/users/search/users

https://docs.x.com/enterprise-api/users/search-users#search-users
```

```
3) get_user_follow_counts : returns (user_id, username, followers_count, following_count)
GET /tweet-x/users/{username}/counts

https://docs.x.com/x-api/users/get-user-by-username#get-user-by-username
```

```
4) search_recent_posts : Retrieves Posts from the last 7 days matching a search query. 
GET /tweet-x/tweets/search/recent-posts

https://docs.x.com/x-api/posts/search-recent-posts#search-recent-posts
```

```
5) search_all_posts : Retrieves Posts from the full archive matching a search query.
GET /tweet-x/tweets/search/all-posts

https://docs.x.com/x-api/posts/search-all-posts
```

```
6) count_posts : Retrieves the count of Posts matching a search query from the full archive.
GET /tweet-x/tweets/search/post-count

https://docs.x.com/x-api/posts/get-count-of-all-posts
```

```
7) search_recent_hashtag : Retrieves Posts from the last 7 days matching a search query.
GET /tweet-x/tweets/hashtag/recent/{tag}

https://docs.x.com/x-api/posts/search-recent-posts#search-recent-posts
```

``` 
8) search_all_hashtag : Retrieves Posts from the full archive matching a search query.
GET /tweet-x/tweets/hashtag/all/{tag}

https://docs.x.com/x-api/posts/search-all-posts
```

```
9) get_following : Retrieves a list of Users followed by a specific User by their ID.
GET /tweet-x/follow/{user_id}/following 

https://docs.x.com/x-api/users/get-following
```

```
10) get_followers : Retrieves a list of Users who follow a specific User by their ID.
GET /tweet-x/follow/{user_id}/followers

https://docs.x.com/enterprise-api/users/get-followers#get-followers
```

