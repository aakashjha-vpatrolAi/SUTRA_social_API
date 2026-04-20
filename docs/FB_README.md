# Facebook API for SUTRA

## Overview
This module integrates with **RapidAPI** (and optionally **Apify**) to fetch publicly available Facebook data such as users, pages, and posts.

---

## Configuration

### Base URL (upstream)
```
https://facebook-scraper3.p.rapidapi.com
```

### Environment variables (SUTRA `.env`)
```
FB_BASE_URL=https://facebook-scraper3.p.rapidapi.com
FB_RAPIDAPI_HOST=facebook-scraper3.p.rapidapi.com
FB_RAPIDAPI_KEY=<YOUR_RAPIDAPI_KEY>
```

### Headers (upstream)
```
X-RapidAPI-Key: <YOUR_RAPIDAPI_KEY>
X-RapidAPI-Host: facebook-scraper3.p.rapidapi.com
```

---

## API Endpoints

Notes:
- All endpoints are **GET**.
- Inputs are passed as **query parameters**.
- Date inputs must be in `YYYY-MM-DD` (ISO) format.
- `cursor` is optional and is used for pagination when the upstream API returns it.

Server base "URL" (example):
```
http://localhost:8000
```

### 1. Search People
Search for Facebook user profiles.

**Endpoint**
```
GET {URL}/FB_rapid/users/search-people

https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_f7a472b6-2abf-4d48-99ba-7927def033a6
```

**Inputs**
- `query` (required): search keyword / name
- `cursor` (optional): pagination cursor

**Example response**
```
{
  "results": [
    {
      "type": "search_profile",
      "profile_id": "100044527235621",
      "url": "https://www.facebook.com/narendramodi",
      "name": "Narendra Modi",
      "is_verified": true,
      "profile_picture": {
        "uri": "https://scontent.fbah1-1.fna.fbcdn.net/v/t39.30808-1/459337720_1303104714517091_2841079786125894817_n.jpg?stp=dst-jpg_s120x120_tt6&_nc_cat=1&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=gpaAhpb1Q8cQ7kNvwF8Oeyc&_nc_oc=AdrzV9J6GPsNoHc6LMeq3qRJGQX__TfYlTK5K3-MOnhDDyZaS-vHUele4WkK9tY--3w&_nc_zt=24&_nc_ht=scontent.fbah1-1.fna&_nc_gid=eD-PmsviI7JG2BS3ZuXJdA&_nc_ss=7a389&oh=00_Af1vH7LZlBh9GPFavRVaJXiPZs4K7y_dr8Gp17YJ0cSfsw&oe=69E39E5E",
        "width": 120,
        "height": 120,
        "scale": 2
      }
    },

  ],
  "cursor": "{\"page_number\": 0, \"flow_cursors_serialized\": {\"INTERNAL_DEBUG_MODULE\": \"{}\", \"SEARCH_CONTROLS_INTERCEPT\": \"{}\", \"INTEGRITY\": \"{\\\"has_more_results\\\":false,\\\"processed_unicorn_ids\\\":[],\\\"is_end_of_serp\\\":false}\", \"SPELLER\": \"{}\", \"SOCIAL_RAG\": \"{}\", \"PEOPLE_TAB\": \"{\\\"has_more_results\\\": true, \\\"browse_cursor_serialized\\\": \\\"AbqCICsXHcCkqk4tP40nS4M0RwNMbGap_jIHj-KakGnGZm1w76adNORe0Bhdu1wI26vX8g41M8GxLzl1ISnHY_T3ffjCt9xy-68MF0_euQ--xc5-2dv1_8jv4e6S9inj2SRzI5bkSvUldw_irTn6ydCoaO5H4k51r0CeLTy4HhKyWizkYzgcwjJrkuVYb1hdEfrKrePvhc1ZydkbsmeU8wiXAps2ksMohPEulSZ8G9IgZCpKzfP9pADlVSGnrQMkaJK9pbopuSw6tJL7XtO-S6LyIRok0jaAKJRSI4BJ-PSBD3XWlSbm5iH2ZodQuJvbzwoMtHAC0xmRhkC5ZZtwdODtDOKkWyC4rKGEj78DEjEA3KH6sjN84uca0SLH8cA9sSddWcvp9PRKdWcs1T_KchQc0-xwaOqEPoGDAHIb9dY4_JlyQxhbxXOqMmB8DVYtOBzBjNJZtGceNoArUhnPNPMqYm2Qd4AkIYzDNVcnbp_vG1dnZ6q4Q1mJlszr22z2bRdtebFyK42PucHjNeRPPvIVzYIE1XkSNbCIyUDRwoTJAw\\\", \\\"processed_unicorn_ids\\\": [], \\\"is_end_of_serp\\\": false}\"}, \"result_ids_shown\": [], \"unit_id_logging_fields\": {\"num_total_modules\": 1, \"num_total_results\": 7, \"num_total_vertical_results\": 7}, \"entity_ids_shown_by_type\": {}, \"processed_unicorn_ids\": [], \"completed_flows\": [\"INTERNAL_DEBUG_MODULE\", \"SEARCH_CONTROLS_INTERCEPT\", \"INTEGRITY\", \"SPELLER\", \"SOCIAL_RAG\"]}"
}
```


**Use Case**
- User discovery
- Identity resolution

---

### 2. Global Search
Search across users, pages, and posts.

**Endpoint**
```
GET  {URL}/FB_rapid/users/search-global

https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_1aa60f06-698a-4376-8674-91173700d761
```

**Inputs**
- `query` (required): keyword to search
- `recent_posts` (optional, bool): when true, prioritize recent posts
- `location_uid` (optional): location filter id
- `start_date` (optional, `YYYY-MM-DD`): defaults to last 30 days if omitted
- `end_date` (optional, `YYYY-MM-DD`): defaults to today if omitted
- `cursor` (optional): pagination cursor

