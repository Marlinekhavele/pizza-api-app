// Backed type S3 for Terraform Remote State Management: https://www.terraform.io/docs/backends/types/s3.html
// Terraform Remote State Management @ Sennder https://www.terraform.io/docs/backends/types/s3.html
// How-To migrate to the secure Terraform Remote State bucket @ Sennder https://senndergmh.atlassian.net/l/c/ufBBx6Zz


// We are defining an empty block of backend config and it will be passed using workspace variables
// example: terraform init -backend=true -backend-config=environments/${CI_ENVIRONMENT_NAME}/backend.tfvars
terraform {
  backend "s3" {
  }
}