# Verification Progress

This file tracks the provider-verification queue. It is not a recommendation list.

## Counts

- Discovery seed entries: maintained in `data/provider-candidates.seed.yaml`
- Official-source verification batches completed: 1
- Providers in verified batch 001: 9
- Benchmark-validated providers: 0

## Batch 001

Official-source checks completed for:

- HostHatch
- Contabo
- Hetzner
- netcup
- UpCloud
- Vultr
- OVHcloud
- Gcore
- Civo

See `results/verified/batch-001.yaml`.

## Important incomplete fields

The first batch intentionally exposes unknowns rather than filling them from assumptions. Examples include:

- exact regional public port limits for some bargain VPS products;
- virtualization technology where the current official product page did not explicitly state it;
- exact private-network fees when documentation describes the feature but not a price;
- public IPv4 add-on cost where it is billed separately;
- whether a snapshot feature satisfies a profile's separate backup requirement;
- current regional worker price when a managed-Kubernetes documentation page verifies features but not pricing;
- Terraform/OpenTofu support when API support alone was verified.

## Next official-verification queue

Priority is based on broad resource coverage or potentially strong price/performance, not recommendation status.

### Batch 002 — low-cost and regional compute

- Onidel
- GreenCloud / GreenCloudVPS identity review
- OrangeVPS
- VSYS Host
- CloudBlast
- Hostinger
- Melbicom
- ExtraVM
- WebHorizon
- FlowVPS
- ServaRica
- HostEons

### Batch 003 — API-driven and managed cloud

- DigitalOcean
- Akamai Cloud / Linode
- Kamatera
- Scaleway
- IONOS
- Exoscale
- CloudSigma
- Cherry Servers
- Serverspace
- Alibaba Cloud
- Tencent Cloud
- Huawei Cloud

### Batch 004 — regional cloud candidates

- Nevacloud
- vHost
- OneAsiaHost
- VPSnet
- Virtuaal.com
- BulutVDS
- Netlen
- Cloudify.ro
- NAV.RO
- ITMCloud
- NovaCloud Africa
- IPXON

## After official verification

Candidates that survive hard filters should move to a benchmark phase. Benchmark data must be stored separately from advertised specifications and should include test date, region, instance plan, OS, kernel, tool version, and full command parameters.

Recommended benchmark categories:

- sustained CPU and steal-time behavior;
- random and sequential storage latency/IOPS;
- fsync-sensitive database behavior;
- network RTT, packet loss, and sustained throughput;
- API provisioning and deletion latency for elastic-cloud candidates;
- node-pool scale-up/down behavior for managed Kubernetes.
