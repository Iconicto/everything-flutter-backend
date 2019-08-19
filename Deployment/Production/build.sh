docker build -f Deployment/Production/Dockerfile -t $IMAGE_NAME:latest .
docker tag $IMAGE_NAME $IMAGE_NAME:commit-$TRAVIS_COMMIT
docker tag $IMAGE_NAME $IMAGE_NAME:production