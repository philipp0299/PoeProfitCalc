import requests
import time

rate_limit_queues = {}


def get(url, json=None, headers=None):
    resp = requests.get(url, json=json, headers=headers)
    handle_rate_limits(resp)
    return resp


def post(url, json=None, headers=None):
    resp = requests.post(url, json=json, headers=headers)
    handle_rate_limits(resp)
    return resp


def handle_rate_limits(response):
    rate_limit_str = response.headers.get("x-rate-limit-ip")
    rate_limit_state_str = response.headers.get("x-rate-limit-ip-state")
    rate_limit_state = rate_limit_state_str.split(",")
    rate_limits = rate_limit_str.split(",")
    for i in range(len(rate_limits)):
        limit = rate_limits[i]
        limit_state = rate_limit_state[i]
        limit_state_parts = limit_state.split(":")
        count_previous_requests = int(limit_state_parts[0])
        limit_parts = limit.split(":")
        num_requests = int(limit_parts[0]) - 1  # -1 Because another request has already been sent
        window_size = int(limit_parts[1])
        if limit in rate_limit_queues:
            queue = rate_limit_queues[limit]
        else:
            queue = [time.time()] * count_previous_requests
            rate_limit_queues[limit] = queue
        queue = list(filter(lambda timestamp: timestamp > time.time() - window_size, queue))
        if len(queue) < num_requests:
            queue.append(time.time())
        else:
            wait_duration = queue[0] + window_size - time.time()
            time.sleep(wait_duration)
            queue.append(time.time())
            queue = list(filter(lambda timestamp: timestamp > time.time() - window_size, queue))
        rate_limit_queues[limit] = queue
