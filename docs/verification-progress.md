# Verification Progress

This file tracks the provider-verification queue. It is not a recommendation list.

## Counts

- Discovery seed entries: maintained in `data/provider-candidates.seed.yaml`
- Official-source verification batches completed: 10
- Providers in verified batch 001: 9
- Providers in verified batch 002: 7
- Providers in verified batch 003: 12
- Providers in verified batch 004: 7
- Providers in verified batch 005: 11
- Providers in verified batch 006: 10
- Providers in verified batch 007: 10
- Providers in verified batch 008: 11
- Providers in verified batch 009: 4
- Providers in verified batch 010: 11
- Total unique provider records in official-source verification batches: 92
- Targeted follow-up files: 1
- Benchmark-ready resources: 1
- Benchmark-measured resources: 0

## Completed batches

### Batch 001 — initial compute / managed-cloud baseline
HostHatch, Contabo, Hetzner, netcup, UpCloud, Vultr, OVHcloud, Gcore, Civo.

### Batch 002 — low-cost and regional compute
Onidel, GreenCloud, Hostinger, Melbicom, ExtraVM, VSYS Host, CloudBlast.

### Batch 003 — performance and bargain VPS/VDS
OrangeVPS, WebHorizon, FlowVPS, ServaRica, HostEons, RackNerd, DediRock, Alwyzon, Time4VPS, Webdock, LunaNode, FiberState.

### Batch 004 — API-driven / managed cloud
DigitalOcean, Akamai Cloud / Linode, Kamatera, Scaleway, Exoscale, Cherry Servers, IONOS.

### Batch 005 — regional public cloud
Nevacloud, vHost, OneAsiaHost, VPSnet, Virtuaal.com, BulutVDS, Netlen, ITMCloud, NovaCloud Africa, Cloudify.ro, NAV.RO.

### Batch 006 — low-cost regional discovery leads
SferaHost, DedicatServer.ro, Astra Telekom, KVMVPS.co.za, GamCo, Mocky, BDIX Web Host, BengalCloud, Shinjiru, Server Galactic.

### Batch 007 — global/API cloud
CloudSigma, Serverspace, Alibaba Cloud, Tencent Cloud, Huawei Cloud, Oracle Cloud Infrastructure, IBM Cloud, AWS Lightsail, Google Cloud, Microsoft Azure.

### Batch 008 — regional and strong-price candidates
IPXON, VPSMalaysia, Randhost, AkileCloud, SpeedyPage, Shock Hosting, SmartHost, Virtono, Evoxt, LiteServer, Aluy.

### Batch 009 — newly discovered strong-price/configurable providers
Advin Servers, HostBrr, HostSlick, UltaHost.

### Batch 010 — Asia-focused local/regional providers
FormoHost, FussionHost, ServerUtama, Herza Cloud, GOFIBER, Kencang, CloudXact, Rumahweb, H2Cloud, Onie Cloud, ModernOne / Nocser.

Verified source files are stored as `results/verified/batch-001.yaml` through `results/verified/batch-010.yaml`.

## Targeted follow-ups

`results/verified/followup-001.yaml` deepens existing records without incrementing the unique-provider count:

- Onidel: core HA/private-network/API/backup features reconfirmed, but the current pricing widget still fails to expose a stable 16 GB plan/price.
- KVMVPS.co.za: dedicated CPU/KVM/NVMe/snapshot/backup facts reconfirmed; exact 16 GB custom price, private network, port speed, and explicit current SLA remain unresolved.
- Cherry Servers: a Tokyo 16 GB dedicated-resource VDS is pinned to an exact current plan and price; it fails the current database budget.
- IONOS: Memory Cube S/M pricing is reconfirmed; transfer allowance, public port speed, and the reusable profile's KVM requirement remain unresolved.

## Strict derived filtering

Derived files currently include:

- `results/derived/standard-compute-strict.yaml`
- `results/derived/database-node-strict.yaml`
- `results/derived/managed-kubernetes-strict.yaml`

### Standard compute

Current clear advertised-specification pass:

- ServaRica KVM Slim Slice 2.

High-priority blocked candidates include:

- Onie Cloud VM 4-8: 4 vCPU, 8 GB, 150 GB NVMe, 7 TB, 10 Gbps, IPv4/IPv6, VPC, API/CLI/Python SDK, hourly billing, autoscaling, load balancing, snapshots, and automated backup; blocked by KVM verification, normalized TCO, and promotional-price persistence.
- Advin Servers Miami Standard XS: current advertised 6 USD promotion / 8 USD reference, 4 shared-burstable vCPU, 8 GB, 80 GB NVMe, 5 TB, 10 Gbps, KVM; blocked by explicit IPv4 verification and promotional-price persistence.
- HostBrr EPYC 8 GB: strong EPYC 9004 / DDR5 ECC / NVMe / 10 Gbps resources; blocked by stable current price and exact product virtualization verification.
- CloudXact, Kencang, ServerUtama, Rumahweb, OrangeVPS, HostEons, BulutVDS, HostHatch, Contabo, Hetzner, IONOS, SferaHost, Netlen, ITMCloud, SmartHost, and IPXON remain blocked by one or more explicit unknown hard fields.

A provider-advertised hard-filter pass is not a final recommendation. It advances the resource to benchmark and operational verification.

### Database node

Current `clear_pass` is empty.

Strong near-matches include Advin Servers, HostBrr, VSYS Host, VPSnet, ServaRica, Onidel, BulutVDS, netcup, BDIX Web Host, BengalCloud, Hostinger, and ITMCloud. Each is blocked by one or more hard requirements such as private networking, reliable backups, snapshot semantics, SLA, KVM, exact current price, port speed, IPv4, or normalized TCO.

