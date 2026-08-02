import os
from openai import AsyncOpenAI as OriginalAsyncOpenAI
from openai._base_client import DEFAULT_MAX_RETRIES
from openai._types import NOT_GIVEN

class AsyncOpenAI(OriginalAsyncOpenAI):
    def __init__(self, *, api_key = None, organization = None, project = None, base_url = None, timeout = NOT_GIVEN, max_retries = DEFAULT_MAX_RETRIES, default_headers = None, default_query = None, http_client = None, _strict_response_validation = False):
        api_key = "dummy_key"
        base_url = os.environ.get("BASE_URL", "http://localhost:8000/v1")
        print("FIXED TO USE LOCAL MODEL!!")
        super().__init__(api_key=api_key, organization=organization, project=project, base_url=base_url, timeout=timeout, max_retries=max_retries, default_headers=default_headers, default_query=default_query, http_client=http_client, _strict_response_validation=_strict_response_validation)
    
    