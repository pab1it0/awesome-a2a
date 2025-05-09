#!/bin/bash

set -x

source development_tutor/.env

name_vars(){
    export AGENT_PATH="./dev_assist"
    export SERVICE_NAME="dev-assist"
    export APP_NAME="dev-assist-app"
}

deploy_service(){
    adk deploy cloud_run \
    --project=$GOOGLE_CLOUD_PROJECT \
    --region=$GOOGLE_CLOUD_LOCATION \
    --service_name=$SERVICE_NAME \
    --app_name=$APP_NAME \
    --with_ui \
    $AGENT_PATH
}

main(){
    name_vars
    deploy_service
}

main

exit 0