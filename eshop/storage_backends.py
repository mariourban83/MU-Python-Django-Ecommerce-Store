from storages.backends.s3boto3 import S3Boto3Storage

# For serving staticfiles from AWS bucket


class MediaStorage(S3Boto3Storage):
    bucket_name = 'eshop-static-s3'
    location = 'media'


class StaticStorage(S3Boto3Storage):
    bucket_name = 'eshop-static-s3'
    location = 'static'
