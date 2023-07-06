#!/usr/bin/env bash
env=$1
case ${env} in
  "dev" | "prod")
  VAR="--var-file=../environments/${env}/variables.tfvars"
  ;;
  "shared")
  VAR=""
  ;;
  *)
  echo "Undefined environment. Please use 'shared' or 'dev' or 'prod' as an argument."
  exit 0
  ;;
esac
function exit_on_error {
  echo $1
  exit 1
}
terraform init -upgrade -backend=true -backend-config=backend.tfvars --backend-config="key=driver-app/pizza-api-app-app/infrastructure/${env}.tfstate"|| exit_on_error "could not initialize terraform"
terraform destroy $VAR
