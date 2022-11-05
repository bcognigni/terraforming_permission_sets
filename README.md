# Terraforming permission sets
Use this repo to terraform your permission sets from AWS IAM Identity Center.

## Usage
First you have to load your terraform configuration in main.tf file.

After that you have to import your permissions sets, generate terraform files and the bash script.
```sh
python3 tf_files_generator.py
```
Now we need to init our terraform workload
```sh
cd terraform
terraform init
```

Finally we have to running our sh file to import permission sets to terraform.tfstate file
```sh
sh terraform_import_permission_sets.sh
```

Now you can extract your terraform configuration from /terraform folder 
