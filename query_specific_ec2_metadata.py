import boto3
import json
import sys

def get_specific_ec2_metadata(instanceId, key = ''):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(InstanceIds=[instanceId])
    instance = response['Reservations'][0]['Instances'][0]
    
    if (key):
        return json.dumps({key: instance.get(key, f"Key '{key}' not found.")}, indent = 4)

    return json.dumps(instance, indent = 4)

def main():
    if (len(sys.argv) < 2):
        raise SystemExit(f"Needs an argument for specific instance id")
    
    instanceId = sys.argv[1]

    if (len(sys.argv) > 2):
        key = sys.argv[2]
        return get_specific_ec2_metadata(instanceId, key)

    return get_specific_ec2_metadata(instanceId)

if __name__ == "__main__":
    result = main()
    print(result)