**Example response**
```
{
  "results": [
    {
      "post_id": "1524364989248373",
      "type": "post",
      "url": "https://www.facebook.com/AjiHaanLive/posts/pfbid02iepcuuN9sXT3QgwoaZ2RzyLvVodfFSNWRpsGbH4JAd9LM4vBfF5hvm6BVgGKjXeil",
      "message": "रीसेंट नोएडा प्रोटेस्ट मैंने देखा है। मजदूरों की मांगें जायज हैं ...महंगाई, कम सैलरी, बढ़ता किराया, बच्चों की फीस और लंबे वर्किंग ऑवर्स के चलते उनका गुस्सा समझ में आता है...UP सरकार ने भी तेजी से रिएक्ट करते हुए न्यूनतम वेतन में करीब 21% की इंटरिम बढ़ोतरी कर दी, जो स्वागत योग्य कदम है..\n\nलेकिन साथ ही हमें बड़े ग्लोबल संदर्भ को भी समझना चाहिए। ईरान-अमेरिका-इजराइल तनाव के कारण स्ट्रेट ऑफ होर्मुज प्रभावित हुआ है...दुनिया China+1 फॉर्मूले के तहत प्रोडक्शन को चीन से हटाकर भारत, वियतनाम और अन्य जगहों पर शिफ्ट कर रही है। \n\nनोएडा-ग्रेटर नोएडा इलेक्ट्रॉनिक्स, ऑटो और टेक्सटाइल का बड़ा हब है, जहां FDI और नए जॉब्स आ रहे हैं..अगर यहां का माहौल अस्थिर दिखा तो इनवेस्टर्स तुरंत दूसरी जगह देख लेंगे..\n\nऐसे में कुछ वेस्टेड इंटरेस्ट्स और बाहरी तत्व पूरे जोर से कोशिश करेंगे कि दुनिया का प्लान B यानि भारत भी खराब नजर आए...वे नोएडा जैसे स्थानीय मुद्दे को बड़े स्तर पर भड़काकर पूरे माहौल को खराब कर सकते हैं। कुछ रिपोर्ट्स में आउटसाइडर्स, व्हाट्सएप बॉट नेटवर्क और विदेशी लिंकेज की बात भी सामने आ रही है।\n\nइसलिए सरकार, एजेंसियों और मजदूर संगठनों तीनों को सतर्क रहना होगा। \n\nसरकार को शांतिपूर्ण प्रदर्शन का अधिकार मानते हुए हिंसा को बिल्कुल बर्दाश्त नहीं करना चाहिए और असली मांगों को जल्द से जल्द निपटाना चाहिए। \n\nमजदूर संगठनों की भी जिम्मेदारी है कि कोई कंप्रोमाइज्ड तत्व उनके आंदोलन को देश-विरोधी एजेंडे में न बदल दे। लेबर यूनियनों का काम मजदूरों की सच्ची आवाज उठाना है, न कि किसी बड़े गेम का टूल बनना।\n\nआखिरकार, भारत को इस मौके का पूरा फायदा उठाना है। China+1 में हमारी युवा वर्कफोर्स, इंफ्रास्ट्रक्चर और PLI स्कीम बड़ी ताकत हैं। लेकिन स्थिरता और विश्वास के बिना यह मौका हमारे हाथ से निकल सकता है..\n\nमजदूरों के हक का समर्थन और राष्ट्रहित की सुरक्षा दोनों साथ साथ चल सकते हैं..बस हमें वॉचफुल और बैलेंस्ड रहना होगा.. 🙏🏻\n\n#noida  #noidanews",
      "message_rich": "रीसेंट नोएडा प्रोटेस्ट मैंने देखा है। मजदूरों की मांगें जायज हैं ...महंगाई, कम सैलरी, बढ़ता किराया, बच्चों की फीस और लंबे वर्किंग ऑवर्स के चलते उनका गुस्सा समझ में आता है...UP सरकार ने भी तेजी से रिएक्ट करते हुए न्यूनतम वेतन में करीब 21% की इंटरिम बढ़ोतरी कर दी, जो स्वागत योग्य कदम है..\n\nलेकिन साथ ही हमें बड़े ग्लोबल संदर्भ को भी समझना चाहिए। ईरान-अमेरिका-इजराइल तनाव के कारण स्ट्रेट ऑफ होर्मुज प्रभावित हुआ है...दुनिया China+1 फॉर्मूले के तहत प्रोडक्शन को चीन से हटाकर भारत, वियतनाम और अन्य जगहों पर शिफ्ट कर रही है। \n\nनोएडा-ग्रेटर नोएडा इलेक्ट्रॉनिक्स, ऑटो और टेक्सटाइल का बड़ा हब है, जहां FDI और नए जॉब्स आ रहे हैं..अगर यहां का माहौल अस्थिर दिखा तो इनवेस्टर्स तुरंत दूसरी जगह देख लेंगे..\n\nऐसे में कुछ वेस्टेड इंटरेस्ट्स और बाहरी तत्व पूरे जोर से कोशिश करेंगे कि दुनिया का प्लान B यानि भारत भी खराब नजर आए...वे नोएडा जैसे स्थानीय मुद्दे को बड़े स्तर पर भड़काकर पूरे माहौल को खराब कर सकते हैं। कुछ रिपोर्ट्स में आउटसाइडर्स, व्हाट्सएप बॉट नेटवर्क और विदेशी लिंकेज की बात भी सामने आ रही है।\n\nइसलिए सरकार, एजेंसियों और मजदूर संगठनों तीनों को सतर्क रहना होगा। \n\nसरकार को शांतिपूर्ण प्रदर्शन का अधिकार मानते हुए हिंसा को बिल्कुल बर्दाश्त नहीं करना चाहिए और असली मांगों को जल्द से जल्द निपटाना चाहिए। \n\nमजदूर संगठनों की भी जिम्मेदारी है कि कोई कंप्रोमाइज्ड तत्व उनके आंदोलन को देश-विरोधी एजेंडे में न बदल दे। लेबर यूनियनों का काम मजदूरों की सच्ची आवाज उठाना है, न कि किसी बड़े गेम का टूल बनना।\n\nआखिरकार, भारत को इस मौके का पूरा फायदा उठाना है। China+1 में हमारी युवा वर्कफोर्स, इंफ्रास्ट्रक्चर और PLI स्कीम बड़ी ताकत हैं। लेकिन स्थिरता और विश्वास के बिना यह मौका हमारे हाथ से निकल सकता है..\n\nमजदूरों के हक का समर्थन और राष्ट्रहित की सुरक्षा दोनों साथ साथ चल सकते हैं..बस हमें वॉचफुल और बैलेंस्ड रहना होगा.. 🙏🏻\n\n#noida  #noidanews",
      "timestamp": 1776151837,
      "comments_count": 3,
      "reactions_count": 93,
      "reshare_count": 4,
      "reactions": {
        "angry": 0,
        "care": 0,
        "haha": 0,
        "like": 93,
        "love": 0,
        "sad": 0,
        "wow": 0
      },
      
    }
  ],
  "cursor": "{\"page_number\": 0, \"flow_cursors_serialized\": {\"INTERNAL_DEBUG_MODULE\": \"{}\", \"SEARCH_CONTROLS_INTERCEPT\": \"{}\", \"INTEGRITY\": \"{}\", \"SHORTCUT_DEEP_DIVE\": \"{}\", \"SPELLER\": \"{}\", \"HASHTAG_CHALLENGE_HEADER\": \"{}\", \"POSTS_TAB_UNICORN_CACHE\": \"{}\", \"POSTS_TAB\": \"{\\\"has_more_results\\\":true,\\\"browse_cursor_serialized\\\":\\\"AbqpL9kw6nqOTt7HDSc9oPUNT15vv7lGYQSZlgsNlwMaH-s30EKbb69aktELcsF1CpRLVLahIu3FKVzCGto7rojMfYzhZHxLrjQ_dydijAL0YapJ6VzByUNDtliX3Jm1JGfAPkiFfaAaJBsCfW6De8YF3NP9fsJaRYAofS-tBjOxULOfjwlTrDo0-uS7Qi6fBvRtTAi3o73d8yfnDk4PArwNfQ9Ya4oAQYhRymtSBVTrZir2x_RkNJTkDw7Een9QGbsXuINF0cDNwD5h-9Zgr4DJ_OKsww0Bvx6JHPCiUJCVTq0KLVW8ql9G2Iq44cU2PveKaO9G3KsECu9bW3GFj0pvU68ig9zO5S75wkVK9H8oHU_pMNLoQdmKha79SYP3PUYgTgyu2Pc25P4HhbRn_ajU5gu2ewZx9RbhjjmeASkuyZSP5gHZRoFafJBpeT-EQnAPWHMkwCLKaAcg6D5jS3GuAlFCLsCGlZVI7al4x_sOiXIk6EVlkEiX0HhfVL_twsUHKwKD2jlH0Hj3bBnjxVGjT9TIEULTRezPCgi3nSJYia3UCOZSM9pp9Hh0zrypnk4wcT-J2o63k_J9OhZxnET2A3dYBtdX9S1NC_URQfouWuIfyEYd2hUvkoddYUOhLPE\\\",\\\"processed_unicorn_ids\\\":[1524364989248373,2165889760844215,1655191766178384,1511386444357812,1655187926178768,1655180802846147,1384560860384764,1655126712851556,1655188456178715,1655180079512886,1436516371834608,1655167322847495,1655031782861049,1443594264470220,2460769757716621,1436512088501703,1384707810370069,1469739517986250,1608597927086936,934361859564228,4237137716545205,899463536428076,1548227267311151,996506056659558,1680507787412957,3256975497934250,1608606967086032,26803893229222944,1604060307486049,1527415868996897,1730522754792185,1655189359511958,945347211577221,1517194866589579,1488799056619169,939213528975484,1451766693413773,1552099183620291,1571818284980014,1403429805165937,1403427505166167,1397800295718044,928833770142614,1288686250436629,5249929355232630,1295910295801920,1391435832999973,1511940773971503,1528710488627019,1416692166880473,1485817023340045,122220909026305644,1669227407563777,1252576707066057,122256229538173751,1484896186351820,907147685635004,4349912621918953,1729955831763304,880468725074589,1128480382865549,1578966973177066,3370144566486177,1440712858084992,1383888827118634,122122282695171421,1496412735538719,1517198773255855,2031037871096847,1528724971958904,1374547111368694,1283412330561500,1551249597038583,1623481335549640,2291459468049920,1510681184428338,948793814539601,10162219178316809,122261075366247664,1654295109601383,1382396340580572,977251234835247,1510622661100857,1715460506492315,1510698461093277],\\\"is_end_of_serp\\\":false}\", \"CONTENT\": \"{\\\"processed_unicorn_ids\\\": []}\"}, \"result_ids_shown\": [], \"unit_id_logging_fields\": {\"num_total_modules\": 2, \"num_total_results\": 5, \"num_total_vertical_results\": 5}, \"entity_ids_shown_by_type\": {}, \"processed_unicorn_ids\": [], \"completed_flows\": [\"INTERNAL_DEBUG_MODULE\", \"SEARCH_CONTROLS_INTERCEPT\", \"INTEGRITY\", \"SHORTCUT_DEEP_DIVE\", \"SPELLER\", \"HASHTAG_CHALLENGE_HEADER\", \"POSTS_TAB_UNICORN_CACHE\"]}"
}
```

