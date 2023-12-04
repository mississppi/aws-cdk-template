import aws_cdk as core
import aws_cdk.assertions as assertions

from vpc_public.vpc_public_stack import VpcPublicStack

# example tests. To run these tests, uncomment this file along with the example
# resource in vpc_public/vpc_public_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = VpcPublicStack(app, "vpc-public")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
