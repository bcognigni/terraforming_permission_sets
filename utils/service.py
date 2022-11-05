import boto3 
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html


class AWSBoto3Service():
    def __init__(self, sso_instance_arn, access_key_id, secret_access_key, session_token):
        self.sso_instance_arn = sso_instance_arn
        self.client = self.get_client(access_key_id, secret_access_key, session_token)

    def get_client(self, access_key_id, secret_access_key, session_token):
        client = boto3.client(
            'sso-admin', 
            region_name='us-east-1',
            aws_access_key_id= access_key_id,
            aws_secret_access_key= secret_access_key,
            aws_session_token= session_token
        )
        return client

    def sso_list_permissions_set(self):
        response = self.client.list_permission_sets(
            InstanceArn= self.sso_instance_arn,
            MaxResults=100
        )
        return response

    def sso_describe_permission_set(self, permission_set_arn):
        response = self.client.describe_permission_set(
            InstanceArn= self.sso_instance_arn,
            PermissionSetArn= permission_set_arn
        )
        return response

    def sso_get_inline_policy_for_permission_set(self, permission_set_arn):
        response = self.client.get_inline_policy_for_permission_set(
            InstanceArn= self.sso_instance_arn,
            PermissionSetArn=permission_set_arn,
        )
        return response

