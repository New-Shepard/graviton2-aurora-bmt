from aws_cdk import (
    core,
    aws_ec2 as ec2,
)

class Network(core.NestedStack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.vpc = ec2.Vpc(self, "vpc",
            cidr="10.100.0.0/16",
            max_azs=2,
            nat_gateways=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name='public',
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=18
                ),
                ec2.SubnetConfiguration(
                    name='private',
                    subnet_type=ec2.SubnetType.PRIVATE,
                    cidr_mask=18
                )
            ]
        )