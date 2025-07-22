import requests
from utils import config
import logging

class BaseAPI:
    def __init__(self, base_url=None):
        self.base_url = base_url or config.BASE_URL
    
    def get(self, endpoint, headers=None, params=None):
        try:
            response = requests.get(f"{self.base_url}{endpoint}", headers=headers or config.DEFAULT_HEADERS, params=params, timeout=10)
            response.raise_for_status()
            return response
        except requests.RequestException as e: 
            logging.error(f"GET {endpoint} failed: {e}")
            raise
    
    def post(self, endpoint, json, headers=None):
        try:
            response = requests.post(f"{self.base_url}{endpoint}", 
             json=json, headers=headers or config.DEFAULT_HEADERS,timeout=10)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logging.error(f"POST {endpoint} failed: {e}")
            return None

    def put(self, endpoint, json, headers=None):
        try:
            response = requests.put(f"{self.base_url}{endpoint}", json=json, headers=headers or config.DEFAULT_HEADERS, timeout=10)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logging.error(f"PUT {endpoint} failed: {e}")
    
    def delete(self, endpoint, headers=None):
        try:
            response = requests.delete(f"{self.base_url}{endpoint}", headers=headers or config.DEFAULT_HEADERS, timeout=10)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logging.error(f"DELETE {endpoint} failed: {e}")