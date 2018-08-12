import requests as req
from bs4 import BeautifulSoup as bs


def get_state_list() -> {}:
    main_page = req.get("http://www.arrl.org/ve-session-counts")
    soup = bs(main_page.text, "html.parser")

    state_list = soup.find("select", attrs={"name": "state"}).find_all("option")

    state_dictionary = {}

    for state_item in state_list:
        if state_item.text != "- Select -":
            state_dictionary[state_item["value"]] = state_item.string

    return state_dictionary
