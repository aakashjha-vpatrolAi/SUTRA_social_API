from apify_client import ApifyClient
from fb_apify.fb_apify_config import apify_settings


def get_apify_client() -> ApifyClient:
    return ApifyClient(apify_settings.APIFY_TOKEN)


def run_actor(actor_id: str, run_input: dict):
    client = get_apify_client()

    run = client.actor(actor_id).call(run_input=run_input)

    dataset_id = run.get("defaultDatasetId")

    results = []
    for item in client.dataset(dataset_id).iterate_items():
        results.append(item)

    return results