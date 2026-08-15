# Verification Progress

This file tracks provider verification and strict requirement matching. It is not a recommendation list.

## Counts

- Official-source verification batches completed: 13
- Total unique provider records in verification batches: 116
- Targeted follow-up files: 3
- Strict profile clear passes:
  - standard compute: 2
  - database node: 0
  - managed Kubernetes: 1
- Benchmark / operational-validation ready resources: 3
- Benchmark-measured resources: 0

Machine-readable status: `results/derived/research-status.yaml`.

## Verification batches

- Batch 001: 9 — HostHatch, Contabo, Hetzner, netcup, UpCloud, Vultr, OVHcloud, Gcore, Civo.
- Batch 002: 7 — Onidel, GreenCloud, Hostinger, Melbicom, ExtraVM, VSYS Host, CloudBlast.
- Batch 003: 12 — OrangeVPS, WebHorizon, FlowVPS, ServaRica, HostEons, RackNerd, DediRock, Alwyzon, Time4VPS, Webdock, LunaNode, FiberState.
- Batch 004: 7 — DigitalOcean, Akamai Cloud / Linode, Kamatera, Scaleway, Exoscale, Cherry Servers, IONOS.
- Batch 005: 11 — Nevacloud, vHost, OneAsiaHost, VPSnet, Virtuaal.com, BulutVDS, Netlen, ITMCloud, NovaCloud Africa, Cloudify.ro, NAV.RO.
- Batch 006: 10 — SferaHost, DedicatServer.ro, Astra Telekom, KVMVPS.co.za, GamCo, Mocky, BDIX Web Host, BengalCloud, Shinjiru, Server Galactic.
- Batch 007: 10 — CloudSigma, Serverspace, Alibaba Cloud, Tencent Cloud, Huawei Cloud, Oracle Cloud Infrastructure, IBM Cloud, AWS Lightsail, Google Cloud, Microsoft Azure.
- Batch 008: 11 — IPXON, VPSMalaysia, Randhost, AkileCloud, SpeedyPage, Shock Hosting, SmartHost, Virtono, Evoxt, LiteServer, Aluy.
- Batch 009: 4 — Advin Servers, HostBrr, HostSlick, UltaHost.
- Batch 010: 11 — FormoHost, FussionHost, ServerUtama, Herza Cloud, GOFIBER, Kencang, CloudXact, Rumahweb, H2Cloud, Onie Cloud, ModernOne / Nocser.
- Batch 011: 8 — AFRICLOUD, NoAck Hosting, OrionVM, D4 Networks, FyfeWeb, Free Range Cloud, Netbela, EstNOC.
- Batch 012: 9 — NAVER Cloud Platform, NHN Cloud, KT Cloud, LayerStack, E2E Cloud, Cyfuture Cloud, Chief Telecom, CtrlS, Yotta.
- Batch 013: 7 — Brightbox, Krystal Cloud / Katapult, TransIP, Aruba Cloud, Leaseweb, Cleura, Open Telekom Cloud.

Source files are `results/verified/batch-001.yaml` through `results/verified/batch-013.yaml`.

## Targeted follow-ups

### Follow-up 001

Deepened Onidel, KVMVPS.co.za, Cherry Servers and IONOS without incrementing the unique-provider count.

### Follow-up 002

- HostEons: exact Hybrid/VDS KVM evidence resolved the final standard-compute virtualization blocker.
- OrangeVPS: IPv4/no-contract/SLA strengthened; BASIC NVMe hypervisor remains unresolved.
- Onie Cloud: VPC, 10 Gbps shared network, dual stack, API/CLI/Python SDK, hourly billing, autoscaling, LB and backup/snapshot capabilities strengthened; public-VM hypervisor and normalized TCO remain unresolved.
- HostBrr: KVM product family, exact EPYC resources, IPv4/IPv6 and backup slot resolved; current numeric price remains unresolved.

### Follow-up 003

- UpCloud Managed Kubernetes: concrete `PREMIUM-2xCPU-4GB` worker now covers the reusable hard requirements together with private networking, managed LB, API, Terraform, native Cluster Autoscaler and monitoring integration.
- ServaRica database node: KVM, 99.9%+ SLA, IPv4 and selected 16 GB capacity/network are resolved; private networking, snapshots and independent backups remain.
- VPSnet database node: KVM, 16 GB/4-vCPU/100-GB replicated Ceph NVMe, 30 TB, 1 Gbps, snapshots, 99.95% SLA and remote daily backups are resolved; private networking and normalized TCO remain.
- VSYS Host database node: Singapore KVM, IPv4, snapshots/backups, 1 Gbps uplink and 99.97% uptime are resolved; customer-configurable private networking on the ordinary VPS product remains unresolved.

## Strict results

### Standard compute

Clear advertised-specification passes:

1. ServaRica — KVM Slim Slice 2.
2. HostEons — Hybrid Special 2.

