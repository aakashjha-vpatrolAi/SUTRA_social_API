# Facebook Data Extraction Code

## 📌 Overview
This project provides a structured integration with the **via RapidAPI and APIfy** to fetch publicly available Facebook data such as users, pages, and posts.

---

## ⚙️ Configuration

### Base URL
```
https://facebook-scraper3.p.rapidapi.com
```

### Headers
```
X-RapidAPI-Key: <YOUR_RAPIDAPI_KEY>
X-RapidAPI-Host: facebook-scraper3.p.rapidapi.com
```

---

## 📚 API Endpoints

### 1. 🔍 Search People
Search for Facebook user profiles.

**Endpoint**
```
GET /FB_rapid/users/search-people

https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_f7a472b6-2abf-4d48-99ba-7927def033a6
```

**Use Case**
- User discovery
- Identity resolution

---

### 2. 🌐 Global Search
Search across users, pages, and posts.

**Endpoint**
```
GET /FB_rapid/users/search-global

https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_1aa60f06-698a-4376-8674-91173700d761

```

**Use Case**
- Unified search for location, hashtag, keyword, etc

---

### 3. 📝 Search Posts
Search public posts by keyword.

**Endpoint**
```
GET /FB_rapid/users/search-posts

https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_c0fb83cf-8dae-4824-a0ee-a66b79b037fb
```

**Use Case**
- Content monitoring
- Check the posts related to a keyword

---

### 4. 📄 Search Pages
Search Facebook pages.

**Endpoint**
```
GET /FB_rapid/users/search-pages

https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_6fc14979-9524-4671-8742-0fc6e8824a2a
```

**Use Case**
- Brand discovery
- Organization tracking
- search any page by its FB-URL

---

### 5. 📑 User Posts
Fetch posts from a user profile.

**Endpoint**
```
GET /FB_rapid/users/user-posts

https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_7817d09c-d8c9-4e47-bcd1-fe48b3abd699
```

**Use Case**
- get the posts of a user by its profile_id
- Timeline analysis of user's post

---

### 6. 👤 Profile Details
Fetch user profile metadata.

**Endpoint**
```
GET /FB_rapid/users/profile/details

https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_cd7a94c1-5880-434f-8119-121c1589a464
```


**Use Case**
- get all profile page data 
- Metadata extraction

---

### 7. 🏢 Page Details
Fetch Facebook page metadata.

**Endpoint**
```
GET /FB_rapid/profile/page/details

https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_847dc586-dd05-4660-a838-128c872a1407
```

**Use Case**
- Page analytics (followers_count, following_count, post_count, categories, is_verified, etc)

---

### 8. 🆔 Get Profile ID
Resolve username or URL to profile ID.

**Endpoint**
```
GET /FB_rapid/profile/get-profile-id

https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_e8f05277-cc6d-4e96-bd1d-725c861eb9e4
```

**Use Case**
- get the profile_id(100044226919512) using the FB page URL(https://www.facebook.com/SachinTendulkar)
- profile_id will used by our other apis 
---

```
# APIfy

facebook Apify apis : 
visit https://console.apify.com/actors and search by using below actor-ids : 
1) fetch_facebook_profile : 4Hv5RhChiaDk6iwad
2) get_facebook_profile_id : 4Hv5RhChiaDk6iwad
3) get_all_facebook_posts : KoJrdxJCTtpon81KY
4) get_post_comments : us5srxAYnsrkgUv2v
5) get_followers_following : hhgonmMEMGmpbDDAN

* slow : avg. time(10 to 20 second)
* Heavy : resource-intensive (RAM, time, terminal)

```
---

## ⚠️ Limitations

- Only public data is accessible
- Followers list, large data, etc  is not fully available or diffcult to access.
---

