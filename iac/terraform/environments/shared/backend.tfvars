// https://www.terraform.io/docs/backends/types/s3.html
// Sennder's Terraform Remote State Management: https://gitlab.com/sennder/platform/terraform-base
// How-To migrate to the secure Terraform Remote State bucket @ Sennder https://senndergmh.atlassian.net/l/c/ufBBx6Zz

// IMP: The TF state key is being passed via the pipeline. If you want to test locally, please refer to the gitlab-ci.yml
bucket         = "cicd-remote-state20210211155158711600000002"
region         = "eu-central-1"
kms_key_id     = "a1a767d0-32dd-4aa7-91bd-cf2d89b2f83b"
encrypt        = "true"
profile        = "cicd"
dynamodb_table = "cicd-remote-state-lock"

// Important "key" must be set on the cli
