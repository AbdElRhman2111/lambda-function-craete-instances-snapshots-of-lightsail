from __future__ import print_function
import boto3
from datetime import datetime, timedelta
from os import getenv
from sys import stdout
from time import time


AUTO_SNAPSHOT_SUFFIX = 'auto'


def lambda_handler(event, context):
    client = boto3.client('lightsail')
    _snapshot_instances(client)


def _snapshot_instances(client, time=time, out=stdout):
    for page in client.get_paginator('get_instances').paginate():
        for instance in page['instances']:
            snapshot_name = '{}-system-{}-{}'.format(instance['name'],
                                                     int(time() * 1000),
                                                     AUTO_SNAPSHOT_SUFFIX)

            client.create_instance_snapshot(instanceName=instance['name'],
                                            instanceSnapshotName=snapshot_name)
            print('Created Snapshot name="{}"'.format(snapshot_name), file=out)