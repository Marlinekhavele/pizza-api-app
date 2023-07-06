// A provider is responsible for understanding API interactions and exposing resources.
// https://registry.terraform.io/providers/hashicorp/aws/latest/docs


// Only Allowed in SennCloud CICD account
// CICD Architecture: https://senndergmh.atlassian.net/l/c/jsJZ31fq
provider "aws" {
  allowed_account_ids = ["075050162388"]
  region              = var.region
  profile             = "cicd" // This is because we are creating ECR repositories in one account (CICD) and using them elsewhere.

  default_tags {
    tags = module.tags.default_tags
  }
}
