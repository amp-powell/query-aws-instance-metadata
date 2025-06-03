import requests
import json
import sys

# This is the local-link address for IPv4
METADATA_URL = "http://169.254.169.254/latest"

def get_token():
    # Retrieve a session token for IMDSv2
    try:
        response = requests.put(
            f"{METADATA_URL}/api/token",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
            timeout=2
        )
        response.raise_for_status()
        return response.text

    except requests.RequestException as e:
        raise SystemExit(f"Error getting token: {e}")

# Recursively retrieves metadata to make sure json has all directory info
def get_metadata(token, key_path = ''):
    url = f"{METADATA_URL}/meta-data/{key_path}"

    try:
        response = requests.get(
            url, 
            headers = {"X-aws-ec2-metadata-token": token}, 
            timeout = 2)

        response.raise_for_status()

        if key_path and not key_path.endswith("/"):
            return response.text

        data = {}

        for item in response.text.strip().split("\n"):
            curr_key = item.strip("/")
            value = get_metadata(token, f"{key_path}{item}")
            data[curr_key] = value

        return data

    except requests.RequestException as e:
        raise SystemExit(f"Failed to get metadata at {url}: {e}")

def get_metadata_json(key = ''):
    token = get_token()
    if (key):
        return json.dumps({key.strip("/"): get_metadata(token, key)}, indent = 4)

    return json.dumps(get_metadata(token), indent = 4)

def main():
    if (len(sys.argv) > 1):
        key = sys.argv[1]
        return get_metadata_json(key)

    return get_metadata_json()

if __name__ == "__main__":
    result = main()
    print(result)

