#/bin/bash

kubectl apply -f signavio.yaml

sleep 30s
minikube service hello-svc
minikube service reverse-svc
