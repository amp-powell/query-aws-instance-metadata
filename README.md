# Query AWS EC2 Instances

These are python scripts to query the metadata of EC2 instances within AWS and print out a json of the output. They are meant for python 3.8 and later.

You can retrieve the data of a specific key by adding on the key as an additional argument.

The script query_specific_ec2_metadata.py is meant for querying the metadata of a specific instance. To use it, you MUST set up [boto3](https://github.com/boto/boto3) and include the instance id as the first script argument.

