import utils.service as service
import json
permissions_set_policies = {}

def list_permission_sets(sso_instance_arn, access_key_id, secret_access_key, session_token):
    AWSClient = service.AWSBoto3Service(sso_instance_arn, access_key_id, secret_access_key, session_token)
    permissons_sets = AWSClient.sso_list_permissions_set()['PermissionSets']
    for permission_set_id in permissons_sets:
        permission_set = AWSClient.sso_describe_permission_set(permission_set_id)['PermissionSet']
        policy = AWSClient.sso_get_inline_policy_for_permission_set(permission_set_id)['InlinePolicy']
        permissions_set_policies[permission_set['Name']] = {}
        permissions_set_policies[permission_set['Name']]['Policy'] = json.loads(policy) if policy else None
        permissions_set_policies[permission_set['Name']]['PermissionSetArn'] = permission_set['PermissionSetArn']
        permissions_set_policies[permission_set['Name']]['Description'] = permission_set.get('Description',None)
        print(".")
    return permissions_set_policies