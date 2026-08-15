# Verification Progress

This file tracks the provider-verification queue. It is not a recommendation list.

## Counts

- Discovery seed entries: maintained in `data/provider-candidates.seed.yaml`
- Official-source verification batches completed: 8
- Providers in verified batch 001: 9
- Providers in verified batch 002: 7
- Providers in verified batch 003: 12
- Providers in verified batch 004: 7
- Providers in verified batch 005: 11
- Providers in verified batch 006: 10
- Providers in verified batch 007: 10
- Providers in verified batch 008: 11
- Total unique provider records in official-source verification batches: 77
- Targeted follow-up files: 1
- Benchmark-validated providers: 0

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

Verified source files are stored as `results/verified/batch-001.yaml` through `results/verified/batch-008.yaml`.

## Targeted follow-ups

`results/verified/followup-001.yaml` deepens existing records without incrementing the unique-provider count:

- Onidel: core HA/private-network/API/backup features reconfirmed, but the current pricing widget still fails to expose a stable 16 GB plan/price.
- KVMVPS.co.za: dedicated CPU/KVM/NVMe/snapshot/backup facts reconfirmed; exact 16 GB custom price, private network, port speed, and explicit current SLA remain unresolved.
- Cherry Servers: a Tokyo 16 GB dedicated-resource VDS is now pinned to an exact current plan and price; it fails the current database budget.
- IONOS: Memory Cube S/M pricing is reconfirmed; transfer allowance, public port speed, and the reusable profile's KVM requirement remain unresolved.

## Strict derived filtering

Derived files currently include:

- `results/derived/standard-compute-strict.yaml`
- `results/derived/database-node-strict.yaml`
- `results/derived/managed-kubernetes-strict.yaml`

### Standard compute

Current clear advertised-specification pass:

- ServaRica KVM Slim Slice 2.

Several low-cost near-matches remain blocked by explicit unknowns rather than being silently promoted to pass.

### Database node

Current `clear_pass` is empty. Strong near-matches include VSYS Host, VPSnet, ServaRica, Onidel, BulutVDS, netcup, BDIX Web Host, BengalCloud, and ITMCloud, each blocked by one or more hard requirements such as private networking, backup semantics, SLA, KVM, exact current price, port speed, or normalized TCO.

### Managed Kubernetes

Current `clear_pass` is empty because no verified record yet covers every hard field together. UpCloud, Scaleway, Exoscale, DigitalOcean, Vultr, GKE, and AKS are among the shortest-path follow-up candidates.

## Notable classification findings

- A bargain headline price is frequently invalidated by a hard network, storage, contract, or virtualization requirement.
- ServaRica remains the strongest strict standard-compute advertised-specification match and should advance to benchmark validation.
- VPSMalaysia demonstrates why transfer allowance alone is insufficient: the 8 GB KVM tier has ample NVMe and transfer but only a 100 Mbps shared port.
- Randhost is a genuine KVM/API/hourly cloud, but its current 8 GB tier is not a bargain-VPS-priced resource.
- AkileCloud is optimized around network paths and high-bandwidth regional products; observed 8 GB products miss the reusable local-storage and/or port hard floors.
- SpeedyPage, Shock Hosting, Virtono, Evoxt, and LiteServer offer credible VPS products but their verified 8 GB monthly tiers exceed the current 15 USD bargain-compute ceiling.
- IPXON provides broad Latin American KVM coverage and advanced networking, but its current price widget is not reliably machine-readable and API status is inconsistent across official pages.
- Annualized, promotional, and renewal pricing remain separate data fields and are never silently treated as ordinary monthly prices.
- Marketing geography is stored separately from actual datacenter geography when the provider exposes a mismatch.

## Important incomplete fields

Common unresolved fields include:

- exact public port limits;
- virtualization type for a specific product line;
- private-network availability or pricing;
- CPU allocation class when a provider only says `vCPU`;
- public IPv4 add-on price;
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

### Batch 009 — additional strong-price discovery leads

- HostBrr
- Advin
- HostSlick
- UltaHost
- additional SmartHost exact configurations if checkout exposes stable prices
- additional regional providers discovered from IX/provider indexes

### Batch 010 — Asia-focused discovery

- Taiwan local KVM/cloud providers
- Vietnam additional KVM/cloud providers
- Indonesia local public-cloud providers
- Malaysia additional providers
- Philippines local providers
- India/Pakistan/Bangladesh additional providers not already counted

### Follow-up 002 — hard-filter unknown reduction

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