**Use Case**
- Unified search for location, hashtag, keyword, etc

---

### 3. Search Posts
Search public posts by keyword.

**Endpoint**
```
GET {URL}/FB_rapid/users/search-posts

https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_c0fb83cf-8dae-4824-a0ee-a66b79b037fb
```

**Inputs**
- `query` (required): keyword to search
- `recent_posts` (optional, bool): when true, prioritize recent posts
- `location_uid` (optional): location filter id
- `start_date` (optional, `YYYY-MM-DD`)
- `end_date` (optional, `YYYY-MM-DD`)
- `cursor` (optional): pagination cursor

**Example Response**
```
{
  "results": [
    {
      "post_id": "1528710488627019",
      "type": "post",
      "url": "https://www.facebook.com/reel/1658559118513497/",
      "message": "नोएडा में हिंसक प्रदर्शन, कवरेज के दौरान भास्कर रिपोर्टर को पुलिस ने डंडा मारा, वर्कर्स को जबरन हिरासत में लिया।  \nhttps://dainik.bhaskar.com/kdbeJQHsi2b   \n\n#NoidaProtest #BhaskarReporter #DainikBhaskar #FactoryWorkers #Protest #Violence #Noida #UttarPradesh",
      "message_rich": "नोएडा में हिंसक प्रदर्शन, कवरेज के दौरान भास्कर रिपोर्टर को पुलिस ने डंडा मारा, वर्कर्स को जबरन हिरासत में लिया।  \nhttps://dainik.bhaskar.com/kdbeJQHsi2b   \n\n#NoidaProtest #BhaskarReporter #DainikBhaskar #FactoryWorkers #Protest #Violence #Noida #UttarPradesh",
      "timestamp": 1776076391,
      "comments_count": 6369,
      "reactions_count": 87044,
      "reshare_count": 11521,
      "reactions": {
        "angry": 783,
        "care": 66,
        "haha": 5627,
        "like": 79604,
        "love": 256,
        "sad": 453,
        "wow": 255
      },
      "author": {
        "id": "100044642460098",
        "name": "Dainik Bhaskar",
        "url": "https://www.facebook.com/dainikbhaskar",
        "profile_picture_url": "https://scontent.fkul16-2.fna.fbcdn.net/v/t39.30808-1/549891562_1354989365999133_8202468245563985639_n.jpg?stp=cp0_dst-jpg_s80x80_tt6&_nc_cat=1&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=qxLsZ9NnRV4Q7kNvwHyN7c6&_nc_oc=Ado0Jz2LLoOk7TGJ4dBgbis3o-GcrqxdFN02ZBMST766fU_ARXRkSJcV877jZjPVx8U&_nc_zt=24&_nc_ht=scontent.fkul16-2.fna&_nc_gid=6xpyiW12pztbIlr-kqVprg&_nc_ss=7a389&oh=00_Af28Np47XfwW4451f1AVhSMcdG4Rptmy69U27eMQMBbq3Q&oe=69E3F034"
      },
      "author_title": null,
      "image": null,
      "video": "https://www.facebook.com/reel/1658559118513497/",
      "album_preview": null,
      "video_files": {
        "video_sd_file": "https://video.fkul16-4.fna.fbcdn.net/o1/v/t2/f2/m412/AQPUok1k_OeyUfXZ-NmMvH6XtFs_8T_YHOZLfzQBEV6HaWVbAGdDcPBV0jk46QT4C_DFx4dw207FgSr6L3kFJQtzxJILVSZItKw9V6VSeQ.mp4?_nc_cat=107&_nc_oc=AdrZNAJfJFlKbBvINfg8o0N7GEzrLW_IYQbHlCBkw0qmxcQQ5ITRC4lgE7EnNOlUNJQ&_nc_sid=8bf8fe&_nc_ht=video.fkul16-4.fna.fbcdn.net&_nc_ohc=xAiD5YRpn-QQ7kNvwHz5M6V&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5GQUNFQk9PSy4uQzMuMzYwLnN2ZV9zZCIsInhwdl9hc3NldF9pZCI6MjA0ODE5NTI3NTczNTU3MCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTIyLCJkdXJhdGlvbl9zIjoyMTEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=6xpyiW12pztbIlr-kqVprg&_nc_ss=7a389&_nc_zt=28&oh=00_Af1FkCfe_tWuHv4v4PZWwuNSKbTCaKMzMRZlLq8JfbbE_A&oe=69E3D19F&bitrate=616067&tag=sve_sd",
        "video_hd_file": "https://video.fkul16-2.fna.fbcdn.net/o1/v/t2/f2/m366/AQP86leFwQI5hl6hQUxNpzcVr2wOgyLVOdSawqHdbnnRMJrqpI0EMrJ0jaXt5Eh316tXAQeGN63xhlGfv4LNZZi2AVpR9eojQVufBqTckdsWWg.mp4?_nc_cat=110&_nc_oc=AdpFmn8qIjDD2okhag3qiLz8OTk3zgdGl7flJVhVuIDR53kkE9dMWfi6_9fhf3vyFJI&_nc_sid=5e9851&_nc_ht=video.fkul16-2.fna.fbcdn.net&_nc_ohc=gygU_7J7o-0Q7kNvwELOVb6&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5GQUNFQk9PSy4uQzMuNzIwLmRhc2hfaDI2NC1iYXNpYy1nZW4yXzcyMHAiLCJ4cHZfYXNzZXRfaWQiOjIwNDgxOTUyNzU3MzU1NzAsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEyMiwiZHVyYXRpb25fcyI6MjExLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=89dfbd4f1df87bca&_nc_vs=HBksFQIYRWZiX2VwaGVtZXJhbC9GMzQ0NTc3MTY5RUQ1OTlDRUVDMTgxRjdBOTk3NzU5Rl9tdF8xX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhAZmJfcGVybWFuZW50LzMyNEFGNENGMzFFM0FGOTI2N0U2MEJBNTM4QjUxODk5X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACakiLr907SjBxUCKAJDMywXQGpwAAAAAAAYGWRhc2hfaDI2NC1iYXNpYy1nZW4yXzcyMHARAHUCZZSeAQA&_nc_gid=6xpyiW12pztbIlr-kqVprg&_nc_ss=7a389&_nc_zt=28&oh=00_Af35CULe2vYvr9g4IadBrobiPVXCQs8TVjtLhMDbJCQqXw&oe=69E3CE8A&bitrate=2246233&tag=dash_h264-basic-gen2_720p"
      },
      "video_thumbnail": "https://scontent.fkul16-2.fna.fbcdn.net/v/t15.5256-10/670952126_4524403947788244_5889705476534083072_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=1&ccb=1-7&_nc_sid=5fad0e&_nc_ohc=ox7o0jLyzq8Q7kNvwG5AZ6y&_nc_oc=Adrbmsla22l_GXVt8H69fm_gVJGWyUrIJy-ef-nBih1gO4CVYP2fXnycIURhYqjbd24&_nc_zt=23&_nc_ht=scontent.fkul16-2.fna&_nc_gid=6xpyiW12pztbIlr-kqVprg&_nc_ss=7a389&oh=00_Af24nLGMEPIwLnhHYevYKVU_6IdjR-ZC9x9b5TMmAV1_VA&oe=69E3E609",
      "external_url": null,
      "attached_event": null,
      "attached_post": null,
      "attached_post_url": null,
      "text_format_metadata": null,
      "comments_id": "1528710488627019",
      "shares_id": "1528710488627019"
    },
    

  ],
  "cursor": "{\"page_number\": 0, \"flow_cursors_serialized\": {\"INTERNAL_DEBUG_MODULE\": \"{}\", \"SEARCH_CONTROLS_INTERCEPT\": \"{}\", \"INTEGRITY\": \"{}\", \"SHORTCUT_DEEP_DIVE\": \"{}\", \"SPELLER\": \"{}\", \"HASHTAG_CHALLENGE_HEADER\": \"{}\", \"POSTS_TAB_UNICORN_CACHE\": \"{}\", \"POSTS_TAB\": \"{\\\"has_more_results\\\": true, \\\"browse_cursor_serialized\\\": \\\"Abr5rfR9tTJvt1KA82uZ6ob1TRSUA0DCe0uin6oEcJ5rL2atW2Hdy1tCqidN6_qso8TofudNGfBPugVMNnK9DVuJW9V4mf5NSCnVZiMIcUB7XqIKHQ0Yg62mmL4QZ04wAgTBmeve3VTnaUrhN9Clwqt-kffEQsSyM4F3K1vR1Pt58PfVH-VEVDJgXzmnVnPDsIYklaFmRkLkqmPPcV94mCNn3F8LO0wt97Lh_-uotKuOJMn9wlfNf6TDBUSGL4oPB61L3F-ErTF2FExUBXQpVARmd5gzQrswQDLZzBXo0QcdSw3YM85P0edMHgiI4s6XvPlv1BiVMTqsoO3VuTVaYeSc6RzgRr2dxr6FcUFpJZMYB5KG9DidapmO880whnZi5EdbB0HTn1Tcp-UFa9CTY0ekHADcMv7z3UIbLZAL4_dywdw-DONeMlmjmzb1ooh-s9S8wPxheJ3bZdhJV5nWBxA833wgzBdQJz6qum6bW29HpR1xt9Wfr-N2cw0wvxxGtk7sBwT6_hpu62Cq_E9UyCIjc6MbAGM1d949xkDOyzGLBXuIAUf77Qs7wkpm7GhXclAOlJ3Kg_Moe5BVb2nHNaNik-tG5O6CXSzG0wYSG9baZFWMlUkGBOuHXVjyrNpPdgo\\\", \\\"processed_unicorn_ids\\\": [], \\\"is_end_of_serp\\\": false}\"}, \"result_ids_shown\": [], \"unit_id_logging_fields\": {\"num_total_modules\": 2, \"num_total_results\": 5, \"num_total_vertical_results\": 5}, \"entity_ids_shown_by_type\": {}, \"processed_unicorn_ids\": [], \"completed_flows\": [\"INTERNAL_DEBUG_MODULE\", \"SEARCH_CONTROLS_INTERCEPT\", \"INTEGRITY\", \"SHORTCUT_DEEP_DIVE\", \"SPELLER\", \"HASHTAG_CHALLENGE_HEADER\", \"POSTS_TAB_UNICORN_CACHE\"]}"
}
```

