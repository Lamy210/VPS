# Verification Progress

This file tracks provider verification and strict requirement matching. It is not a recommendation list.

## Counts

- Official-source verification batches completed: 11
- Total unique provider records in verification batches: 100
- Targeted follow-up files: 3
- Strict profile clear passes:
  - standard compute: 2
  - database node: 0
  - managed Kubernetes: 1
- Benchmark / operational-validation ready resources: 3
- Benchmark-measured resources: 0

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

Source files are `results/verified/batch-001.yaml` through `results/verified/batch-011.yaml`.

## Targeted follow-ups

### Follow-up 001

Deepened Onidel, KVMVPS.co.za, Cherry Servers and IONOS without incrementing the unique-provider count.

### Follow-up 002

- HostEons: exact Hybrid/VDS KVM evidence resolved the final standard-compute virtualization blocker.
- OrangeVPS: IPv4/no-contract/SLA strengthened; BASIC NVMe hypervisor remains unresolved.
- Onie Cloud: VPC, 10 Gbps shared network, dual stack, API/CLI/Python SDK, hourly billing, autoscaling, LB and backup/snapshot capabilities strengthened; public-VM hypervisor and normalized TCO remain unresolved.
- HostBrr: KVM product family, exact EPYC resources, IPv4/IPv6 and backup slot resolved; current numeric price remains unresolved.

### Follow-up 003

- UpCloud Managed Kubernetes: a concrete qualifying worker architecture is now pinned using `PREMIUM-2xCPU-4GB`. Official documentation covers 2 CPU, 4 GB RAM, 50 GB MaxIOPS storage, IPv4/IPv6, 1 Gbps public networking, private networking, managed load balancing, API, Terraform, native Cluster Autoscaler and monitoring integrations. This clears the reusable managed-Kubernetes hard requirements.
- ServaRica database node: KVM, 99.9%+ SLA, IPv4 and selected 16 GB plan capacity/network are resolved. Remaining hard fields are private networking, snapshots and independent backups.
- VPSnet database node: KVM, 16 GB/4-vCPU/100-GB replicated Ceph NVMe, 30 TB, 1 Gbps, snapshots, 99.95% SLA and daily backups on a separate remote server are resolved. Remaining hard fields are private networking and normalized TCO.
- VSYS Host database node: Singapore KVM, IPv4, snapshots/backups, 1 Gbps uplink and 99.97% uptime are resolved. Customer-configurable private networking on the ordinary VPS product remains unresolved.

## Strict results

### Standard compute

Clear advertised-specification passes:

1. ServaRica — KVM Slim Slice 2.
2. HostEons — Hybrid Special 2.

High-priority blocked candidates:

- Onie Cloud — blocked by public-cloud hypervisor, normalized TCO and promotion persistence.
- Advin Servers — blocked by explicit IPv4 inclusion and promotion persistence.
- HostBrr — KVM/IPv4/IPv6/resource facts resolved; blocked by current numeric price.
- CloudXact, Kencang, ServerUtama, Rumahweb, OrangeVPS, BulutVDS, HostHatch, Contabo, Hetzner, IONOS, SferaHost, Netlen, ITMCloud, SmartHost, IPXON, FyfeWeb and Netbela remain blocked by explicit hard-field unknowns.

### Database node

`clear_pass` remains empty.

Shortest-path candidates now include:

- VPSnet — private network + normalized TCO remain.
- ServaRica — private network + snapshot + independent backup remain.
- VSYS Host — customer-configurable private network remains.
- Onidel — exact current 16 GB plan/price + KVM remain.
- HostBrr, Advin, BulutVDS, netcup, BDIX Web Host, BengalCloud, Hostinger and ITMCloud require additional hard-field closure.

### Managed Kubernetes

Clear pass:

1. UpCloud Managed Kubernetes with a qualifying Premium worker architecture.

Blocked high-priority candidates:

- Scaleway Kapsule — pin a >=1-Gbps worker shape with >=40 GB storage and explicit public IPv4 behavior.
- Exoscale SKS — resolve LB, monitoring, local-storage and worker IPv4 facts.
- DigitalOcean DOKS — resolve monitoring, qualifying worker shape and selected worker private-network semantics.
- Vultr VKE, GKE and AKS remain valuable follow-up candidates.

## Validation readiness

`results/benchmark/queue.yaml` separates source verification from measured validation.

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

### Managed-Kubernetes follow-up

- Scaleway concrete >=1-Gbps worker + IPv4.
- Exoscale LB/monitoring/worker storage/IP.
- DigitalOcean monitoring + concrete qualifying worker.
- GKE / AKS concrete single-region architecture verification.

### Batch 012 — expand beyond 100 providers

Continue official verification of additional Root Server, VDS, regional Cloud, API/hourly and local-provider candidates, especially South Korea, Hong Kong, Taiwan, India/Pakistan and additional European regional providers.
