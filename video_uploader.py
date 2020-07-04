import os
import boto3
from dotenv import load_dotenv
load_dotenv()


session = boto3.session.Session()
client = session.client('s3',
                        region_name='sgp1',
                        endpoint_url='https://sgp1.digitaloceanspaces.com',
                        aws_access_key_id=os.getenv('SPACES_KEY'),
                        aws_secret_access_key=os.getenv('SPACES_SECRET'))


def video_uploader(file_path, file_id, video_quality):

    client.put_object(Bucket='brightway',
                      Key='videos/'+file_id+"-"+video_quality+".mp4",
                      Body=open(file_path, 'rb'),
                      ACL='private',
                      ContentType='video/mp4')
