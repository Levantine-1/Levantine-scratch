import boto3

service='rekognition'
#accessKey='AKIAVIFHHUHTI7XLR3EL'
#secretKey='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'
accessKey='AKIAVIFHHUHTHFH4XWVR'
secretKey='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'
defaultRegion='us-west-1'
session = boto3.client(service,
                        aws_access_key_id=accessKey,
                        aws_secret_access_key=secretKey,
                        region_name=defaultRegion)

bucket='project-theia-test'
photo='subaru1997wrc.jpg'

if __name__ == "__main__":
    response = session.detect_labels(Image={'S3Object':
                                                {'Bucket':bucket,
                                                 'Name':photo}},
                                            MaxLabels=100)
    print(response)