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

## Strict derived filtering

`results/derived/standard-compute-strict.yaml` re-evaluates the verified records against every hard requirement in `requirements/profiles/standard-compute.yaml`.

Current strict result:

- ServaRica KVM Slim Slice 2 is a clear advertised-specification pass.
- OrangeVPS BASIC 3, HostEons Hybrid Special 2, and BulutVDS EPYC 4 have very strong price/specification signals but remain `unknown` because KVM virtualization was not explicitly verified for those exact product lines.
- HostHatch, Contabo, Hetzner, IONOS, SferaHost, Netlen, and ITMCloud have promising near-matches blocked by one or more unresolved hard fields such as port speed, virtualization, normalized TCO, or transfer allowance.
- A provider-advertised hard-filter pass is not a final recommendation. It advances the resource to benchmark and operational verification.

## Notable classification findings

- ServaRica exposes unusually inexpensive KVM plans with dedicated CPU and should move to benchmark validation.
- HostEons also exposes unusually inexpensive dedicated-resource plans, but the strict reusable profile still requires exact virtualization verification for the Hybrid product before calling it a pass.
- RackNerd specials are annual-prepay products; annualized monthly cost must not be treated as a normal month-to-month price.
- Time4VPS publishes materially different promotional and renewal prices across 1-, 12-, and 24-month terms.
- Mocky markets the VPS product in Kenya, but its official product page explicitly places the verified servers in an EU datacenter. Marketing geography is stored separately from actual datacenter geography.
- NAV.RO MultiCloud products are resource pools; aggregate pool RAM cannot be treated as per-VM RAM.
- Shinjiru, DedicatServer.ro, and GamCo show why network hard filters matter: inexpensive RAM/storage does not compensate for a verified sub-1-Gbps port when 1 Gbps is mandatory.
- DigitalOcean, Scaleway, Exoscale, and other managed-cloud products are evaluated as automation/managed-Kubernetes classes rather than ranked only by RAM price.
- FiberState is currently verified as bare metal rather than a public VPS offer.

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
- dynamic price tables that could not be captured;
- promotional versus renewal pricing and minimum contract term;
- local-currency conversion policy;
- stock / location availability;
- marketing location versus actual datacenter;
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
- OrangeVPS virtualization verification
- HostEons Hybrid virtualization verification
- BulutVDS virtualization verification

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
