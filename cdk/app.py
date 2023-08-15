# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
#!/usr/bin/env python3

import aws_cdk as cdk 

from eks_vpc.eks_vpc import EKSVPCCdkStack

env_EU=cdk.Environment(region="eu-west-2", account="xxxxx")

app = cdk.App()

eks_vpc = EKSVPCCdkStack(
    scope=app,
    id="eks-vpc",
    env=env_EU
)

app.synth()
