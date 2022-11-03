from minio import Minio

client = Minio("203.157.102.60:39000", access_key="1tFEA44fhZIkmmr0", secret_key="W0SnAWhVE9yB9LRvqwbvxV3cCVxPVbfs", secure=False)

obj = client.fget_object(bucket_name="airflow", object_name="satit-air-20221101045810.zip")

print(obj)


