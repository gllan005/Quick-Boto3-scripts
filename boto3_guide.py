#import resource
from lib2to3.pytree import LeafPattern
import boto3
import uuid  # universal unique identifier for unique bucket name

def create_bucket_name(bucket_prefix):
    # bucket name must be between 3-63 chars long
    return "".join([bucket_prefix, str(uuid.uuid4())])


# --------------right way to do it---------------------
def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    if current_region == "us-east-1":
        bucket_response = s3_connection.create_bucket(
            Bucket=bucket_name)
    else:
        bucket_response = s3_connection.create_bucket(
             Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': current_region
            }
        )
    print(bucket_name, current_region)
    return bucket_name, bucket_response


s3_resource = boto3.resource('s3')
first_bucket_name, first_response = create_bucket(bucket_prefix='gabefirstpythonbuckettt',
                                                  s3_connection=s3_resource.meta.client)

print("bucket name: ", first_bucket_name)
print("response: ", first_response)
# gabefirstpythonbucketttc42d75b9-4c74-40bd-a488-7eea2e28cf04 us-east-1


###################### NOTES ##########################
# bucket names cannot have capital Letters 
# create ~/.aws in git bash because something weird happens with Windows commands
# if current region is in us-east-1 you have to remove CreateBucketConfiguration api all together,
# the LocationConstraint is by default set to us-east-1 if region is not sepcified.

#While the name space for buckets is global, 
# S3 (like most of the other AWS services) runs in each AWS region (see the AWS Global 
# Infrastructure page for more information).
#######################################################


# # test bucket name creation
# print(create_bucket_name("test_name"))

# -------------- Manual way of create S3 bucket in different regions------------

# resource.create_bucket(Bucket=YOUR_BUCKET_NAME,
#                        CreateBucketConfiguration={
#                            "LocationConstraint": "eu-west-1"
#                        })


# -------------- This wont work with us-east-1 as a constraint with LocationConstraint -------------
# -------------                          with boto3 and aws                            -------------

# def create_bucket(bucket_prefix, s3_connection):
#     session = boto3.session.Session()
#     current_region = session.region_name
#     bucket_name = create_bucket_name(bucket_prefix)
#     bucket_response = s3_connection.create_bucket(
#         Bucket = bucket_name,
#         CreateBucketConfiguration = {
#             "LocationConstraint": current_region
#         }
#     )
#     print(bucket_name, current_region)
#     return bucket_name, bucket_response


