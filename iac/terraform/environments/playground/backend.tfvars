// https://www.terraform.io/docs/backends/types/s3.html
// Sennder's Terraform Remote State Management: https://gitlab.com/sennder/platform/terraform-base
// How-To migrate to the secure Terraform Remote State bucket @ Sennder https://senndergmh.atlassian.net/l/c/ufBBx6Zz

// IMP: The TF state key is being passed via the pipeline. If you want to test locally, please refer to the gitlab-ci.yml
bucket         = "play-remote-state20210531134533083800000007"
region         = "eu-central-1"
encrypt        = "true"
dynamodb_table = "play-remote-state-lock"
kms_key_id     = "fc4fadc2-33e9-490e-b174-4cbb86d5f891"
profile        = "playground"

// Important "key" must be set on the cli
