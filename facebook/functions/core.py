import requests
from datetime import date, datetime
from typing import Optional, Union
from facebook.fb_config import fb_config


def get_headers():
    return {
        "X-RapidAPI-Key": fb_config.FB_RAPIDAPI_KEY,
        "X-RapidAPI-Host": fb_config.FB_RAPIDAPI_HOST
    }


def make_request(url: str, method: str = "GET", params: dict = None):
    try:
        if params is not None:
            params = {k: v for k, v in params.items() if v is not None}

        response = requests.request(
            method=method,
            url=url,
            headers=get_headers(),
            params=params,
            timeout=10
        )
        print(f"Request URL: {response.url}")
        
        if response.status_code != 200:
            raise Exception(
                f"FB API Error | {response.status_code} | {response.text}"
            )

        return response.json()

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request Failed: {str(e)}")


def parse_to_date(
    value: Optional[Union[str, date, datetime]],
    field_name: str,
) -> Optional[date]:
    if value is None:
        return None

    if isinstance(value, datetime):
        return value.date()

    if isinstance(value, date):
        return value

    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be a string in YYYY-MM-DD format")

    raw = value.strip()
    if not raw:
        return None

    try:
        return date.fromisoformat(raw)
    except ValueError as e:
        raise ValueError(f"Invalid {field_name}. Use YYYY-MM-DD (e.g. 2026-04-14).") from e


_parse_to_date = parse_to_date
