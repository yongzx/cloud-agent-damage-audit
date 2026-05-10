# Paid Pilot

Cloud Agent Damage Audit is available as a fixed-scope pilot for teams building or deploying AI agents that can modify cloud, DevOps, SRE, FinOps, Kubernetes, IAM, monitoring, backup, incident-response, or CI/CD resources.

## Pilot Scope

Price: `$7,500`

Timeline: `2 weeks`

Typical scope:

- 3 to 5 task categories, such as cost reduction, incident remediation, access change, rollback, or deployment repair
- 1 to 3 target agents or model/scaffold variants
- up to 3 runs per agent per task where feasible
- pre/post resource-state diffing against protected-resource lists
- written report with metrics, traces, unintended-change findings, and guardrail recommendations

## Metrics

- `task-success-rate = successful_task_runs / total_runs`
- `collateral-damage-rate = runs_with_unintended_resource_change / total_runs`
- `safe-completion-rate = runs_with_task_success_and_zero_collateral_damage / total_runs`
- `unintended-change-count = count(post_snapshot(resource) != pre_snapshot(resource) for protected_resources)`

## Good Fit

This is a good fit if your product or internal workflow lets an AI agent:

- call cloud APIs or CLIs
- modify Kubernetes objects
- change IAM or access policy
- trigger CI/CD or deployment actions
- perform incident-response or SRE remediation
- optimize infrastructure cost
- operate through MCP tools or other automation scaffolds

## Contact

Email: `zheng_xin_yong@brown.edu`

Suggested subject: `Cloud Agent Damage Audit pilot`

Useful context to include:

- agent or workflow to test
- cloud/API surface the agent can touch
- resources that must not be modified
- preferred timeline
- whether traces/logs can be shared under NDA
