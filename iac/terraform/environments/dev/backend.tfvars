// https://www.terraform.io/docs/backends/types/s3.html
// Sennder's Terraform Remote State Management: https://gitlab.com/sennder/platform/terraform-base
// How-To migrate to the secure Terraform Remote State bucket @ Sennder https://senndergmh.atlassian.net/l/c/ufBBx6Zz

// IMP: The TF state key is being passed via the pipeline. If you want to test locally, please refer to the gitlab-ci.yml
bucket         = "dev-remote-state20210210134116421900000002"
region         = "eu-central-1"
encrypt        = "true"
dynamodb_table = "dev-remote-state-lock"
kms_key_id     = "6d1839d7-7445-4759-8a60-2227ce9b29d2"
profile        = "dev"

// Important "key" must be set on the cli
