// How to use ECR Module: https://senndergmh.atlassian.net/wiki/x/pYC_PQ
// ECR Module Input Variables: https://gitlab.com/sennder/engineering-effectiveness/platform/terraform-module-ecr-repository/-/blob/master/README.md
// ECR Module Releases: https://gitlab.com/sennder/engineering-effectiveness/platform/terraform-module-ecr-repository/-/tags

// Please go through the module release notes to see the breaking changes.
// Terraform Help Channel: https://sennder.slack.com/archives/C01AQC06DPX

locals {
  team      = "driver-app"
  ba        = "carriers-and-drivers"
  namespace = "sennder"
  project   = "pizza-api-app"
}

module "ecr_repository" {
  source  = "gitlab.com/sennder/terraform-module-ecr/platform"
  version = ">= 5, < 6"

  name                = "${local.namespace}/${local.team}/${local.project}"
  allow_mutable_tags  = var.allow_mutable_tags
  scan_on_push        = var.scan_on_push
  tag_prefix          = var.tag_prefix
  keep_images         = var.keep_images
  keep_untagged_days  = var.keep_untagged_days
  component_name      = local.project
  force_delete        = true
}
