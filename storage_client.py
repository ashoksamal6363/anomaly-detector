
from azure.storage.blob import BlobServiceClient, ContentSettings
from datetime import datetime
import variables as v

client = BlobServiceClient.from_connection_string(v.AZURE_STORAGE_CONNECTION_STRING)
container = client.get_container_client(v.AZURE_STORAGE_CONTAINER_NAME)

def save_frame(image_bytes, is_anomaly, camera_id, ts):
    folder = ts.strftime(v.ANOMALY_PATH_PATTERN if is_anomaly else v.NON_ANOMALY_PATH_PATTERN)
    name = f"{folder}/{camera_id}_{int(ts.timestamp())}.jpg"
    container.upload_blob(name, image_bytes, overwrite=True,
        content_settings=ContentSettings(content_type="image/jpeg"))
    return container.get_blob_client(name).url
