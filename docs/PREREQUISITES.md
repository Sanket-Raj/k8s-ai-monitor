# 📋 Prerequisites

Before deploying the K8s AI Monitor, ensure your environment meets the following requirements.

## 1. Kubernetes Cluster
You need a running Kubernetes cluster (version 1.24+ recommended).
* **Local Development:** [Minikube](https://minikube.sigs.k8s.io/docs/), [Kind](https://kind.sigs.k8s.io/), or Docker Desktop (Kubernetes enabled).
* **Cloud:** EKS (AWS), GKE (Google Cloud), or AKS (Azure).

## 2. CLI Tools
Ensure the following tools are installed and available in your system path:
* **kubectl:** The Kubernetes command-line tool. [Installation Guide](https://kubernetes.io/docs/tasks/tools/).
  * Verification: Run `kubectl version --client`
* **Docker:** Required if you plan to rebuild the agent image locally.
  * Verification: Run `docker --version`

## 3. Container Registry Access (Optional)
If you modify the source code (`Agent/analyzer.py`), you will need an account on Docker Hub or GitHub Container Registry (GHCR) to push your custom images.
* You must update the `image:` field in `k8-manifests/deployment.yml` to match your repository.

## 4. RBAC Permissions
The user deploying this application must have administrative privileges on the cluster to create `ClusterRoles` and `ServiceAccounts`.
