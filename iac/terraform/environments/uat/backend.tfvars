// https://www.terraform.io/docs/backends/types/s3.html
// Sennder's Terraform Remote State Management: https://gitlab.com/sennder/platform/terraform-base
// How-To migrate to the secure Terraform Remote State bucket @ Sennder https://senndergmh.atlassian.net/l/c/ufBBx6Zz

// IMP: The TF state key is being passed via the pipeline. If you want to test locally, please refer to the gitlab-ci.yml
bucket         = "uat-remote-state2023062216351247900000000a"
region         = "eu-central-1"
encrypt        = "true"
dynamodb_table = "uat-remote-state-lock"
kms_key_id     = "4492389b-86e3-4f46-9900-37e456e47e9a"
profile        = "uat"

// Important "key" must be set on the cli
