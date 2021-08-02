from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_cloud9 as cloud9,
    aws_iam as iam,
)
from app_context import (
    Parameters,
)

class Cloud9(core.NestedStack):

    def __init__(self, scope: core.Construct, id: str, bmt_vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # https://aws.amazon.com/ko/blogs/security/isolating-network-access-to-your-aws-cloud9-environments/
        
        # ec2.InterfaceVpcEndpoint(self, 'ssm',
        #     vpc=bmt_vpc,
        #     service=ec2.InterfaceVpcEndpointAwsService.SSM,
        #     subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.ISOLATED)
        # )

        # ec2.InterfaceVpcEndpoint(self, 'ssm-msg',
        #     vpc=bmt_vpc,
        #     service=ec2.InterfaceVpcEndpointAwsService.SSM_MESSAGES,
        #     subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.ISOLATED)
        # )

        # ec2.InterfaceVpcEndpoint(self, 'ecr',
        #     vpc=bmt_vpc,
        #     service=ec2.InterfaceVpcEndpointAwsService.ECR,
        #     subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.ISOLATED)
        # )

        # ec2.InterfaceVpcEndpoint(self, 'ecr-dkr',
        #     vpc=bmt_vpc,
        #     service=ec2.InterfaceVpcEndpointAwsService.ECR_DOCKER,
        #     subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.ISOLATED)
        # )
        # https://github.com/aws/aws-cdk/issues/14423 definition of S3 on InterfaceVpcEndpointAwsService is missing


        param = Parameters.instance()
        cloud9.CfnEnvironmentEC2(self, 'benchmark', 
            instance_type='m5.large',
            automatic_stop_time_minutes=60,
            connection_type='CONNECT_SSM',
            subnet_id=bmt_vpc.private_subnets[0].subnet_id,
            owner_arn=param.getParameter('cloud9_owner_arn')
        )