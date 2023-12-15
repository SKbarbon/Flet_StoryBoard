import requests



def is_connected_to_internet ():
    try:
        requests.get("https://google.com", timeout=5)
        return True
    except:
        return False


if __name__ == "__main__":
    print(is_connected_to_internet())