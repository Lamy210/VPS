# Verification Progress

This file tracks the provider-verification queue. It is not a recommendation list.

## Counts

- Discovery seed entries: maintained in `data/provider-candidates.seed.yaml`
- Official-source verification batches completed: 6
- Providers in verified batch 001: 9
- Providers in verified batch 002: 7
- Providers in verified batch 003: 12
- Providers in verified batch 004: 7
- Providers in verified batch 005: 11
- Providers in verified batch 006: 10
- Total provider records with an official-source verification batch: 56
- Benchmark-validated providers: 0

## Completed batches

### Batch 001 — initial compute / managed-cloud baseline

HostHatch, Contabo, Hetzner, netcup, UpCloud, Vultr, OVHcloud, Gcore, Civo.

See `results/verified/batch-001.yaml`.

### Batch 002 — low-cost and regional compute

Onidel, GreenCloud, Hostinger, Melbicom, ExtraVM, VSYS Host, CloudBlast.

See `results/verified/batch-002.yaml`.

### Batch 003 — performance and bargain VPS/VDS

OrangeVPS, WebHorizon, FlowVPS, ServaRica, HostEons, RackNerd, DediRock, Alwyzon, Time4VPS, Webdock, LunaNode, FiberState.

See `results/verified/batch-003.yaml`.

### Batch 004 — API-driven / managed cloud

DigitalOcean, Akamai Cloud / Linode, Kamatera, Scaleway, Exoscale, Cherry Servers, IONOS.

See `results/verified/batch-004.yaml`.

### Batch 005 — regional public cloud

Nevacloud, vHost, OneAsiaHost, VPSnet, Virtuaal.com, BulutVDS, Netlen, ITMCloud, NovaCloud Africa, Cloudify.ro, NAV.RO.

See `results/verified/batch-005.yaml`.

### Batch 006 — low-cost regional discovery leads

SferaHost, DedicatServer.ro, Astra Telekom, KVMVPS.co.za, GamCo, Mocky, BDIX Web Host, BengalCloud, Shinjiru, Server Galactic.

See `results/verified/batch-006.yaml`.

## Notable classification findings

- ServaRica and HostEons expose unusually inexpensive dedicated-resource plans and should move to benchmark validation rather than being judged only by advertised vCPU count.
- BulutVDS currently has a fully verified plan that passes the reusable `standard-compute` headline hard filters.
- OrangeVPS also has a clear standard-compute match in its 8 GB NVMe tier.
- RackNerd specials are annual-prepay products; annualized monthly cost must not be treated as a normal month-to-month price.
- Time4VPS publishes materially different promotional and renewal prices across 1-, 12-, and 24-month terms.
- Mocky markets the VPS product in Kenya, but its official product page explicitly places the verified servers in an EU datacenter. Marketing geography is therefore stored separately from actual datacenter geography.
- NAV.RO MultiCloud products are resource pools; aggregate pool RAM cannot be treated as per-VM RAM when applying hard filters.
- Shinjiru and DedicatServer.ro have attractive memory/storage pricing but fail the reusable 1 Gbps hard network floor on the verified tiers.
- DigitalOcean, Scaleway, Exoscale, and other managed-cloud products are intentionally evaluated as automation/managed-Kubernetes classes rather than compared only on RAM price.
- FiberState is currently verified as bare metal rather than a public VPS offer; it remains an architecture alternative but must not be counted as a matching VPS provider.

## Important incomplete fields

Verification intentionally exposes unknowns rather than filling them from assumptions. Common unresolved fields include:

- exact public port limits;
- private-network availability or pricing;
- CPU allocation class when a provider only says `vCPU`;
- public IPv4 add-on price;
- snapshot versus independent backup semantics;
- regional worker-node pricing for managed Kubernetes;
- Terraform/OpenTofu support when only a REST API is documented;
- dynamic price tables that could not be captured;
- promotional versus renewal pricing and minimum contract term;
- local-currency conversion policy;
- stock / location availability;
- whether a marketing location matches the actual datacenter;
- fair-use definitions for `unlimited` or `unmetered` traffic.

## Next official-verification queue

### Batch 007 — remaining global/API cloud

- CloudSigma
- Serverspace
- Alibaba Cloud
- Tencent Cloud
- Huawei Cloud
- Oracle Cloud
- IBM Cloud
- AWS Lightsail
- Google Compute Engine
- Azure Virtual Machines

### Batch 008 — remaining regional / automation candidates

- IPXON
- VPSMalaysia
- Randhost
- SferaHost deeper networking/API review
- KVMVPS.co.za custom 16 GB pricing
- Onidel current plan-price capture
- Cherry Servers 8/16 GB VDS plan pricing
- IONOS Cloud Cubes transfer / port terms

### Batch 009 — additional strong-price discovery leads

- HostBrr
- Advin
- Akile
- SpeedyPage
- ShockHosting
- SmartHost
- Virtono
- Ultahost
- Aluy
- LiteServer
- HostSlick
- Evoxt

## Derived comparison work

After enough provider batches exist, create derived files rather than editing source verification records:

- clear hard-filter passes;
- near matches blocked only by unknown fields;
- hard rejects with rejection reason;
- managed-Kubernetes candidates;
- database-node candidates;
- benchmark queue.

Derived results must point back to the verified source batch and must never overwrite the underlying observed facts.

## Benchmark phase

Candidates that survive hard filters should move to benchmark validation. Benchmark data must be stored separately from advertised specifications and should include test date, region, instance plan, OS, kernel, tool version, and full command parameters.

Recommended benchmark categories:

- sustained CPU and steal-time behavior;
- random and sequential storage latency/IOPS;
- fsync-sensitive database behavior;
- network RTT, packet loss, and sustained throughput;
- API provisioning and deletion latency for elastic-cloud candidates;
- node-pool scale-up/down behavior for managed Kubernetes.
