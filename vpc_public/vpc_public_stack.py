from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2  
    # aws_sqs as sqs,
)
from constructs import Construct

CIDR = '192.168.0.0/16'

class VpcPublicStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(
            self,
            'two-tier',
            cidr=CIDR,
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name='public',
                    subnet_type=ec2.SubnetType.PUBLIC
                ),
                ec2.SubnetConfiguration(
                    name='private',
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT
                ),
            ]
        )
