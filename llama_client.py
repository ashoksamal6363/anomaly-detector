
import base64, json, requests
import variables as v

def analyze_frame(image_bytes, camera_id):
    payload = {
        "system_prompt": v.LLAMA_SYSTEM_PROMPT,
        "camera_id": camera_id,
        "image_base64": base64.b64encode(image_bytes).decode()
    }
    headers = {"Authorization": f"Bearer {v.LLAMA_API_KEY}", "Content-Type": "application/json"}
    try:
        r = requests.post(v.LLAMA_ENDPOINT_URL, headers=headers, data=json.dumps(payload), timeout=v.HTTP_REQUEST_TIMEOUT)
        r.raise_for_status()
        return r.json()
    except Exception:
        return {"anomaly": False, "reason": "error"}
