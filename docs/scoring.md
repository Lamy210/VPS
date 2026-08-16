# Scoring and TCO

Hard requirements are evaluated before scores. A resource that fails a hard requirement is rejected even if its weighted score would otherwise be high.

## 1. Hard filters

Examples:

- minimum RAM / CPU
- required region or maximum latency
- minimum local storage
- required virtualization type
- required private networking
- required API / cloud-init / Terraform support
- budget ceiling
- required resource type

Result: `pass`, `fail`, or `unknown`.

`unknown` must not be silently treated as `pass`.

## 2. Effective monthly TCO

Do not rank only by headline VM price.

```text
monthly_tco =
  base_compute
  + mandatory_public_ipv4
  + private_network_fee
  + required_block_storage
  + required_backup
  + snapshot_storage
  + load_balancer
  + nat_gateway
  + managed_control_plane
  + expected_egress_overage
  + recurring_support_required_by_profile
```

Also record:

- setup fee
- minimum contract term
- prepayment term
- promotional price
- renewal price
- taxes when determinable

## 3. Normalized cost metrics

Useful secondary metrics:

- `monthly_tco / RAM_GB`
- `monthly_tco / vCPU`
- `monthly_tco / dedicated_core`
- `monthly_tco / local_storage_GB`
- `monthly_tco / included_transfer_TB`

These are diagnostics, not standalone rankings.

## 4. Weighted score

Default categories:

- cost
- compute performance
- storage performance
- network
- reliability
- automation
- scalability
- support / operational maturity

Each category receives a 0-10 score, multiplied by the requirement profile's weight.

```text
weighted_score = sum(category_score * category_weight) / sum(category_weight)
```

## 5. Confidence penalty

A cheap but poorly verified resource should not outrank a fully verified resource without warning.

Suggested confidence levels:

- A+: official specification + official cost + network/automation verification + independent or controlled benchmark
- A: official specification + official cost + material operational features verified
- B: official price/spec verified, some operational details unknown
- C: official provider found, current resource details incomplete
- D: discovery lead only

Apply a visible confidence label rather than hiding uncertainty inside the numeric score.

## 6. Performance evidence

Prefer workload-relevant evidence:

- CPU: sustained benchmark and steal-time behavior
- database: fsync latency, random read/write latency, database benchmark
- storage: fio with documented block sizes and queue depths
- network: RTT, packet loss, sustained transfer, region-to-region tests
- Kubernetes: provisioning time, API rate limits, node creation/deletion time

Synthetic scores alone are insufficient for a final selection.

## 7. Separate resource classes

Do not put fundamentally different products into one price-only table.

Recommended classes:

- bargain VPS
- performance / dedicated-resource VDS
- regional public cloud
- elastic API-driven cloud
- managed Kubernetes
- bare metal
- managed database
- managed cache
- object storage
- serverless / container runtime

Compare within a class first, then compare complete architecture TCO across classes.
