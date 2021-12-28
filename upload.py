# 引用套件
from google.cloud import storage
# 建立跟cloud storage 溝通的客戶端
storage_client = storage.Client()
# 桶子, 物件, 本地檔案事先指定好
bucket_name="road-project-picture/U3dfebbd05927687e3e912e2d98f6905e/corrdinate"
destination_blob_name="l.txt"
source_file_name="location.json"
# 正式上傳檔案至bucket內
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)
