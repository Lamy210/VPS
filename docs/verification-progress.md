# Verification Progress

This file tracks provider verification and strict requirement matching. It is not a recommendation list.

Machine-readable status: `results/derived/research-status.yaml`.

## Current counts

- Official-source verification batches: **14**
- Unique verified provider records: **126**
- Targeted follow-up files: **4**
- Strict standard-compute passes: **3**
- Strict database-node passes: **0**
- Strict managed-Kubernetes passes: **1**
- Benchmark / operational-validation ready resources: **4**
- Measured benchmark resources: **0**

## Verification batches

- Batch 001: HostHatch, Contabo, Hetzner, netcup, UpCloud, Vultr, OVHcloud, Gcore, Civo.
- Batch 002: Onidel, GreenCloud, Hostinger, Melbicom, ExtraVM, VSYS Host, CloudBlast.
- Batch 003: OrangeVPS, WebHorizon, FlowVPS, ServaRica, HostEons, RackNerd, DediRock, Alwyzon, Time4VPS, Webdock, LunaNode, FiberState.
- Batch 004: DigitalOcean, Akamai Cloud / Linode, Kamatera, Scaleway, Exoscale, Cherry Servers, IONOS.
- Batch 005: Nevacloud, vHost, OneAsiaHost, VPSnet, Virtuaal.com, BulutVDS, Netlen, ITMCloud, NovaCloud Africa, Cloudify.ro, NAV.RO.
- Batch 006: SferaHost, DedicatServer.ro, Astra Telekom, KVMVPS.co.za, GamCo, Mocky, BDIX Web Host, BengalCloud, Shinjiru, Server Galactic.
- Batch 007: CloudSigma, Serverspace, Alibaba Cloud, Tencent Cloud, Huawei Cloud, Oracle Cloud Infrastructure, IBM Cloud, AWS Lightsail, Google Cloud, Microsoft Azure.
- Batch 008: IPXON, VPSMalaysia, Randhost, AkileCloud, SpeedyPage, Shock Hosting, SmartHost, Virtono, Evoxt, LiteServer, Aluy.
- Batch 009: Advin Servers, HostBrr, HostSlick, UltaHost.
- Batch 010: FormoHost, FussionHost, ServerUtama, Herza Cloud, GOFIBER, Kencang, CloudXact, Rumahweb, H2Cloud, Onie Cloud, ModernOne / Nocser.
- Batch 011: AFRICLOUD, NoAck Hosting, OrionVM, D4 Networks, FyfeWeb, Free Range Cloud, Netbela, EstNOC.
- Batch 012: NAVER Cloud Platform, NHN Cloud, KT Cloud, LayerStack, E2E Cloud, Cyfuture Cloud, Chief Telecom, CtrlS, Yotta.
- Batch 013: Brightbox, Krystal Cloud / Katapult, TransIP, Aruba Cloud, Leaseweb, Cleura, Open Telekom Cloud.
- Batch 014: CloudCone, BandwagonHost, GigsGigsCloud, Crunchbits, RamNode, OneProvider, Cloudzy, QuantVPS, VPSServer, Hostwinds.

Source files are `results/verified/batch-001.yaml` through `results/verified/batch-014.yaml`.

## Targeted follow-ups

### Follow-up 001

Deepened Onidel, KVMVPS.co.za, Cherry Servers, and IONOS without increasing the unique-provider count.

### Follow-up 002

- Resolved HostEons Hybrid/VDS KVM evidence, allowing Hybrid Special 2 to become a strict standard-compute match.
- Strengthened OrangeVPS IPv4/no-contract/SLA evidence while keeping BASIC NVMe hypervisor unknown.
- Strengthened Onie Cloud VPC/network/API/autoscaling/LB/backup evidence while keeping public-VM hypervisor and TCO unresolved.
- Resolved HostBrr KVM/resource/IP/backup-slot evidence; current numeric price remains unresolved.

### Follow-up 003

- Promoted UpCloud Managed Kubernetes to the first strict managed-Kubernetes pass using a concrete `PREMIUM-2xCPU-4GB` worker.
- Reduced ServaRica database blockers to private networking, snapshots, and independent backups.
- Reduced VPSnet database blockers to private networking and normalized TCO.
- Reduced VSYS Host database blockers to customer-configurable private networking on the ordinary VPS product.

### Follow-up 004

- Promoted **Advin Servers KVM Premium S (Miami)** to a strict standard-compute pass using the ordinary **$10/month** tier instead of depending on the promotional Standard XS tier.
- Verified KVM, 4 vCPU, 8 GB RAM, 128 GB NVMe, 5 TB transfer, 10 Gbps, monthly/no-contract operation, and presence of a primary IPv4 for the Advin VPS service.
- Rechecked VPSnet, VSYS Host, and ServaRica public documentation for their remaining database blockers. Where customer private networking or backup semantics could not be established, the field remains `unknown` rather than being guessed.

## Strict results

