# Verification Progress

This file tracks the provider-verification queue. It is not a recommendation list.

## Counts

- Discovery seed entries: maintained in `data/provider-candidates.seed.yaml`
- Official-source verification batches completed: 3
- Providers in verified batch 001: 9
- Providers in verified batch 002: 7
- Providers in verified batch 003: 12
- Total provider records with an official-source verification batch: 28
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

## Batch 002

Official-source checks completed for:

- Onidel
- GreenCloud
- Hostinger
- Melbicom
- ExtraVM
- VSYS Host
- CloudBlast

See `results/verified/batch-002.yaml`.

## Batch 003

Official-source checks completed for:

- OrangeVPS
- WebHorizon
- FlowVPS
- ServaRica
- HostEons
- RackNerd
- DediRock
- Alwyzon
- Time4VPS
- Webdock
- LunaNode
- FiberState

See `results/verified/batch-003.yaml`.

Notable classification findings from this batch:

- ServaRica and HostEons expose unusually inexpensive dedicated-resource plans and should be benchmarked rather than judged only by advertised vCPU count.
- RackNerd specials are annual-prepay products; annualized monthly cost must not be treated as a normal month-to-month price.
- Time4VPS publishes materially different promotional and renewal prices across 1-, 12-, and 24-month terms.
- Webdock exposes configurable profiles through its API, so a fixed-plan table alone is insufficient for requirement matching.
- LunaNode is an API-driven hourly cloud with private networking and automation primitives, but its 8/16 GB tiers are not bargain-VPS priced.
- FiberState is currently verified as bare metal rather than a public VPS offer; it remains useful as an architecture alternative but must not be counted as a matching VPS provider.

## Important incomplete fields

Verification intentionally exposes unknowns rather than filling them from assumptions. Examples include:

- exact regional public port limits for some bargain VPS products;
- virtualization technology where the current official product page did not explicitly state it;
- exact private-network fees when documentation describes the feature but not a price;
- public IPv4 add-on cost where it is billed separately;
- whether a snapshot feature satisfies a profile's separate backup requirement;
- current regional worker price when managed-Kubernetes documentation verifies features but not pricing;
- Terraform/OpenTofu support when API support alone was verified;
- provider pages whose dynamic pricing table could not be captured;
- region pages with inconsistent availability labels;
- promotional or annualized prices whose contract term differs from a reusable profile's default assumptions;
- whether a provider's advertised CPU allocation is dedicated, fair-share, burstable, or merely unspecified.

## Next official-verification queue

Priority is based on broad resource coverage or potentially strong price/performance, not recommendation status.

### Batch 004 — API-driven and managed cloud

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

### Batch 005 — regional cloud candidates

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

### Batch 006 — remaining discovery leads with strong price or automation signals

- SferaHost
- DedicatServer.ro
- Astra Telekom
- KVMVPS.co.za
- GamCo
- Mocky
- BDIX Web Host
- BengalCloud
- VPSMalaysia
- Shinjiru
- Server Galactic
- Randhost

## After official verification

Candidates that survive hard filters should move to a benchmark phase. Benchmark data must be stored separately from advertised specifications and should include test date, region, instance plan, OS, kernel, tool version, and full command parameters.

Recommended benchmark categories:

- sustained CPU and steal-time behavior;
- random and sequential storage latency/IOPS;
- fsync-sensitive database behavior;
- network RTT, packet loss, and sustained throughput;
- API provisioning and deletion latency for elastic-cloud candidates;
- node-pool scale-up/down behavior for managed Kubernetes.
