from bs4 import BeautifulSoup
import requests
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_site_favicon(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    favicon_link = soup.find('link', rel='icon') or soup.find('link', rel='shortcut icon') or soup.find('link', rel='apple-touch-icon')
    try:
        favicon_url = favicon_link['href']
        if str(favicon_url).startswith("http"):
            return f"{favicon_url}"
        else:
            return f"{url}/{favicon_url}"
    except:
        return None
