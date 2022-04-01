import boto3

s3 = boto3.resource('s3')
response = s3.meta.client.list_buckets()

print(response)
print('\nExisting buckets\n')

buckets_to_delete = []

for buckets in response['Buckets']:
    bucket_name = buckets["Name"]
    print(f' {bucket_name}')
    if 'gabefirstpython' in bucket_name:
        response = s3.meta.client.delete_bucket(Bucket=bucket_name)
        print("deleted bucket: ", bucket_name)


print('\nRemaining buckets\n')
response = s3.meta.client.list_buckets()

for buckets in response['Buckets']:
    bucket_name = buckets["Name"]
    print(f' {bucket_name}')