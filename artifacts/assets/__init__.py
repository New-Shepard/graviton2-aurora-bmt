import constructs
from aws_cdk import (
    core,
    aws_s3,
    aws_s3_deployment,
)

class BenchmarkAssets():

    def __init__(self, scope: constructs.Construct) -> None:

        s3_bucket = aws_s3.Bucket(scope, 'bmt',
            # BucketAccessControl.PRIVATE: Owner gets FULL_CONTROL. No one else has access rights.    
            access_control=aws_s3.BucketAccessControl.PRIVATE,
            block_public_access=aws_s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=core.RemovalPolicy.DESTROY
        )
        self.s3_bucket_name = s3_bucket.bucket_name

        aws_s3_deployment.BucketDeployment(scope, 'bmt-assets',
            destination_bucket=s3_bucket,
            sources=[aws_s3_deployment.Source.asset('artifacts/assets/resources')],
        )
