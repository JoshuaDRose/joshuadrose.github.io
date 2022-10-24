"""
Description: Analyses the webpage with google's Page Speed Insights
Built by: Joshua Rose
"""

import os
import sys
import json
import requests
import subprocess

__url__ = os.path.split(os.getcwd())[1]


def format_json_data(_response_json) -> (str | None):
    if isinstance(_response_json, requests.Response):
        return json.dumps(_response_json.json(), indent=4);
    elif not isinstance(_response_json, dict):
        raise TypeError

def recv_url_data() -> requests.Response:
    _response = requests.get(f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://{__url__}')
    return _response

def concat_dict(_dict):
    data = json.dumps(_dict["lighthouseResult"]["audits"]["metrics"]["details"]["items"])
    return json.loads(data)

def index_json(_response: dict) -> None:
    print(type(concat_dict(_response)))
    print("""
Page Speed Insights
===================
Chrome UX Report
---------------------
Contentful Paint: {content_paint}
Input Delay: {input_delay}
Lighthouse Audit Results
---------------------
Speed Index: {speed_index}
TTI: {time_to_interactive}
CPU Idle: {cpu_idle}
Input Latency: {input_latency}""".format(
    content_paint=concat_dict(_response).index("observedFirstContentfulPaint"),
    input_delay=concat_dict(_response).index('observedNavigationStart'),
    speed_index=concat_dict(_response).index("observedSpeedIndex"),
    time_to_interactive=concat_dict(_response).index("interactive")
))

_response = recv_url_data();

print(index_json(_response.json()))
