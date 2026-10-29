import requests


class APIClientGet:
    def __init__(self, url: str):
        self.url = url

    def get_data(self):
        try:
            response = requests.get(self.url, timeout=10)

            if response.status_code == 200:
                print("The API call was successful and response was retrieved.")
                return response.json()
            else:
                raise Exception(
                    f"API call failed with status code: {response.status_code}"
                )

        except requests.exceptions.RequestException as e:
            raise Exception(f"Error while calling API: {e}")


class APIClientResource:
    def __init__(self, url: str, query_params: dict = None):
        self.url = url
        self.query_params = query_params or {}

    def get_data(self):
        try:
            response = requests.get(
                self.url,
                params=self.query_params,
                timeout=(10, 30),
                # 10 seconds for connection timeout and 30 sec for read timeout
            )

            if response.status_code == 200:
                # raises https status code for unsuccessful https status code and None for 200 series
                print("The API call was successful and response was retrieved.")
                return response.json()

            raise Exception(f"API call failed with status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            raise Exception(f"Error while calling API: {e}")


if __name__ == "__main__":
    url = "https://dummyjson.com/products"
    # url = "https://dummyjson.com/carts"
    query_params = {"limit": 10, "skip": 5}

    resource_client = APIClientResource(url, query_params)

    try:
        result = resource_client.get_data()
        print(result)
    except Exception as e:
        print(f"Error: {e}")
