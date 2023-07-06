// Outputs needed for deployment - Needed in the Gitlab CI deployment phase
output "ecr_repo_url" {
  description = "The ECR Repository URL."
  value       = module.ecr_repository.url
}
