# Microservices on Kubernetes

Two small FastAPI services that talk to each other, containerized with Docker and deployed on a local Kubernetes cluster (minikube).

## Architecture

```
Browser / curl
      |  :30080
      v
[ Service: frontend-service (NodePort) ]
      v
[ Pod: frontend ]  --calls http://api-service:8001-->  [ Service: api-service (ClusterIP) ]
                                                                  v
                                                          [ Pod(s): api ]
```

- **frontend-service**: public entry point, fetches data from the api over HTTP
- **api-service**: private backend, only reachable inside the cluster

## Tech stack

Python (FastAPI) | Docker | Kubernetes (minikube) | kubectl

## Project structure

```
microservices/
  api-service/        FastAPI api + Dockerfile
  frontend-service/   FastAPI frontend + Dockerfile
  k8s/                Deployment and Service manifests
```

## Run it

Requires Docker, minikube and kubectl.

```bash
minikube start --driver=docker

docker build -t api-service:v1 ./api-service
docker build -t frontend-service:v1 ./frontend-service
minikube image load api-service:v1
minikube image load frontend-service:v1

kubectl apply -f k8s/
minikube service frontend-service --url
```

Then open the printed URL and add `/users`:

```json
{"from":"frontend-service","users":[{"id":1,"name":"Brian"},{"id":2,"name":"Wanjiku"},{"id":3,"name":"Otieno"}]}
```

## What this project demonstrates

- Containerizing services with Dockerfiles
- Service-to-service communication using Kubernetes Services and cluster DNS
- ClusterIP (internal) vs NodePort (external) exposure
- Scaling: `kubectl scale deployment api-service --replicas=3`
- Self-healing: delete a pod and Kubernetes recreates it
- Rolling updates and rollbacks with zero downtime

## Next steps

- Add a database service
- Add health checks (liveness and readiness probes)
- Add a CI pipeline that builds the images on every push
