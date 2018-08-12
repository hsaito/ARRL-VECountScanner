import requests as req
from bs4 import BeautifulSoup as bs
import re


def parse_call_name(entry: str) -> (str, str):
    item = re.match("(.*?)\((.*?)\)", entry)
    return item.group(1).strip(), item.group(2).strip()


def get_state(state: str, state_name: str) -> []:
    state_page = req.get("http://www.arrl.org/ve-session-counts?state=" + state)
    soup = bs(state_page.text, "html.parser")
    ve_entry = soup.find("table").find_all("tr")

    result = []

    for ve_item in ve_entry:
        entry = ve_item.find_all("td")
        if entry:
            name, call = parse_call_name(entry[0].text)
            stat_entry = [name, call, state_name, int(entry[1].text)]
            result.append(stat_entry)
    return result
