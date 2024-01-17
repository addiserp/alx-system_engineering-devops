#!/usr/bin/python3
"""
DD_SITE="datadoghq.com" DD_API_KEY="412c489f19920750e1b864bc61d37d0a" DD_APP_KEY="5640d9215cfa1cec037fdbb99aab5a343013fc4f" python3 get-dashboard-datadog.py
"""
import sys
import requests

"""
Get all dashboards returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.list_dashboards(
        filter_shared=False,
    )

    print(response)
