# Introduction
Here the yaml configuration of deployment and the services of the python applications are present.
A minimal deployment script (script.sh) is used to deploy the services.

## Pre-requisites
minikube and kubectl needs to be already existing in your machine.
A minikube cluster must be existing before the deployment script (script.sh) must be run.
I used virtualbox as vmdriver.

```shell
minikube start --vm-driver=virtualbox
```

## Deployment script
Once the minikube cluster is existing. Simply run script.sh in the same folder as signavio.yaml file.
It will create the deployments and services and after 30seconds also opens the browser to access both services.

The services can be accessed by:

```shell
minikube service hello-svc
minikube service reverse-svc
```

## Troubleshooting
1. Always check the raw data for reverse-svc in the browser