Advin's current backup documentation describes the backup system as experimental/best-effort, so it is not treated as satisfying the strict database backup requirement.

### Managed Kubernetes

Current `clear_pass` is empty because no verified record yet covers every hard field together. UpCloud, Scaleway, Exoscale, DigitalOcean, Vultr, GKE, and AKS are among the shortest-path follow-up candidates.

## Benchmark readiness

`results/benchmark/queue.yaml` separates resources that are ready for measured validation from candidates that are still blocked by source-verification gaps.

Current benchmark-ready resource:

- ServaRica KVM Slim Slice 2 for the standard-compute profile.

High-priority blocked benchmark candidates now also include Onie Cloud, Advin Servers, and HostBrr for standard compute.

No benchmark has been executed or claimed yet. The queue defines reproducible CPU, storage, database, network, and stability checks and requires exact region/plan/OS/kernel/tool metadata for future measurements.

## Notable classification findings

- A bargain headline price is frequently invalidated by a hard network, storage, contract, virtualization, IPv4, transfer, or availability requirement.
- ServaRica remains the strongest strict standard-compute advertised-specification match and is benchmark-ready.
- Onie Cloud is one of the strongest newly verified Asia-local API-driven compute leads, but strict filtering correctly withholds pass status until virtualization and TCO/price persistence are resolved.
- Advin Servers is a particularly strong global price/specification lead, but strict filtering correctly withholds pass status until IPv4 inclusion and price persistence are verified.
- HostBrr exposes compelling EPYC 9004 memory-optimized shapes, but the current checkout did not expose stable numeric prices during verification.
- FormoHost Taiwan, FussionHost Manila, GOFIBER Vietnam, and ModernOne Malaysia demonstrate how local presence can still fail generic requirements due RAM, transfer, price, or port-speed hard limits.
- Herza Cloud Manila provides KVM and a shared 10 Gbps port, but its 8 GB plan exceeds the current bargain-compute budget.
- H2Cloud exposes inexpensive 10 Gbps/KVM/NVMe Vietnam plans, but the verified 8 GB high-speed tier includes only 1 TB/month and was out of stock.
- ServerUtama, CloudXact, Kencang, and Rumahweb remain useful near-matches because only a small number of hard fields are unresolved.
- Annualized, promotional, and renewal pricing remain separate data fields and are never silently treated as ordinary monthly prices.
- Marketing geography is stored separately from actual datacenter geography when the provider exposes a mismatch or ambiguity.

## Important incomplete fields

Common unresolved fields include:

- exact public port limits;
- virtualization type for a specific product line;
- private-network availability or pricing;
- CPU allocation class when a provider only says `vCPU`;
- public IPv4 inclusion or add-on price;
- snapshot versus independent backup semantics;
- regional worker-node pricing for managed Kubernetes;
- Terraform/OpenTofu support when only a REST API is documented;
- dynamic price tables that cannot be captured;
- promotional versus renewal pricing and minimum contract term;
- local-currency conversion policy;
- stock / location availability;
- marketing location versus actual datacenter;
- fair-use definitions for `unlimited` or `unmetered` traffic.

## Next official-verification queue

### Batch 011 — more Asia/local discovery

- additional Taiwan local cloud/VPS providers
- Vietnam providers with 8 GB and 1+ Gbps signals
- Indonesia providers with KVM, IPv4, and explicit port speeds
- Philippines local providers not already counted
- India/Pakistan/Bangladesh providers not already counted
- South Korea/Hong Kong regional providers outside the major cloud set

### Batch 012 — Europe and global low-cost discovery

- remaining VPS index candidates with 8 GB or configurable-memory signals
- regional Root Server / VDS providers not yet normalized into the verified set
- API/hourly providers absent from major cloud comparisons

### Follow-up 002 — hard-filter unknown reduction

- Onie Cloud KVM virtualization, ordinary monthly price/TCO, and promotion persistence
- CloudXact exact public port speed and setup-fee-inclusive TCO
- Kencang IPv4 and port-floor semantics
- ServerUtama public port and datacenter geography
- Rumahweb public port and IPv4
- Advin Servers IPv4 inclusion and non-promotional monthly price behavior
- HostBrr stable 8/16 GB pricing and exact product virtualization
- VSYS Host private-network verification
- VPSnet private-network verification
- ServaRica database-node network/backup/SLA verification
- Onidel current 16 GB availability/price capture
- UpCloud managed-Kubernetes monitoring and worker-shape verification
- Scaleway managed-Kubernetes load-balancer/monitoring/worker-shape verification
- Exoscale managed-Kubernetes load-balancer/monitoring/worker-shape verification
- DigitalOcean Terraform/monitoring/exact worker TCO verification

## Derived comparison work

Derived files should be used for:

- clear hard-filter passes;
- near matches blocked by unknown fields;
- hard rejects and rejection reasons;
- managed-Kubernetes candidates;
- database-node candidates;
- benchmark queue.

Derived results point back to verified source batches and do not overwrite observed facts.

## Benchmark phase

Candidates that survive hard filters should move to benchmark validation. Store benchmark evidence separately with test date, region, exact plan, OS/kernel, tool version, and full command parameters.

Recommended benchmark categories:

- sustained CPU and steal-time behavior;
- random and sequential storage latency/IOPS;
- fsync-sensitive database behavior;
- network RTT, packet loss, and sustained throughput;
- API provisioning and deletion latency for elastic-cloud candidates;
- node-pool scale-up/down behavior for managed Kubernetes.
