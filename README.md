# lambda-function-craete-instances-snapshots-of-lightsail


## This Function Target Lightsail of Amazon web Service by `Python 3.9` has Target all region by defualt of lightsail and check about instances and Create snapshot with naming convention current time and suffix getting From value of `AUTO_SNAPSHOT_SUFFIX` if want useing with specific region follow example

```py
def lambda_handler(event, context):
    client = boto3.client('lightsail','region_name')
    _snapshot_instances(client)
```



# Create Policies for granting Role permission to Access Resources Go to `Identity and Access Management (IAM)` and create Policies

## lightsail Access Policy 

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "lightsail:DeleteDiskSnapshot",
                "lightsail:GetInstanceSnapshot",
                "lightsail:DeleteInstanceSnapshot",
                "lightsail:GetAutoSnapshots",
                "lightsail:GetInstanceSnapshots",
                "lightsail:DeleteAutoSnapshot",
                "lightsail:CreateInstanceSnapshot"
            ],
            "Resource": "*"
        }
    ]
```
## cloudwatch Access Policy

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "cloudwatch:*",
            "Resource": "*"
        }
    ]
}
```

## Create Role by previous Policies for granting Lambda permission to Access Resources make sure about role type `AWS service` and Common use cases for `Lambda` let's Create Function don't forget used Created Role for Lambda

## let's Create Function don't forget Change value of function Timeout 

![image.png](/image.png)

![image2.png](/image2.png)