High-priority blocked candidates include Onie Cloud, Advin Servers, HostBrr, CloudXact, Kencang, ServerUtama, Rumahweb, OrangeVPS, BulutVDS, Aruba Cloud and LayerStack. They remain `unknown` until their exact hard-field gaps are resolved; they are not silently promoted by attractive headline pricing.

### Database node

`clear_pass` remains empty.

Shortest-path candidates:

- VPSnet — private network + normalized TCO remain.
- ServaRica — private network + snapshot + independent backup remain.
- VSYS Host — customer-configurable private network remains.
- Onidel — exact current 16 GB plan/price + KVM remain.
- HostBrr, Advin, BulutVDS, netcup, BDIX Web Host, BengalCloud, Hostinger and ITMCloud still require additional hard-field closure.

### Managed Kubernetes

Clear pass:

1. UpCloud Managed Kubernetes with a qualifying Premium worker architecture.

Blocked high-priority candidates include Scaleway Kapsule, Exoscale SKS, DigitalOcean DOKS, Vultr VKE, GKE, AKS and NAVER Cloud Platform. Each needs a concrete worker/network/automation architecture with all reusable hard fields pinned together.

## Recent market findings

- NAVER Cloud Platform has current Korea 8 GB server pricing plus VPC, REST APIs, snapshots, public IP, load balancing, managed Kubernetes, PostgreSQL and cache services; it is retained as a regional public-cloud candidate rather than compared only on bargain-VPS price.
- LayerStack adds Hong Kong, Singapore and Tokyo coverage with public API and paid 1-Gbps same-region private Layer-2 networking; its low-price ARM offers require exact selected-plan hard-field capture before strict qualification.
- E2E Cloud's CPU-compute pricing changed effective August 1, 2026; current transfer/SLA/API facts are recorded while numeric CPU-node pricing is left calculator/API-dependent.
- Aruba Cloud's OpenStack 8 GB promotional tier is recorded separately from its list price, promotion end date and required paid IPv4.
- Leaseweb adds a Japan Public Cloud/VPS class with hourly/monthly billing, API automation and 99.99% instance SLA, but exact Japan 8 GB TCO still needs capture.
- Brightbox, TransIP and Cleura demonstrate that regional-cloud automation and sovereignty benefits often sit in a different price class from bargain VPS products.

## Validation readiness

Ready:

- ServaRica KVM Slim Slice 2 — standard-compute benchmark.
- HostEons Hybrid Special 2 — standard-compute benchmark.
- UpCloud Managed Kubernetes / `PREMIUM-2xCPU-4GB` — operational and scaling validation.

No benchmark has been executed or claimed yet.

## FX and TCO

`docs/fx-tco-policy.md` defines the normalization policy:

- retain provider-native prices;
- use timestamped FX snapshots only in derived outputs;
- keep ordinary monthly, hourly-cap, prepay, promotion, renewal and setup-fee prices separate;
- include required IPv4, private networking, storage, backup, load balancer, NAT, egress and applicable taxes in effective TCO;
- avoid false precision when normal FX movement could reverse rankings.

## Data-quality rules

- Unknown hard fields never silently pass.
- `Up to` bandwidth is not automatically treated as a guaranteed hard floor.
- VPS/VDS naming does not prove KVM, IPv4, private networking or dedicated CPU.
- Marketing geography does not prove datacenter geography.
- Snapshots do not automatically satisfy independent-backup requirements.
- Provider-advertised performance is not benchmark evidence.
- Promotional/annualized pricing is not ordinary month-to-month pricing.

## Next work

### Follow-up 004 — highest-value unknown reduction

- VPSnet private network.
- VSYS ordinary-VPS private network.
- ServaRica private network + snapshot + independent backup.
- HostBrr stable current 8/16 GB numeric pricing.
- Advin IPv4 and promotion persistence.
- Onie Cloud public hypervisor and ordinary TCO.
- OrangeVPS BASIC NVMe virtualization.
- BulutVDS EPYC virtualization.
- Aruba OpenStack port/hypervisor/TCO details.
- LayerStack concrete 8 GB ARM/x86 plan details.

### Managed-Kubernetes follow-up

- Scaleway concrete >=1-Gbps worker + IPv4.
- Exoscale LB/monitoring/worker storage/IP.
- DigitalOcean monitoring + concrete qualifying worker.
- NAVER Cloud Platform concrete worker + autoscaler/Terraform/monitoring architecture.
- GKE / AKS concrete single-region architecture verification.

### Batch 014 — expand beyond 116 providers

Continue official verification of regional Root Server/VDS, local Asian cloud, sovereign European cloud, API/hourly compute and additional Kubernetes-capable providers while preserving provider identity normalization.

### Repository quality

Add schema validation and derived-status consistency checks before the research branch is considered merge-ready.
