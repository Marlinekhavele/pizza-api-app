#!/usr/bin/env bash
sed -i 's#ssh://git@#https://gitlab-ci-token:'"${CI_JOB_TOKEN}"'@#g' *.tf
echo terraform init -backend=true -backend-config=../environments/${CI_ENVIRONMENT_NAME}/backend.tfvars  -backend-config="key=driver-app/pizza-api-app-app/infrastructure/${CI_ENVIRONMENT_NAME}.tfstate"
terraform init -backend=true -backend-config=../environments/${CI_ENVIRONMENT_NAME}/backend.tfvars  -backend-config="key=driver-app/pizza-api-app-app/infrastructure/${CI_ENVIRONMENT_NAME}.tfstate"
