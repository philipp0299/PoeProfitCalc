import json

import ratelimited_requests


def get_current_league(standard=False, hc=False, ruthless=False):
    headers = {'User-Agent': 'PoeProfitCalc (https://github.com/Dakri7/PoeProfitCalc.git)',
               'accept': 'application/json'}
    # TODO current league
    api_endpoint = "http://www.pathofexile.com/api/leagues"
    query_response = ratelimited_requests.get(api_endpoint, headers=headers)
    all_leagues = json.loads(query_response.content)
    for league in all_leagues:
        id = league["id"]
        rules = league["rules"]
        end_at = league["endAt"]
        if contains_rule(rules, "NoParties"):
            continue
        if contains_rule(rules, "Hardcore") == hc and contains_rule(rules, "Ruthless") == ruthless:
            if standard == (end_at is None):
                return id


def contains_rule(rules, rule_id):
    for rule in rules:
        if rule["id"] == rule_id:
            return True
    return False