### Standard compute

Clear advertised-specification passes:

1. **ServaRica — KVM Slim Slice 2**
2. **HostEons — Hybrid Special 2**
3. **Advin Servers — KVM Premium S (Miami)**

These are advertised-specification passes only. They are not performance recommendations until measured validation is completed.

High-priority blocked candidates include Onie Cloud, HostBrr, CloudCone, Crunchbits, VPSServer, CloudXact, Kencang, ServerUtama, Rumahweb, OrangeVPS, BulutVDS, Aruba Cloud, LayerStack, and others whose remaining hard fields are explicitly documented in `results/derived/standard-compute-strict.yaml`.

Batch 014 adds several useful classification examples:

- **CloudCone SSD VPS 5** clears the technical CPU/RAM/storage/transfer/port/IPv4/KVM floors at a displayed **$4.79/month equivalent**, but it is **$57.59 billed annually in advance**. Annualized prepaid pricing is not silently treated as ordinary month-to-month pricing.
- **Crunchbits Xeon 6146 VDS 8 GB** is **$8/month** with one dedicated physical core / two threads, 150 GB NVMe, 20 TB and 2.5 Gbps. The repository does not silently convert CPU threads into the profile's `min_vcpu` count, and the exact VDS hypervisor remains separately verified.
- **VPSServer** has KVM/NVMe/public-IP/hourly billing and global regions, but its public configurator did not expose a stable exact 8 GB price/port snapshot in the parsed page.
- BandwagonHost, GigsGigsCloud, RamNode, OneProvider, Cloudzy, QuantVPS, and Hostwinds are technically capable but fail the current $15 standard-compute budget on the verified 8 GB tiers.

### Database node

`clear_pass` remains empty.

Shortest-path candidates:

- **VPSnet** — private network + normalized TCO remain.
- **ServaRica** — private network + snapshots + independent backup remain.
- **VSYS Host** — customer-configurable private network applicability/TCO remains to be pinned for the selected Singapore VPS architecture.
- **Onidel** — exact current 16 GB plan/price + KVM remain.

Other near-matches include HostBrr, Advin Servers, BulutVDS, netcup, BDIX Web Host, BengalCloud, Hostinger, and ITMCloud.

### Managed Kubernetes

Clear pass:

1. **UpCloud Managed Kubernetes** using `PREMIUM-2xCPU-4GB` as the concrete qualifying worker.

Blocked high-priority candidates include Scaleway Kapsule, Exoscale SKS, DigitalOcean DOKS, Vultr VKE, GKE, AKS, and NAVER Cloud Platform.

## Validation readiness

Ready for measured validation:

- ServaRica KVM Slim Slice 2 — standard compute.
- HostEons Hybrid Special 2 — standard compute.
- Advin Servers KVM Premium S — standard compute.
- UpCloud Managed Kubernetes / `PREMIUM-2xCPU-4GB` — operational/scaling validation.

No benchmark result has been executed or claimed yet.

## Data validation

The repository runs `.github/workflows/validate-research-data.yml` on relevant pull-request changes.

CI checks include:

- YAML parsing and duplicate mapping keys;
- required verification-batch metadata;
- normalized canonical-provider duplicates;
- follow-up references to registered providers;
- derived and benchmark references to registered providers;
- `research-status.yaml` batch/provider/follow-up counts;
- strict clear-pass counts;
- validation-ready queue count.

## FX and TCO

`docs/fx-tco-policy.md` defines the normalization policy:

- retain provider-native prices;
- use timestamped FX snapshots only in derived output;
- keep ordinary monthly, hourly-cap, prepay, promotion, renewal, and setup-fee prices separate;
- include required IPv4, private network, storage, backup, load balancer, NAT, egress, and applicable taxes in effective TCO;
- avoid false precision where ordinary FX movement could reverse rankings.

## Data-quality rules

- Unknown hard fields never silently pass.
- `Up to` bandwidth is not automatically treated as a guaranteed hard floor.
- VPS/VDS naming does not prove KVM, IPv4, private networking, or dedicated CPU.
- Physical threads are not silently substituted for explicit vCPU/core requirements.
- Marketing geography does not prove datacenter geography.
- Snapshots do not automatically satisfy independent-backup requirements.
- Provider-advertised performance is not benchmark evidence.
- Promotional or annualized prepaid pricing is not ordinary month-to-month pricing.

## Next work

Highest-value next steps:

1. Reduce remaining database-node unknowns for VPSnet, ServaRica, VSYS Host, and Onidel.
2. Resolve standard-compute unknowns for Onie Cloud, HostBrr, CloudCone, Crunchbits, VPSServer, OrangeVPS, and BulutVDS.
3. Pin concrete managed-Kubernetes worker architectures for Scaleway, Exoscale, and DigitalOcean.
4. Continue Batch 015 beyond 126 verified providers.
5. Execute measured validation only after the exact plan/region is pinned and the user chooses to spend on the candidate instance.