**Use Case**
- Content monitoring
- Check the posts related to a keyword

---

### 4. Search Pages
Search Facebook pages.

**Endpoint**
```
GET  {URL}/FB_rapid/users/search-pages

https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_6fc14979-9524-4671-8742-0fc6e8824a2a
```

**Inputs**
- `query` (required): page name / keyword
- `location_uid` (optional): location filter id
- `cursor` (optional): pagination cursor

**Example response**
```
{
  "results": [
    {
      "type": "page",
      "profile_url": "https://www.facebook.com/people/The-Label-Jenn/100084236786813/",
      "url": "https://www.facebook.com/people/The-Label-Jenn/100084236786813/",
      "image": {
        "uri": "https://scontent.fbah1-1.fna.fbcdn.net/v/t39.30808-1/298514810_107577528727687_2550087521856375265_n.jpg?stp=dst-jpg_s120x120_tt6&_nc_cat=106&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=raoKRzVboDUQ7kNvwFLRIV2&_nc_oc=AdpAhPtWGehxImomxSzSgr-WSpxNSCdL4ltx0AKx88LZZF_OGceFBpHi4OuxjoC9P2Y&_nc_zt=24&_nc_ht=scontent.fbah1-1.fna&_nc_gid=8H61xvZy5xf95qvtLfyZDQ&_nc_ss=7a389&oh=00_Af3_R3Ge7Amnq10WPwXrkMwEzL6wmmX2o1z-zYwHmTHeFg&oe=69E3CF03",
        "width": 120,
        "height": 120,
        "scale": 2
      },
      "name": "The Label Jenn",
      "facebook_id": "100084236786813",
      "is_verified": false
    },
    
    ],
  "cursor": "{\"page_number\": 0, \"flow_cursors_serialized\": {\"INTERNAL_DEBUG_MODULE\": \"{}\", \"SEARCH_CONTROLS_INTERCEPT\": \"{}\", \"INTEGRITY\": \"{\\\"has_more_results\\\":false,\\\"processed_unicorn_ids\\\":[],\\\"is_end_of_serp\\\":false}\", \"SPELLER\": \"{}\", \"PAGES_TAB\": \"{\\\"has_more_results\\\": true, \\\"browse_cursor_serialized\\\": \\\"AbpL5okk1CkujuYONct2FjBqB9lTGvQqaq74-wxGrAIGD1HxPW7ldOvtGrpFL_G2GE5SwOsbG3SN6KikS3zXcqwkGgCdaPSRBrzduhFuSGJgEfw-0dmkrqLPIIH_6q9Km-8-m5BKEE8LBuQGer8U6J-b-Utcdj30Ec2a22ePsUrpvyAGG6PrS3_6cn6aIjmJneQMJmksROe23jD-hV_idQmNsRBb9XfIvIBTZTOViohqQrl60StmrydJVM9x8hBleV9RYKEn4oF6XANtD45RXnK6fwzAlOr9zo5VaqhK1cFc2oQoMnKG3hJkyAYyk2PCJFSvAY2duOyBHta05LRjYLs9m3Mp1_zSLhI0Tta9fHd9A8ne7aI8uFBA2SYHG0w8yOatVOg5UU9XT6srySDBD3pWS08swPG__X-Kqc0GO2dUppPKmA7oyz7WjlUDLUhb5kKaZmn2rSIIIBUS6FLS3qqJuxPehGT6G8Uae9qUYYuTRk7DqacHc6ubHfzyYFSjEtbz2B4HASRbWDoVzYdEEti8skDxcrFhij6UDcZwbOLaQQ\\\", \\\"processed_unicorn_ids\\\": [], \\\"is_end_of_serp\\\": false}\"}, \"result_ids_shown\": [], \"unit_id_logging_fields\": {\"num_total_modules\": 1, \"num_total_results\": 7, \"num_total_vertical_results\": 7}, \"entity_ids_shown_by_type\": {}, \"processed_unicorn_ids\": [], \"completed_flows\": [\"INTERNAL_DEBUG_MODULE\", \"SEARCH_CONTROLS_INTERCEPT\", \"INTEGRITY\", \"SPELLER\"]}"
}

```

**Use Case**
- Brand discovery
- Organization tracking
- Search any page by name/keyword (not by URL)

---

### 5. User Posts
Fetch posts from a user profile.

**Endpoint**
```
GET  {URL}/FB_rapid/posts/user-posts

https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_7817d09c-d8c9-4e47-bcd1-fe48b3abd699
```

**Inputs**
- `profile_id` (required): numeric profile id (example: `100044226919512`)
- `start_date` (optional, `YYYY-MM-DD`): defaults to last 30 days if omitted
- `end_date` (optional, `YYYY-MM-DD`): defaults to today if omitted
- `cursor` (optional): pagination cursor

