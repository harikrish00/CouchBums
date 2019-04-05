# CouchBums

Build Status
CouchBums

### Summary:
Ways to share movies/tv shows with friends

### Resources
Users
Friends
Watch List
Shows Watched
Post
Star Rating
Movies
TV Shows
Functionality Breakdown By Resources

### Users
```
GET /users
GET /users/<user_id>
POST /users
DELTE /users/<user_id>
```

### Friends
```
GET /users/<user_id>/friends
GET /users/<user_id>/friends/<friend_id>
POST /users/<user_id>/friends/<friend_id>/users/<user_id>/friends/<friend_id>
DEL  /users/<user_id>/friends/<friend_id>/users/<user_id>/friends/<friend_id>
```

### Watch List
```
GET /users/<user_id>/watchlist
POST /users/<user_id>/watchlist
DEL /users/<user_id>/watchlist
GET /users/<user_id>/watchlist/items
POST /users/<user_id>/watchlist/items
GET /users/<user_id>/watchlist/items/<item_id>
DEL /users/<user_id>/watchlist/items/<item_id>
```

### Post
```
GET /users/<user_id>/posts
POST /users/<user_id>/posts
GET /users/<user_id>/posts/<post_id>
DEL /users/<user_id>/posts/<post_id>
```

### Movies
```
GET /movies
POST /movies
GET /movies/<movie_id>
DEL /movies/<movie_id>
```

### TV
```
GET /tv
POST /tv
GET /tv/<tv_id>
DEL /tv/<tv_id>
```
### Ratings

Movies
```
GET /movies/<movie_id>/ratings
POST /movies/<movie_id>/ratings
GET /movies/<movie_id>/ratings/<rating_id>
DEL /movies/<movie_id>/ratings/<rating_id>
```

TV
```
GET /tv/<tv_id>/ratings
POST /tv/<tv_id>/ratings
GET /tv/<tv_id>/ratings/<rating_id>
DEL /tv/<tv_id>/ratings/<rating_id>
```
