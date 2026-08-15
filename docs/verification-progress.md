# Verification Progress

This file tracks the provider-verification queue. It is not a recommendation list.

## Counts

- Discovery seed entries: maintained in `data/provider-candidates.seed.yaml`
- Official-source verification batches completed: 11
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
- Providers in verified batch 011: 8
- Total unique provider records in official-source verification batches: 100
- Targeted follow-up files: 2
- Benchmark-ready resources: 2
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

### Batch 011 — IX/ecosystem discovery converted to official records
AFRICLOUD, NoAck Hosting, OrionVM, D4 Networks, FyfeWeb, Free Range Cloud, Netbela, EstNOC.

Verified source files are stored as `results/verified/batch-001.yaml` through `results/verified/batch-011.yaml`.

## Targeted follow-ups

`results/verified/followup-001.yaml` deepens existing records without incrementing the unique-provider count:

- Onidel: core HA/private-network/API/backup features reconfirmed, but the current pricing widget still fails to expose a stable 16 GB plan/price.
- KVMVPS.co.za: dedicated CPU/KVM/NVMe/snapshot/backup facts reconfirmed; exact 16 GB custom price, private network, port speed, and explicit current SLA remain unresolved.
- Cherry Servers: a Tokyo 16 GB dedicated-resource VDS is pinned to an exact current plan and price; it fails the current database budget.
- IONOS: Memory Cube S/M pricing is reconfirmed; transfer allowance, public port speed, and the reusable profile's KVM requirement remain unresolved.

`results/verified/followup-002.yaml` resolves several high-priority gaps:

- HostEons: official product and knowledgebase evidence now establishes that the Hybrid/VDS product family is KVM-based; Hybrid Special 2 therefore clears the remaining standard-compute virtualization blocker.
- OrangeVPS: IPv4 inclusion is confirmed for VPS products, but exact BASIC NVMe hypervisor technology remains unresolved.
- Onie Cloud: VPC, 10 Gbps shared networking, dual stack, REST API/CLI/Python SDK, hourly billing, SLA, autoscaling, load balancing and backup/snapshot capabilities are strengthened; public-cloud hypervisor and normalized TCO remain unresolved.
- HostBrr: exact EPYC-8GBrr resources, IPv4/IPv6, backup slot and KVM product-family evidence are now confirmed; stable current numeric price is the remaining standard-compute blocker.

## Strict derived filtering

Derived files currently include:

- `results/derived/standard-compute-strict.yaml`
- `results/derived/database-node-strict.yaml`
- `results/derived/managed-kubernetes-strict.yaml`

### Standard compute

Current clear advertised-specification passes after targeted follow-up:

- ServaRica KVM Slim Slice 2.
- HostEons Hybrid Special 2.

High-priority blocked candidates include:

- Onie Cloud VM 4-8: strong Asia-local/API-driven resource match; blocked by exact public-cloud hypervisor, normalized TCO, and promotion persistence.
- Advin Servers Miami Standard XS: strong price/specification match; blocked by explicit IPv4 verification and promotion persistence.
- HostBrr EPYC 8 GB: KVM, IPv4/IPv6, backup slot, EPYC 9004, NVMe and 10 Gbps are now confirmed; blocked only by stable current numeric price.
- CloudXact, Kencang, ServerUtama, Rumahweb, OrangeVPS, BulutVDS, HostHatch, Contabo, Hetzner, IONOS, SferaHost, Netlen, ITMCloud, SmartHost, and IPXON remain blocked by one or more explicit unknown hard fields.

A provider-advertised hard-filter pass is not a final recommendation. It advances the resource to benchmark and operational verification.

### Database node

Current `clear_pass` is empty.

Strong near-matches include Advin Servers, HostBrr, VSYS Host, VPSnet, ServaRica, Onidel, BulutVDS, netcup, BDIX Web Host, BengalCloud, Hostinger, and ITMCloud. Each is blocked by one or more hard requirements such as private networking, reliable backups, snapshot semantics, SLA, KVM, exact current price, port speed, IPv4, or normalized TCO.

### Managed Kubernetes

Current `clear_pass` is empty because no verified record yet covers every hard field together. UpCloud, Scaleway, Exoscale, DigitalOcean, Vultr, GKE, and AKS are among the shortest-path follow-up candidates.

## Benchmark readiness

`results/benchmark/queue.yaml` separates resources that are ready for measured validation from candidates that are still blocked by source-verification gaps.

Current benchmark-ready standard-compute resources:

- ServaRica KVM Slim Slice 2.
- HostEons Hybrid Special 2.

High-priority blocked benchmark candidates include Onie Cloud, Advin Servers, and HostBrr for standard compute.

No benchmark has been executed or claimed yet. The queue defines reproducible CPU, storage, database, network, and stability checks and requires exact region/plan/OS/kernel/tool metadata for future measurements.

## FX and TCO normalization

`docs/fx-tco-policy.md` defines the cross-currency and total-cost rules used by derived comparisons.

Key rules:

- preserve provider-native prices;
- convert only in derived outputs with a timestamped FX snapshot;
- keep ordinary monthly, hourly-cap, annualized, multi-year, promotional, recurring-promo, renewal, and setup-fee prices separate;
- include required IPv4, private network, storage, backup, load balancer, NAT, egress and taxes in effective TCO when the active profile requires them;
- do not force a ranking when normal FX movement can reverse two nearly equal prices.

## Notable classification findings

- A bargain headline price is frequently invalidated by a hard network, storage, contract, virtualization, IPv4, transfer, or availability requirement.
- ServaRica and HostEons are now the two strict standard-compute advertised-specification matches ready for benchmark validation.
- Onie Cloud remains one of the strongest Asia-local API-driven compute leads, but strict filtering correctly withholds pass status until hypervisor and TCO/promotion questions are resolved.
- HostBrr is now technically much closer to strict clearance; current numeric price is the remaining standard-compute blocker for the selected EPYC 8 GB product.
- AFRICLOUD, OrionVM and Netbela expand the catalog beyond bargain VPS into regional/wholesale/configurable cloud classes and should not be ranked purely by RAM price.
- NoAck Hosting and FyfeWeb demonstrate why the public-port hard floor matters even when regional/network qualities are otherwise attractive.
- EstNOC provides unusually broad regional coverage, including Tokyo, but its currently listed Japan base tiers do not reach the reusable 8 GB floor.
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
- local-currency conversion snapshot;
- stock / location availability;
- marketing location versus actual datacenter;
- fair-use definitions for `unlimited` or `unmetered` traffic.

## Next official-verification queue

### Batch 012 — additional global/Europe/Asia discovery

- remaining VPS index candidates with 8 GB or configurable-memory signals
- regional Root Server / VDS providers not yet normalized into the verified set
- API/hourly providers absent from major cloud comparisons
- South Korea, Hong Kong, Taiwan and India/Pakistan local providers not yet counted

### Follow-up 003 — hard-filter unknown reduction

- Onie Cloud public hypervisor and ordinary monthly TCO
- Advin Servers IPv4 inclusion and promotion persistence
- HostBrr stable current 8/16 GB pricing
- OrangeVPS BASIC NVMe virtualization
- BulutVDS EPYC virtualization
- VSYS Host private-network verification
- VPSnet private-network verification
- ServaRica database-node private-network/backup/SLA verification
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