**Example response**
```
{
  "results": [
    {
      "post_id": "2023362625056154",
      "type": "post",
      "url": "https://www.facebook.com/narendramodi/videos/2023362625056154/",
      "message": "LIVE. ‘Mera Booth, Sabse Mazboot Samvaad - Tamil Nadu.’",
      "message_rich": "LIVE. ‘Mera Booth, Sabse Mazboot Samvaad - Tamil Nadu.’",
      "timestamp": 1776076834,
      "comments_count": 3121,
      "reactions_count": 9633,
      "reshare_count": 1349,
      "reactions": {
        "angry": 9,
        "care": 75,
        "haha": 39,
        "like": 7785,
        "love": 1713,
        "sad": 2,
        "wow": 10
      },
      "author": {
        "id": "100044527235621",
        "name": "Narendra Modi",
        "url": "https://www.facebook.com/narendramodi",
        "profile_picture_url": "https://scontent.fush1-1.fna.fbcdn.net/v/t39.30808-1/459337720_1303104714517091_2841079786125894817_n.jpg?stp=cp0_dst-jpg_s40x40_tt6&_nc_cat=1&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=gpaAhpb1Q8cQ7kNvwFP5Vb-&_nc_oc=AdpU6Qoy1eSxY3ett2N8frvbccCB1EiMv8PwhkWogn4IXykuxL7PEhHmJ1mj1nqSCf0&_nc_zt=24&_nc_ht=scontent.fush1-1.fna&_nc_gid=QBe4TFJ8a9Pb72GrRZqovA&_nc_ss=7a389&oh=00_Af2cRs-J2S4DlvLRIk6f_FkPYqC-9H5lVwzqtrla_K0uew&oe=69E3D69E"
      },
      "author_title": null,
      "image": null,
      "video": "https://www.facebook.com/narendramodi/videos/2023362625056154/",
      "album_preview": null,
      "video_files": {
        "video_sd_file": "https://video.fush1-1.fna.fbcdn.net/o1/v/t2/f2/m366/AQO_g2jsZGdyjlVud92E5Dqdm3HPfECgQYQZhcRhlsGoa_Y1BNCzTP5TNAaJn-FyR5RT1-yDUjTN0Be782Bf7zufn5a_pHlOsnaZXH3CBpEO3q3IE7k1h8sJ58qUEUd6Jp0HsUbAuWPjuQJWRDp_OdBSrSUu.mp4?_nc_cat=104&_nc_oc=AdrGjQWQ2T6_UI0tHSpPatuVLZ9Hml2TKqV_dFJiBioIur6570rZcyBCd97pbOLrpRs&_nc_sid=8bf8fe&_nc_ht=video.fush1-1.fna.fbcdn.net&_nc_ohc=JxlbSuELujcQ7kNvwET9Sml&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5GQUNFQk9PSy4uQzMuNjQwLnNkIiwieHB2X2Fzc2V0X2lkIjozOTU5OTk3OTcwODAzNjc0LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAxMjUsImR1cmF0aW9uX3MiOjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=QBe4TFJ8a9Pb72GrRZqovA&_nc_ss=7a389&_nc_zt=28&oh=00_Af3g1Lp_k-ft-q7ofcDt14rLolMt_43tGDQ50DTkaLjJ9A&oe=69E3D4D5&bitrate=293747&tag=sd",
        "video_hd_file": "https://video.fush1-1.fna.fbcdn.net/o1/v/t2/f2/m311/AQPiwQ6WXW__EUTM_Cj0faJXQjQrm-AlofY3IDm1AgmAmTkv3_OufgIL4rgpcb4DwOfB17HOfkM_MJEyO2RWV2t4h8G4ePAEe3N3w85XDyWkCkka8B1NTN9Q_oXywBXJ381RbFOlS0FBiTNb35Getj2swvEi_GIIWO67-PU.mp4?_nc_cat=1&_nc_oc=AdqqPgyTv5J6fWPaomcDQkmaQw3csIY0Lo3dOnGldKDiBSpWocb_c_dRGBM--qUsNPg&_nc_sid=5e9851&_nc_ht=video.fush1-1.fna.fbcdn.net&_nc_ohc=qMgDbdzVg7cQ7kNvwFrd0Z0&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5GQUNFQk9PSy4uQzMuNjQwLmRhc2hfbGl2ZV9tZF9mcmFnXzJfdmlkZW8iLCJ4cHZfYXNzZXRfaWQiOjM5NTk5OTc5NzA4MDM2NzQsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDEyNSwiZHVyYXRpb25fcyI6MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=5f95cb344ea5b202&_nc_vs=HBksFQIYeHdhc2xpdmVfZmJfcGVybWFuZW50L0UxNEE1Nzc1MkU1OUZDNTNENDBGM0NBNkI4OEY5Q0I0X3dhc19saXZlX3JlbXV4X2Rhc2hfb2lsX3dpdGhfbGl2ZV90b192b2RfbWFwLXZpZGVvX291dHB1dF9kYXNoLm1wNBUAAsgBEgAVAhh4d2FzbGl2ZV9mYl9wZXJtYW5lbnQvQjM0N0I2MjFGQjJEMEEwMTI0RUE3MjREQThCOUU3ODNfd2FzX2xpdmVfcmVtdXhfZGFzaF9vaWxfd2l0aF9saXZlX3RvX3ZvZF9tYXAtYXVkaW9fb3V0cHV0X2Rhc2gubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJrSv44Wc5ogOFQIoAkMzLBdAriSZFocrAhgZZGFzaF9saXZlX21kX2ZyYWdfMl92aWRlbxEAdQJlmp4BAA&_nc_gid=QBe4TFJ8a9Pb72GrRZqovA&_nc_ss=7a389&_nc_zt=28&oh=00_Af3qZ1IGAG8ipR9FlAxkei8Z5yix95NcnILHheP1Kn9eFw&oe=69E00780&bitrate=290630&tag=dash_live_md_frag_2_video"
      },
      "video_thumbnail": "https://scontent.fush1-1.fna.fbcdn.net/v/t15.5256-10/669125701_2023419965050420_2546001167811261904_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=1&ccb=1-7&_nc_sid=df2c94&_nc_ohc=fOQVQoWi45QQ7kNvwHvvJqA&_nc_oc=Adp8Isd6E1ACkEOWgAZRdmIbIRGlx23iwAYBtRaHYha2wCiBYGBoJOO_lYWda0LMPYU&_nc_zt=23&_nc_ht=scontent.fush1-1.fna&_nc_gid=QBe4TFJ8a9Pb72GrRZqovA&_nc_ss=7a389&oh=00_Af2FpBFfTnw0G8v9nwXE1z2nISFIwUewCfCD8B95DgSwuA&oe=69E3E827",
      "external_url": null,
      "attached_event": null,
      "attached_post": null,
      "attached_post_url": null,
      "text_format_metadata": null,
      "comments_id": "2023362625056154",
      "shares_id": "2023362625056154"
    },
    
  ],
  "cursor": "Cg8Ob3JnYW5pY19jdXJzb3IJAAACGkFRSFNuVEtLN1lTdGtfczdzMFJ5dWZ4ckFMaWdDTWpVR012TzdXVU9DdkFRanA4U044RGJyNnYzTXh1R195YnV6UmdENVZyZ0ZrWFdfQ2kzTFpDYkpSVzdBdWo3OVI0U2xwREJDdlY2MEV3a1RkTENQa01uSVNTbmNTeHhZTzloQjAwd2lPZ2kzNXA1Q0RVcGlRMERwWno1VnE3aVhhdk8wdU1vUmdZblRRZTYzQ1FxOGwyMWNPUVVEREpVektpSzg5S2ltREoyZjBWY1E2cTg3WFZqb2NBV05SWS1BMEdrVE1Dd0Z4UERoRkJVV09ZVnRocDJTMTZ6ZUFzRGxqazNoR09rNEpvcklxVzhyMjFiSEhMSW9JeFZSXzgyQ3ExUTZnME9qR0dndV9CTFQwcGhqaUdSb3R3ZE5XQ3BrQnFwUUdzZmM2cmtkd1o2ZlhsbmNYVEZYcjJlcXJ5bWJUakxsQTNrazNtV05HMkhaYTUyeDhEVFRCcl9pVmJuUnplME0wa1lsODJoSi16WEVDb3RKS1FNUzlzc29OdDllY2JUampMOVNvdEtHU1ljTjNGejc1UlAzaFRiX0k3cnJoa29Sd1dzRWw0NzRxNHBkYlZValYtZGZMTmdHWkZHVmlmb2U0bXF4enVFTjl6NlBfWGlya3drTVNhc0VYMkIzdWt2b0RqVnFnN0U4bDJvVWV1dVRhZ0N3Yk5wMncPCWFkX2N1cnNvcg4PD2dsb2JhbF9wb3NpdGlvbgIADwZvZmZzZXQCAA8QbGFzdF9hZF9wb3NpdGlvbgL/AQ=="
}
```

**Use Case**
- Get the posts of a user by `profile_id`
- Timeline analysis of user's posts

---

### 6. Profile Details
Fetch user profile metadata.

**Endpoint**
```
GET  {URL}/FB_rapid/profile/details

https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_cd7a94c1-5880-434f-8119-121c1589a464
```

**Inputs**
- `profile_url` (required): full Facebook profile URL

