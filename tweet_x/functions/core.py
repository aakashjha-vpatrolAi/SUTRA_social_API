from __future__ import annotations

from typing import Any, Mapping, Optional

import requests

from tweet_x.x_config import x_config

def get_headers():
    return {
        "Authorization": f"Bearer {x_config.X_BEARER_TOKEN}"
    }

def make_request(
    url: str,
    params: Optional[Mapping[str, Any]] = None,
    method: str = "GET",
    json: Optional[Mapping[str, Any]] = None,
    data: Optional[Mapping[str, Any]] = None,
):
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=get_headers(),
            params=params,
            json=json,
            data=data,
            timeout=x_config.tweet_REQUEST_TIMEOUT,
        )

        if response.status_code != 200:
            raise Exception(f"X API Error | Status: {response.status_code} | Response: {response.text}")

        return response.json()

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request Failed: {str(e)}")
