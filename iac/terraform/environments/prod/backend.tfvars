// https://www.terraform.io/docs/backends/types/s3.html
// Sennder's Terraform Remote State Management: https://gitlab.com/sennder/platform/terraform-base
// How-To migrate to the secure Terraform Remote State bucket @ Sennder https://senndergmh.atlassian.net/l/c/ufBBx6Zz

// IMP: The TF state key is being passed via the pipeline. If you want to test locally, please refer to the gitlab-ci.yml
bucket         = "prod-remote-state20210222150757926600000007"
region         = "eu-central-1"
encrypt        = "true"
dynamodb_table = "prod-remote-state-lock"
kms_key_id     = "8a3e531d-7b9e-41ae-8d16-82b7e2151e56"
profile        = "prod"

// Important "key" must be set on the cli