**Example response**
```
{
  "profile": {
    "name": "Narendra Modi",
    "profile_id": "100044527235621",
    "url": "https://www.facebook.com/narendramodi",
    "image": "https://scontent-lhr8-1.xx.fbcdn.net/v/t39.30808-1/459337720_1303104714517091_2841079786125894817_n.jpg?stp=dst-jpg_s480x480_tt6&_nc_cat=107&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=gpaAhpb1Q8cQ7kNvwFD2uKF&_nc_oc=AdpLO6WFpZwMRDTmAdB-qy3Hph1oqa8YCSqI70GKFJFFo05yNFkjtxIaa9U_7ZVA3g4&_nc_zt=24&_nc_ht=scontent-lhr8-1.xx&_nc_gid=ZYFgh_aVTmU8C-RQFgmA3Q&_nc_ss=7a389&oh=00_Af2NpeolsDcd2CMM0L7wx4u7Bjwdt-6ItD4AjQFl1TfSTg&oe=69E3D69E",
    "intro": "Prime Minister of India.",
    "cover_image": "https://scontent-lhr6-2.xx.fbcdn.net/v/t39.30808-6/573634163_1626580965502796_839119417535673119_n.png?_nc_cat=104&ccb=1-7&_nc_sid=2a1932&_nc_ohc=5d1Mfh_lLHgQ7kNvwEja-4B&_nc_oc=AdocAgc3P0ubHF3p-aB95DuznmkMrdTiL-FnwooLQgkETAMGTFpHwF8CqMmgXrRG27Q&_nc_zt=23&_nc_ht=scontent-lhr6-2.xx&_nc_gid=ZYFgh_aVTmU8C-RQFgmA3Q&_nc_ss=7a389&oh=00_Af27uDQz8AFS3yKRgbzf-EQlDJ_mrbpVKteDGS8oXWubIg&oe=69E3CF3A",
    "gender": "MALE",
    "about": {},
    "about_public": [
      {
        "icon": {
          "height": 40,
          "scale": 2,
          "uri": "https://static.xx.fbcdn.net/rsrc.php/yz/r/77rw1oPmYdg.webp",
          "width": 40
        },
        "text": "Page · Politician",
        "external_url": null
      },
      {
        "icon": {
          "height": 40,
          "scale": 2,
          "uri": "https://static.xx.fbcdn.net/rsrc.php/yc/r/FUgdr-WWpnL.webp",
          "width": 40
        },
        "text": "https://youtube.com/narendramodi",
        "external_url": "https://youtube.com/@narendramodi"
      },
      {
        "icon": {
          "height": 40,
          "scale": 2,
          "uri": "https://static.xx.fbcdn.net/rsrc.php/yx/r/oXHzaZ4Cp6w.webp",
          "width": 40
        },
        "text": "narendramodi.in",
        "external_url": "https://l.facebook.com/l.php?u=http%3A%2F%2Fwww.narendramodi.in%2F&h=AT7CbBRc85MJJknNWH437ous8S_4aqwnpRTCzPYlXW94K5funXtj2WviZlUVsAQT1qDX956ayZcloq4Jh9bdoYDtnWq-M09GjNevGOPQ1bzFfuhOeLk6dL5E4mCOiKJ8Y52oYkGXTL3aoEhB9W7wRcaRrDY&s=1"
      }
    ],
    "verified": true,
    "delegate_page_id": null,
    "reels_profile_id": "YXBwX2NvbGxlY3Rpb246cGZiaWQwMkMxdmpBS2JXa1NZTDgzV2k4dURuN2RTOFhDY3RDR0c1cW1YeFltMnppTjl3aFZWTHl4SmJhOTRpQ2pBelJOSGdITUNIV3dubld6VGFNaldVRUFUWjJnYndxeEQ5cGlZdTI2RDJMbA==",
    "influencer_category": "Page · Politician",
    "education": null,
    "current_city": null,
    "hometown": null,
    "relationship": null,
    "member_since": null,
    "reels_page_id": "YXBwX2NvbGxlY3Rpb246cGZiaWQwMkMxdmpBS2JXa1NZTDgzV2k4dURuN2RTOFhDY3RDR0c1cW1YeFltMnppTjl3aFZWTHl4SmJhOTRpQ2pBelJOSGdITUNIV3dubld6VGFNaldVRUFUWjJnYndxeEQ5cGlZdTI2RDJMbA=="
  }
}
```

**Use Case**
- Get all profile page data
- Metadata extraction

---

### 7. Page Details
Fetch Facebook page metadata.

**Endpoint**
```
GET  {URL}/FB_rapid/profile/page/details

https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_847dc586-dd05-4660-a838-128c872a1407
```

**Inputs**
- `page_url` (required): full Facebook page URL

**Example**
```
{
  "results": {
    "name": "Narendra Modi",
    "type": "page",
    "page_id": "100044527235621",
    "url": "https://www.facebook.com/narendramodi",
    "image": "https://scontent-ord5-1.xx.fbcdn.net/v/t39.30808-1/459337720_1303104714517091_2841079786125894817_n.jpg?stp=dst-jpg_s480x480_tt6&_nc_cat=1&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=gpaAhpb1Q8cQ7kNvwHpCcR5&_nc_oc=AdpCbQ9ipwSkwhK2bImxoMyRiay1IZ-mhw6nI5fQC-YYJJlXDvNOFKQ3kMQbu7P2ozM&_nc_zt=24&_nc_ht=scontent-ord5-1.xx&_nc_gid=30JYvKjV6FebN3N-tLfaAQ&_nc_ss=7a389&oh=00_Af2DuBmce3nO8NH7CqlL16903ff2ukgDxqfRFpjed7xCtQ&oe=69E3D69E",
    "intro": "Prime Minister of India.",
    "likes": null,
    "followers": 55000000,
    "following": 0,
    "categories": [
      "Page",
      "Politician"
    ],
    "phone": null,
    "email": null,
    "address": null,
    "rating": null,
    "services": null,
    "price_range": null,
    "website": "narendramodi.in",
    "delegate_page": {
      "id": "177526890164",
      "pamv_comms_data": null
    },
    "cover_image": "https://scontent-ord5-1.xx.fbcdn.net/v/t39.30808-6/573634163_1626580965502796_839119417535673119_n.png?_nc_cat=1&ccb=1-7&_nc_sid=2a1932&_nc_ohc=5d1Mfh_lLHgQ7kNvwH9zE5T&_nc_oc=AdpcnsWd77jrjturmQYua44MI8iiL6eiBh3bZrPpSbhceDtWbyXAfxa9aw2rCS0hlos&_nc_zt=23&_nc_ht=scontent-ord5-1.xx&_nc_gid=30JYvKjV6FebN3N-tLfaAQ&_nc_ss=7a389&oh=00_Af0hETDIlVK0vxemrAjsPEuexl30dqvadYO6F3rVOaY0xQ&oe=69E3CF3A",
    "verified": true,
    "other_accounts": [
      {
        "url": "https://youtube.com/@narendramodi"
      }
    ],
    "reels_page_id": "YXBwX2NvbGxlY3Rpb246cGZiaWQwMkMxdmpBS2JXa1NZTDgzV2k4dURuN2RTOFhDY3RDR0c1cW1YeFltMnppTjl3aFZWTHl4SmJhOTRpQ2pBelJOSGdITUNIV3dubld6VGFNaldVRUFUWjJnYndxeEQ5cGlZdTI2RDJMbA=="
  }
}
```

**Use Case**
- Page analytics (followers_count, following_count, post_count, categories, is_verified, etc)

---

### 8. Get Profile ID
Resolve username or URL to profile ID.

**Endpoint**
```
GET  {URL}/FB_rapid/profile/get-profile-id

https://rapidapi.com/krasnoludkolo/api/facebook-scraper3/playground/apiendpoint_e8f05277-cc6d-4e96-bd1d-725c861eb9e4
```

**Inputs**
- `profile_url` (required): full Facebook profile/page URL

**Example**
```
{
  "profile_id": "100044527235621"
}
```

**Use Case**
- Get the `profile_id` (e.g. `100044226919512`) using the FB URL (e.g. `https://www.facebook.com/SachinTendulkar`)
- `profile_id` is used by other APIs like **User Posts**

---
---
---
---
## Apify
Visit `https://console.apify.com/actors` and search by actor id:
1) fetch_facebook_profile : `4Hv5RhChiaDk6iwad`
2) get_facebook_profile_id : `4Hv5RhChiaDk6iwad`
3) get_all_facebook_posts : `KoJrdxJCTtpon81KY`
4) get_post_comments : `us5srxAYnsrkgUv2v`
5) get_followers_following : `hhgonmMEMGmpbDDAN`

Notes:
- slow: avg time 10–20 seconds
- heavy: resource intensive (RAM/time)

---

## Limitations

- Only public data is accessible
- Followers list / large data may be unavailable or difficult to access
- link's are temporary

---

## FB Apify (Apify) APIs

Notes:
- These endpoints use **Apify** via `fb_apify/` (slower than RapidAPI).
- Inputs are passed as **query parameters**.
- Requires `APIFY_TOKEN` in SUTRA `.env`.

### Environment variables (SUTRA `.env`)
```
APIFY_TOKEN=<YOUR_APIFY_TOKEN>
FACEBOOK_PAGE_ACTOR=4Hv5RhChiaDk6iwad
```

Server base "URL" (example):
```
http://localhost:8000
```

### 1. Profile Details (Apify)
Fetch Facebook profile/page details.

**Endpoint**
```
GET {URL}/FB_apify/profile/profile
```

**Inputs**
- `url` (required): Facebook profile/page URL

