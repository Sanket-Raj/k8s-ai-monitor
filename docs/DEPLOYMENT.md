# 🚀 Deployment Guide

Follow these steps to deploy the AI Monitor Agent to your cluster.

## Phase 1: Authentication Setup (RBAC)
The agent requires specific permissions to "watch" the Kubernetes Event Stream. We use a dedicated `ServiceAccount` for this.

1. **Create the Service Account and ClusterRole:**
   ```bash
   kubectl apply -f k8-manifests/rbac.yml
