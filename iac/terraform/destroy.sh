#!/usr/bin/env bash

env=$1
folder="app"

case ${env} in
  "dev" | "prod")
    ;;
  "shared")
    folder=${env}
    ;;
  *)
    echo "Undefined environment. Please use 'dev', 'prod' or 'shared'."
    exit 0
    ;;
esac

function exit_on_error {
  echo $1
  exit 1
}

cd terraform/${folder}

terraform init -upgrade -backend=true -backend-config=../environments/${env}/backend.tfvars --backend-config="key=driver-app/pizza-api-app-app/infrastructure/${env}.tfstate" || exit_on_error "could not initialize terraform"

terraform destroy \
-var-file=../environments/${env}/variables.tfvars