**Example response**
```
{
  "status": "success",
  "data": {
    "facebookUrl": "https://www.facebook.com/narendramodi",
    "categories": [
      "Page",
      "Politician"
    ],
    "info": [
      "Narendra Modi. 55,590,201 likes",
      "12,949,013 talking about this. Prime Minister of India."
    ],
    "likes": 55590201,
    "messenger": null,
    "title": "Narendra Modi",
    "pageId": "100044527235621",
    "pageName": "narendramodi",
    "pageUrl": "https://www.facebook.com/narendramodi",
    "intro": "Prime Minister of India.",
    "websites": [
      "https://youtube.com/@narendramodi",
      "http://www.narendramodi.in/"
    ],
    "alternativeSocialMedia": "https://youtube.com/@narendramodi",
    "website": "http://www.narendramodi.in/",
    "followers": 55590202,
    "followings": 0,
    "profilePictureUrl": "https://scontent-msp1-1.xx.fbcdn.net/v/t39.30808-1/459337720_1303104714517091_2841079786125894817_n.jpg?stp=dst-jpg_s200x200_tt6&_nc_cat=1&ccb=1-7&_nc_sid=f907e8&_nc_ohc=gpaAhpb1Q8cQ7kNvwHCMDXg&_nc_oc=AdqW60bW2VKG8mZK1JgMs1zjB1hzXtq0sERhz86eGAmujN2HitJkSJWAIm7CqkNKCoI&_nc_zt=24&_nc_ht=scontent-msp1-1.xx&_nc_gid=vz3LXVG8RMXUpwhpdXPc3w&_nc_ss=7a389&oh=00_Af2jh8ZyxdYS9M-kNbgwnAS-AKxvzGq8p-TzQm0PTT2amA&oe=69E4EFDE",
    "coverPhotoUrl": "https://scontent-msp1-1.xx.fbcdn.net/v/t39.30808-6/573634163_1626580965502796_839119417535673119_n.png?_nc_cat=1&ccb=1-7&_nc_sid=2a1932&_nc_ohc=lQB0w7GslawQ7kNvwHdDDRG&_nc_oc=Adq6q7RPUdpg2RwmGIbCzeWbKFnjZjfXLuAT5nFW0_dFCnFiEPBlQS1EuS4EFMe5JTQ&_nc_zt=23&_nc_ht=scontent-msp1-1.xx&_nc_gid=rKQwpFQIrgIdTj4LOQUZBg&_nc_ss=7a389&oh=00_Af0gQJFXhZai5gxEdTOCK8SToXTPPVe0Ybg85nQtzSQ3pA&oe=69E4E87A",
    "profilePhoto": "https://www.facebook.com/photo/?fbid=1303104711183758&set=a.538824284278475",
    "category": "Politician",
    "youtube": [
      {
        "username": "https://youtube.com/narendramodi",
        "url": "https://youtube.com/@narendramodi"
      }
    ],
    "creation_date": "May 5, 2009",
    "ad_status": "This Page isn't currently running ads.",
    "facebookId": "100044527235621",
    "pageAdLibrary": {
      "id": "177526890164",
      "pamv_comms_data": null
    }
  }
}
```

---

### 2. Get Profile ID (Apify)
Get the `facebookId` from a Facebook profile/page URL.

**Endpoint**
```
GET {URL}/FB_apify/profile/get_profile_id
```

**Inputs**
- `url` (required): Facebook profile/page URL

**Example response**
```
{
  "facebookId": "100044527235621"
}
```

---

### 3. Get All Posts (Apify)
Fetch recent posts for a profile/page.

**Endpoint**
```
GET {URL}/FB_apify/profile/posts/all
```

**Inputs**
- `url` (required): Facebook profile/page URL
- `resultsLimit` (optional, int): default `10`

**Example response**
```
[
  {
    "facebookUrl": "https://www.facebook.com/p/The-Label-Jenn-100084236786813/",
    "postId": "955713720579845",
    "pageName": "p",
    "url": "https://www.facebook.com/permalink.php?story_fbid=pfbid02DQ8mxxirEoi1MLLvvNQ3Av9hLBmM3xcpg86WuYP2jFNmKzpBtLq9F1XsWBrMZT1Xl&id=100084236786813",
    "time": "2026-04-15T16:05:55.000Z",
    "timestamp": 1776269155,
    "user": {
      "id": "100084236786813",
      "name": "The Label Jenn",
      "profileUrl": "https://www.facebook.com/100084236786813",
      "profilePic": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.30808-1/298514810_107577528727687_2550087521856375265_n.jpg?stp=cp0_dst-jpg_s50x50_tt6&_nc_cat=106&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=B7JvS3tx0J4Q7kNvwFh_82T&_nc_oc=Ado6_1zVeHCHnGFk4YJgNv5P_v64it5Pqq5TL4TWZvTtc8Y2sK9_oQiFimiICxxWH9w&_nc_zt=24&_nc_ht=scontent-atl3-1.xx&_nc_gid=8o9p3odBinwtk-rGO1bi4Q&_nc_ss=7a389&oh=00_Af3Lv4ydQUThGmZkOKFGWnzJj4dTchX_wSDKmKoRSWm22Q&oe=69E67203"
    },
    "collaborators": [],
    "text": "Muscle drape,textured fall and a statement fit // April2026 - Signature drape pants",
    "likes": 0,
    "shares": 0,
    "topReactionsCount": 0,
    "media": [
      {
        "mediaset_token": "pcb.955713720579845",
        "url": "https://www.facebook.com/permalink.php?story_fbid=pfbid02DQ8mxxirEoi1MLLvvNQ3Av9hLBmM3xcpg86WuYP2jFNmKzpBtLq9F1XsWBrMZT1Xl&id=100084236786813",
        "comet_product_tag_feed_overlay_renderer": null
      },
      {
        "thumbnail": "https://scontent-atl3-2.xx.fbcdn.net/v/t51.82787-15/670867972_18111566821833192_8578014998912072662_n.jpg?stp=dst-jpg_s590x590_tt6&_nc_cat=105&ccb=1-7&_nc_sid=13d280&_nc_ohc=QBd-xN6ucawQ7kNvwHIgYlu&_nc_oc=AdrZmjFH6ZsoRhvz6ZpiLBfTIYvUwPkfW2-mGh_sdYCM1fr9wKvVzbpfJvHey3vQP3A&_nc_zt=23&_nc_ht=scontent-atl3-2.xx&_nc_gid=8o9p3odBinwtk-rGO1bi4Q&_nc_ss=7a389&oh=00_Af3VaI7tGB2thRHjL08cUhTP2wOnITLv64E5Wh6yNjIUCw&oe=69E66C69",
        "__typename": "Photo",
        "is_playable": false,
        "image": {
          "uri": "https://scontent-atl3-2.xx.fbcdn.net/v/t51.82787-15/670867972_18111566821833192_8578014998912072662_n.jpg?stp=dst-jpg_s590x590_tt6&_nc_cat=105&ccb=1-7&_nc_sid=13d280&_nc_ohc=QBd-xN6ucawQ7kNvwHIgYlu&_nc_oc=AdrZmjFH6ZsoRhvz6ZpiLBfTIYvUwPkfW2-mGh_sdYCM1fr9wKvVzbpfJvHey3vQP3A&_nc_zt=23&_nc_ht=scontent-atl3-2.xx&_nc_gid=8o9p3odBinwtk-rGO1bi4Q&_nc_ss=7a389&oh=00_Af3VaI7tGB2thRHjL08cUhTP2wOnITLv64E5Wh6yNjIUCw&oe=69E66C69",
          "height": 590,
          "width": 443
        },
        "id": "955713677246516",
        "__isMedia": "Photo",
        "photo_cix_screen": null,
        "copyright_banner_info": null,
        "owner": {
          "__typename": "User",
          "id": "100084236786813"
        },
        "ocrText": "No photo description available."
      },
  
    ],
    "feedbackId": "ZmVlZGJhY2s6OTU0OTMzMTAzOTkxMjQw",
    "topLevelUrl": "https://www.facebook.com/100084236786813/posts/954933103991240",
    "facebookId": "100084236786813",
    "pageAdLibrary": {
      "id": "107575558727884",
      "pamv_comms_data": null
    },
    "inputUrl": "https://www.facebook.com/p/The-Label-Jenn-100084236786813/"
  }
]
```

---

### 4. Post Comments (Apify)
Fetch comments for a specific post URL.

**Endpoint**
```
GET {URL}/FB_apify/comments/post_comments
```

**Inputs**
- `post_url` (required): Facebook post URL
- `includeNestedComments` (optional, bool): default `false`
- `resultsLimit` (optional, int): default `10`
- `viewOption` (optional, str): default `RANKED_UNFILTERED`

