# ☸️ Kubernetes AI Log Monitor

![Status](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Kubernetes](https://img.shields.io/badge/K8s-Native-326ce5?logo=kubernetes)
![Docker](https://img.shields.io/badge/Docker-Container-2496ed?logo=docker)

A lightweight, **event-driven observability agent** that runs directly inside a Kubernetes cluster. It connects to the K8s API server to watch the Event Stream in real-time and uses heuristic logic to detect and categorize pod failures (like `CrashLoopBackOff` or `OOMKilled`) before they impact the user experience.

## 🧐 Why I Built This
Traditional monitoring tools often scrape logs every few minutes, which creates a delay between a crash and an alert. I wanted to build an **event-driven** system that:
1.  Reacts instantly (push-based vs. poll-based).
2.  Runs natively inside the cluster using `ServiceAccount` authentication.
3.  Filters out the noise and only flags actual "Critical" or "Warning" events.

## 🛠️ Architecture

The agent runs as a Deployment in the `default` namespace. It authenticates using a custom RBAC role that grants read-only access to the Event API.

```mermaid
graph TD
    API[Kubernetes API Server] -- Watch Stream --> Agent[AI Monitor Agent]
    subgraph "K8s Cluster"
        Agent -- Heuristic Analysis --> Logs[Structured Logs]
        Logs --> Loki[Loki / Fluentd]
    end
    style Agent fill:#f9f,stroke:#333,stroke-width:2px

    📖 Documentation:
    Prerequisites
    Deployment Guide
    Future Roadmap
