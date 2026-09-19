import requests
from requests.auth import HTTPBasicAuth as auth


def get_details(url, username, password, timeout=10):
	response = requests.get(
		url,
		auth=auth(username, password),
		timeout=timeout,
	)
	response.raise_for_status()
	payload = response.json()
	return payload["details"]


if __name__ == "__main__":
	details = get_details(
		"http://127.0.0.1:5000/index",
		"Bhaskar",
		"mandiya",
	)
	print(details)