**Example response**
```
[
  {
    "facebookUrl": "https://www.facebook.com/narendramodi/posts/pfbid0TNN7bJimZrcE8zzzT1dJktrdC6y6AJKJDKmucJQioC2EWA75nzBm54RorMZ4SicHl",
    "commentUrl": "https://www.facebook.com/narendramodi/posts/pfbid02WjrJDL5PbYoYfn2KwmzgKaLeMmfiaBp6fGWBfFczWqk7G9a8UMYHsHGu6p2KwQowl?comment_id=1762203608483871",
    "commentId": "1762203608483871",
    "id": "Y29tbWVudDoxNzU1MDMwODUyNjU3ODA2XzE3NjIyMDM2MDg0ODM4NzE=",
    "feedbackId": "ZmVlZGJhY2s6MTc1NTAzMDg1MjY1NzgwNl8xNzYyMjAzNjA4NDgzODcx",
    "date": "2026-04-15T11:01:33.000Z",
    "text": "Our Hon'ble PM Shri Narendra Modiji today shared pictures from his visit to the Sri Adichunchanagiri Mahasamsthana Math. During the visit, he went to the Jwala Peetha and offered prayers at the Sri Kalabhairava Temple, seeking divine blessings for the peace, prosperity and well-being of the nation.🙏🙏",
    "profileUrl": "https://www.facebook.com/rakesh.kalia.142",
    "profilePicture": "https://scontent-xxc1-1.xx.fbcdn.net/v/t1.6435-1/44677346_1893119557410053_1759918847319605248_n.jpg?stp=cp0_dst-jpg_s32x32_tt6&_nc_cat=104&ccb=1-7&_nc_sid=e99d92&_nc_ohc=ErnV-1Ucq-YQ7kNvwGDvRZh&_nc_oc=AdoqjuoUP1i9IGSvug8HzD9xjMjRcy1paUMBq902U63osn-Fa__TFPMqbOs2NkiPA_8&_nc_zt=24&_nc_ht=scontent-xxc1-1.xx&_nc_gid=5tj62N-C7_qDgkPJL_fLyA&_nc_ss=7a389&oh=00_Af3KxVJtQqW_ms-wSvR5zNMK9L5U6VuP1pylkQ2oToiiBg&oe=6A07F953",
    "profileId": "pfbid02YL8fFMBrE5VyX3WTuGVJc9KAKaZWF3Aeoee6xLNk9Lv8rc8ewpM9oAUn1bt9QuM3l",
    "profileName": "Rakesh Kalia",
    "likesCount": "14",
    "commentsCount": 1,
    "comments": [],
    "threadingDepth": 0,
    "facebookId": "1755030852657806",
    "postTitle": "At the Sri Adichunchanagiri Mahasamsthana Math, visited the Jwala Peetha and prayed at Sri Kalabhairava Temple.",
    "pageAdLibrary": {
      "is_business_page_active": false,
      "id": "177526890164"
    },
    "inputUrl": "https://www.facebook.com/narendramodi/posts/pfbid0TNN7bJimZrcE8zzzT1dJktrdC6y6AJKJDKmucJQioC2EWA75nzBm54RorMZ4SicHl"
  },

]
```

---

### 5. Followers / Following (Apify)
Fetch followers/followings list for a profile/page URL.

**Endpoint**
```
GET {URL}/FB_apify/follow/followers_followings
```

**Inputs**
- `profile_url` (required): Facebook profile/page URL
- `resultsLimit` (optional, int): default `10`

**Example response**
```
[
  {
    "facebookUrl": "https://www.facebook.com/p/The-Label-Jenn-100084236786813/",
    "followType": "follower",
    "id": "100044312295290",
    "image": "https://scontent-lga3-3.xx.fbcdn.net/v/t39.30808-1/557282842_1387587412728322_7417138558890258053_n.jpg?stp=cp0_dst-jpg_s80x80_tt6&_nc_cat=104&ccb=1-7&_nc_sid=167101&_nc_ohc=okJmZcYBGoEQ7kNvwGic5p6&_nc_oc=AdoQ-aPaGGTXdHx8A0xZIRCZgStXRyVlSYfdSTj5Orvp3j82yQdHHQlfd1g18ejRLbE&_nc_zt=24&_nc_ht=scontent-lga3-3.xx&_nc_gid=UHSiUVKsuJ6_ApM5-CMfSQ&_nc_ss=7a389&oh=00_Af0jxs9C9GYV5xcXCtSkepUA6UgrJpRq6Q9jkG8nLGKq2w&oe=69E655F4",
    "title": "Mirchi Manali",
    "subtitle_text": "",
    "url": "https://www.facebook.com/rjmanali.fanpage",
    "privacy_scope": null,
    "__typename": "User",
    "__isEntity": "User",
    "facebookId": "100084236786813",
    "navSections": [
      {
        "id": "YXBwX2NvbGxlY3Rpb246cGZiaWQwSkFhQzlDaG1odjc2dEdaVnpUVkRrTWV4RWVpWWFnbTFrcHFrRHlKU2dlWjhhYjNFbmUxTlZuUW56UGV3U3pLS1ZXU01TQ1ZvQ3NGMVlwQkVuWWF1Zzg4YlNjaTllbA==",
        "name": "Followers",
        "url": "https://www.facebook.com/people/The-Label-Jenn/100084236786813/?sk=followers"
      }
    ],
    "pageAdLibrary": {
      "is_business_page_active": false,
      "id": "107575558727884"
    },
    "followersId": "YXBwX2NvbGxlY3Rpb246cGZiaWQwSkFhQzlDaG1odjc2dEdaVnpUVkRrTWV4RWVpWWFnbTFrcHFrRHlKU2dlWjhhYjNFbmUxTlZuUW56UGV3U3pLS1ZXU01TQ1ZvQ3NGMVlwQkVuWWF1Zzg4YlNjaTllbA==",
    "inputUrl": "https://www.facebook.com/p/The-Label-Jenn-100084236786813/"
  },
  {
    "facebookUrl": "https://www.facebook.com/p/The-Label-Jenn-100084236786813/",
    "followType": "follower",
    "id": "100063836663636",
    "image": "https://scontent-lga3-2.xx.fbcdn.net/v/t39.30808-1/300524571_467941092010442_6585022432526833542_n.jpg?stp=cp0_dst-jpg_s80x80_tt6&_nc_cat=105&ccb=1-7&_nc_sid=167101&_nc_ohc=DCyNT5bQTvoQ7kNvwENc1Gp&_nc_oc=AdpPW4xqYcMHoGVgYAWV5s0PYExZNExwMq1ZwtVWLUCwzTjpaZm40kGyFXT7_Cq5Rek&_nc_zt=24&_nc_ht=scontent-lga3-2.xx&_nc_gid=UHSiUVKsuJ6_ApM5-CMfSQ&_nc_ss=7a389&oh=00_Af3JYdG3aFvHKnmvY4d1iQDJS3pUE0xxa3dceY_W77t3cg&oe=69E65686",
    "title": "Kareem Western Tack",
    "subtitle_text": "",
    "url": "https://www.facebook.com/people/Kareem-Western-Tack/100063836663636/",
    "privacy_scope": null,
    "__typename": "User",
    "__isEntity": "User",
    "facebookId": "100084236786813",
    "navSections": [
      {
        "id": "YXBwX2NvbGxlY3Rpb246cGZiaWQwSkFhQzlDaG1odjc2dEdaVnpUVkRrTWV4RWVpWWFnbTFrcHFrRHlKU2dlWjhhYjNFbmUxTlZuUW56UGV3U3pLS1ZXU01TQ1ZvQ3NGMVlwQkVuWWF1Zzg4YlNjaTllbA==",
        "name": "Followers",
        "url": "https://www.facebook.com/people/The-Label-Jenn/100084236786813/?sk=followers"
      }
    ],
    "pageAdLibrary": {
      "is_business_page_active": false,
      "id": "107575558727884"
    },
    "followersId": "YXBwX2NvbGxlY3Rpb246cGZiaWQwSkFhQzlDaG1odjc2dEdaVnpUVkRrTWV4RWVpWWFnbTFrcHFrRHlKU2dlWjhhYjNFbmUxTlZuUW56UGV3U3pLS1ZXU01TQ1ZvQ3NGMVlwQkVuWWF1Zzg4YlNjaTllbA==",
    "inputUrl": "https://www.facebook.com/p/The-Label-Jenn-100084236786813/"
  },

  {
    "url": "https://www.facebook.com/p/The-Label-Jenn-100084236786813/",
    "error": "no_items",
    "errorDescription": "Empty or private data for provided input"
  }
]
```
