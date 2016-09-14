#! /bin/bash

#
# Original:
# http://dev.mikamai.com/post/144501132499/continuous-delivery-with-travis-and-ecs
# 
# Modified to:
#   Use Docker Hub instead of AWS ECR
#   Add better error handling

# Push only if it's not a pull request
if [ -z "$TRAVIS_PULL_REQUEST" ] || [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
  # Push only if we're testing the master branch
  if [ "$TRAVIS_BRANCH" == "master" ]; then
  
    # This is needed to login on AWS and push the image on ECR
    # Change it accordingly to your docker repo
#    pip install --user awscli
    export PATH=$PATH:$HOME/.local/bin
#    eval $(aws ecr get-login --region $AWS_DEFAULT_REGION)
    docker login -u $DOCKER_HUB_USER -p $DOCKER_HUB_PASS
    
    # Build and push
    echo "Building $IMAGE_NAME"
    docker build -t $IMAGE_NAME .
    retval=$?
    if [ $retval -ne 0 ]; then
      echo "Build failed"
    else
      echo "Build succeeded"
    fi

    echo "Pushing $IMAGE_NAME:latest"
    docker tag $IMAGE_NAME:latest "$REPOSITORY/$IMAGE_NAME:latest" && \
    docker push "$REPOSITORY/$IMAGE_NAME:latest"
    retval=$?
    if [ $retval -ne 0 ]; then
      echo "Tag/push failed"
    else
      echo "Pushed $IMAGE_NAME:latest"
    fi
    
  else
    echo "Skipping deploy because branch is not 'master'"
  fi
else
  echo "Skipping deploy because it's a pull request"
fi