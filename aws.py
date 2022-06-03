import logging
import boto3
from botocore.exceptions import ClientError
import os

class S3:
    """handle all S3 things

    :param profile_name: Profile to use, see https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html?highlight=credentials#shared-credentials-file
    """

    def __init__(self, profile_name):
        self.__session = boto3.Session(profile_name=profile_name)

    def create_presigned_url(self, bucket_name, object_name, expiration=3600):
        """Generate a presigned URL to share an S3 object

        :param bucket_name: string
        :param object_name: string
        :param expiration: Time in seconds for the presigned URL to remain valid
        :return: Presigned URL as string. If error, returns None.
        """

        # Generate a presigned URL for the S3 object
        s3_client = self.__session.client('s3')
        try:
            response = s3_client.generate_presigned_url('get_object',
                                                        Params={'Bucket': bucket_name,
                                                                'Key': object_name},
                                                        ExpiresIn=expiration)
        except ClientError as e:
            logging.error(e)
            return None

        # The response contains the presigned URL
        return response


    def upload_file(self, file_name, bucket, object_name=None):
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :param make_public: Make the object read-public. Defaults to true.
        :return: True if file was uploaded, else False
        """

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = os.path.basename(file_name)

        # Upload the file
        s3_client = self.__session.client('s3')
        try:
            response = s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def object_exists(self, bucket, key):
        """Check if an object already exists in an S3 bucket

        :param bucket: Bucket to upload to
        :param object_name: S3 object name.
        :return: True if object exists in bucket, else False
        """

        s3_client = self.__session.client('s3')
        try:
            the_object = s3_client.get_object(Bucket=bucket, Key=key)
        except ClientError:
            if ex.response['Error']['Code'] == 'NoSuchKey':
                logging.info('Object with key {} not found'.format(key))
                return False
        return True
