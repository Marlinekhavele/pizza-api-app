

resource "aws_ssm_parameter" "database_master_password" {
  name        = "/${local.team}/${local.project}/${var.env}/database_master_password"
  description = "The RDS DB Password"
  type        = "SecureString"
  value       = var.database_master_password
}

module "rds" { // https://senndergmh.atlassian.net/wiki/x/DQFrQ
  source  = "gitlab.com/sennder/terraform-module-rds/platform"
  version = ">= 7, < 8"

  team           = local.team
  project        = local.project
  region         = var.region
  namespace      = local.namespace
  env            = var.env
  component_name = local.project

  database_name  = var.database_name
  engine         = var.engine
  engine_version = var.engine_version
  instance_class = var.instance_class
  storage_size   = var.storage_size
  port           = var.port

  username      = var.username
  password      = aws_ssm_parameter.database_master_password.value

  deletion_protection     = var.deletion_protection
  backup_retention_period = var.backup_retention_period
  monitoring_interval     = var.monitoring_interval
  allow_vpn_access        = true

  enable_replication      = true

  switch_off = var.switch_off # only affects non-prod envs

  providers = {
    aws       = aws
    aws.admin = aws.admin
  }
}


