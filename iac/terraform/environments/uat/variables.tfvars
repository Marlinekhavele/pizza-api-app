// https://www.terraform.io/docs/cloud/workspaces/variables.html
// We use Terraform workspaces and load workspace/environment specific variables from files

env = "uat"

container_environment = {}

allowed_origins = ["*"]


engine         = "postgres"
engine_version = "14"
instance_class = "db.t4g.micro"
storage_size   = "25"
database_name  = "pizzaapiappdev"
username       = "pizzaapiapp"
port           = "5432"
switch_off     = true

