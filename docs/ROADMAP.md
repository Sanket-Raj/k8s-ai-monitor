This project is currently in **Beta (v0.1)**. The following features are planned for upcoming releases to enhance observability and intelligence.

## Q1 2026: Intelligence Upgrades
- [ ] **LLM Integration:** Replace the current keyword-based heuristic with a lightweight local LLM (e.g., DistilBERT) to analyze error context.
- [ ] **Root Cause Prediction:** Implement a correlation engine that groups related events (e.g., `OOMKilled` on Pod A + `Connection Refused` on Pod B).

## Q2 2026: Observability Integrations
- [ ] **Prometheus Exporter:** Expose an HTTP `/metrics` endpoint to scrape event severity counts (e.g., `k8s_ai_critical_events_total`).
- [ ] **Grafana Dashboard:** Publish a JSON dashboard template to visualize cluster health based on AI scores.
- [ ] **Slack/Teams Alerts:** Add a webhook integration to post "CRITICAL" severity findings directly to a chat channel.

## Q3 2026: Architecture & Scale
- [ ] **Helm Chart:** Package the manifests into a Helm chart for easier multi-environment deployment.
- [ ] **Leader Election:** Enable running multiple replicas of the agent for high availability without duplicating event logs.
