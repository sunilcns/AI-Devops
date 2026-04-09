import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import datetime 


# This script checks if the required files exist in the S3 bucket
# It checks for the following files:
# S3 bucket name : a204956_s3_logs
# S3 path : s3://a204956_s3_logs/YYYY/MM/DD/
# S3 file format : extension of file is .txt 
# Sometimes files will not be generated, in that case the date folder will be empty. So we need to check if the file exists or not.
# finally i want to schedule this script as aws lambda to run it daily at 8:00 AM UTC time.
# it should take current date and check for the files in the S3 bucket for that date. If the files are not found, it should print a message saying "Files not found for YYYY/MM/DD". If the files are found, it should print a message saying "Files found for YYYY/MM/DD".


def check_s3_files(bucket_name, date):
    s3 = boto3.client('s3')
    prefix = date.strftime('%Y/%m/%d/')
    
    try:
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
        if 'Contents' in response:
            print(f"Files found for {prefix}")
        else:
            print(f"Files not found for {prefix}")
    except NoCredentialsError:
        print("Credentials not available")
    except ClientError as e:
        print(f"Client error: {e}")


if __name__ == "__main__":
    bucket_name = "a204956_s3_logs"
    current_date = datetime.datetime.utcnow().date()
    check_s3_files(bucket_name, current_date)

    
