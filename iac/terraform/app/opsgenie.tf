module "opsgenie_service" {
  source  = "gitlab.com/sennder/terraform-module-opsgenie-service/platform"
  version = ">= 1, < 2"

  project        = local.project
  description    = "Opsgenie service for ${local.project}"
  environment    = var.env
  team           = local.team
  ba             = local.ba
  pod            = local.team
  service_name   = "${local.namespace}-${var.env}-${local.project}"
  component_name = local.project

  opsgenie_api_key = var.opsgenie_api_key
}
