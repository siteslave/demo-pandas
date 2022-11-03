from minio import Minio

client = Minio("203.157.102.60:39000", access_key="1tFEA44fhZIkmmr0", secret_key="W0SnAWhVE9yB9LRvqwbvxV3cCVxPVbfs", secure=False)

buckets = client.list_objects(bucket_name="airflow")
for bucket in buckets:
    file_name = bucket.object_name
    try:
        client.fget_object(bucket_name="airflow", object_name=file_name, file_path=f"./tmp/{file_name}")
    
    except Exception:
        print(Exception)
    