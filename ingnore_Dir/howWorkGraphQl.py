import requests


def get_access_token(url, query):
    # Prepare the request headers
    headers = {"Content-Type": "application/json"}
    payload = {"query": query}
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        json_response = response.json()
        token = json_response["data"]["login"]["access_token"]
        return token
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


# Example usage:
graphql_url = "https://api.ceasta.com/graphql"
graphql_mutation = """
mutation Login2 {
    login(
        loginUserInput: { password: "12345678", username: "blankchip.zapta@gmail.com" }
    ) {
        access_token
    }
}
"""

access_token = get_access_token(graphql_url, graphql_mutation)

if access_token:
    print("Access Token:", access_token)
else:
    print("Failed to obtain access token.")
