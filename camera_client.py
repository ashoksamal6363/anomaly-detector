
import requests
from requests.auth import HTTPBasicAuth
import variables as v

def grab_frame(camera):
    try:
        auth = HTTPBasicAuth(camera["username"], camera["password"]) if camera.get("username") else None
        r = requests.get(camera["snapshot_url"], auth=auth, timeout=v.HTTP_REQUEST_TIMEOUT)
        r.raise_for_status()
        return r.content
    except Exception:
        return None
