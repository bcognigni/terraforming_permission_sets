
import json
from list_all_permission_sets import list_permission_sets

instance_arn = input("SSO Instance Arn:\n")
access_key_id = input('Access Key ID:\n')
secret_access_key = input('Secret Access Key:\n')
session_token = input('Session Token (Leave blank if none):\n') or None
print("\nHold on a sec")

permission_sets = list_permission_sets(instance_arn, access_key_id, secret_access_key, session_token)


with open('terraform/terraform_import_permission_sets.sh', 'w') as f:
        f.write("#! usr/bin/bash")

for key in permission_sets.keys():
    permission_sets[key]
    data = "resource \"aws_ssoadmin_permission_set\" \"{}\" ".format(key)+"{\r\n    name             = \""+"{}\"\r\n    instance_arn     = \"{}\"\r\n    session_duration = \"PT8H\"\r\n    description = \"{}\"".format(key,instance_arn,permission_sets[key]['Description'])+"\r\n}\r\n\n"
    data = data + "resource \"aws_ssoadmin_permission_set_inline_policy\" \"{}_policy\"".format(key)+ " {"+"\r\n  instance_arn       = aws_ssoadmin_permission_set.{}.instance_arn\r\n  permission_set_arn = aws_ssoadmin_permission_set.{}.arn\r\n  inline_policy      = <<CONTENT\n".format(key, key)
    data = data + json.dumps(permission_sets[key]['Policy'], sort_keys=True, indent=4) + "\nCONTENT\n}"
    with open('terraform/{}.tf'.format(key), 'w') as f:
        f.write(data)
    bash = "\nterraform import aws_ssoadmin_permission_set.{} {},{} && ".format(key, permission_sets[key]['PermissionSetArn'], instance_arn)
    bash = bash + "terraform import aws_ssoadmin_permission_set_inline_policy.{}_policy {},{}".format(key, permission_sets[key]['PermissionSetArn'], instance_arn)
    with open('terraform/terraform_import_permission_sets.sh'.format(key), 'a') as f:
        f.write(bash)


