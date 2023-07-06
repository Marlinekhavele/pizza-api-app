module "tags" {
  source  = "gitlab.com/sennder/terraform-module-global-aws-tags/platform"
  version = ">= 3, < 4"

  environment  = var.env
  project_name = local.project
  ba           = local.ba
  team         = local.team
  pod          = local.team

  git_last_commit_author    = var.git_last_commit_author
  git_last_commit_short_sha = var.git_last_commit_short_sha
  git_repository_url        = var.git_repository
  project_id                = var.project_id
}

variable "git_last_commit_author" {
  default     = null
  type        = string
  description = "The Latest Commit Author"
}

variable "git_last_commit_short_sha" {
  default     = null
  type        = string
  description = "The Latest Short Commit Sha"
}

variable "git_repository" {
  default     = null
  type        = string
  description = "GitLab Project URL"
}

variable "project_id" {
  default     = null
  type        = string
  description = "GitLab Project ID"
}
