#!/bin/bash

PROJECT=LambdaRestart

# Change the suffix on the bucket to something unique!
BUCKET=lambd4buck3t

# generate next stage yaml file
aws cloudformation package                   \
    --template-file template.yaml            \
    --output-template-file ./output.yaml \
    --s3-bucket $BUCKET

# the actual deployment step
aws cloudformation deploy                     \
    --template-file ./output.yaml         \
    --stack-name $PROJECT                     \
    --capabilities CAPABILITY_IAM
