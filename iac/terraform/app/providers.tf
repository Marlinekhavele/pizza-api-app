// A provider is responsible for understanding API interactions and exposing resources.
// https://registry.terraform.io/providers/hashicorp/aws/latest/docs

provider "aws" {
  region              = var.region
  allowed_account_ids = [lookup(local.account_id, var.env)]
  profile             = var.env

  default_tags {
    tags = module.tags.default_tags
  }
}

provider "aws" {
  alias               = "admin"
  region              = var.region
  allowed_account_ids = ["471588272217"]
  profile             = "admin"
  default_tags {
    tags = module.tags.default_tags
  }
}

provider "opsgenie" {
  api_key = var.opsgenie_api_key  # parametrise
  api_url = "api.eu.opsgenie.com" #default is api.opsgenie.com
}

provider "kubernetes" {
  host                   = data.aws_eks_cluster.default.endpoint
  cluster_ca_certificate = base64decode(data.aws_eks_cluster.default.certificate_authority[0].data)
  exec {
    api_version = "client.authentication.k8s.io/v1beta1"
    args        = ["eks", "get-token", "--cluster-name", local.cluster_name, "--profile", "${var.env}"]
    command     = "aws"
  }
}
