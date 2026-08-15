# Verification Progress

This file tracks provider verification and strict requirement matching. It is not a recommendation list.

Machine-readable status: `results/derived/research-status.yaml`.

## Current counts

- Official-source verification batches: **15**
- Unique verified provider records: **136**
- Targeted follow-up files: **4**
- Strict standard-compute passes: **4**
- Strict database-node passes: **0**
- Strict managed-Kubernetes passes: **1**
- Benchmark / operational-validation ready resources: **5**
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
- Batch 015: InterServer, BuyVM, Clouding.io, mivoCloud, EthernetServers, HostNamaste, HostSailor, V.PS, Togglebox, Bacloud.

Source files are `results/verified/batch-001.yaml` through `results/verified/batch-015.yaml`.

## Strict results

### Standard compute

Clear advertised-specification passes:

1. **ServaRica — KVM Slim Slice 2**
2. **HostEons — Hybrid Special 2**
3. **Advin Servers — KVM Premium S (Miami)**
4. **InterServer — Cloud Compute 4 Slices**

InterServer is the newest strict pass: $12/month, 2 CPU cores, 8 GB RAM, 160 GB SSD, 8 TB transfer, one IPv4, KVM, month-to-month billing, and a 10 Gbps shared port. The shared port is not interpreted as guaranteed sustained throughput, so network contention is a required validation target.

These are advertised-specification passes only. They are not performance recommendations until measured validation is completed.

High-priority blocked candidates include Onie Cloud, HostBrr, CloudCone, Crunchbits, VPSServer, CloudXact, Kencang, ServerUtama, Rumahweb, OrangeVPS, BulutVDS, Aruba Cloud, LayerStack, and other records listed in `results/derived/standard-compute-strict.yaml`.

Batch 014/015 classification examples:

- **CloudCone SSD VPS 5** clears the technical resource floors at a displayed $4.79/month equivalent, but the verified charge is $57.59 billed annually in advance. Annualized prepaid pricing is not silently treated as ordinary month-to-month pricing.
- **Crunchbits Xeon 6146 VDS 8 GB** is $8/month with one dedicated physical core / two threads, 150 GB NVMe, 20 TB and 2.5 Gbps. Threads are not silently converted into the profile's explicit vCPU/core-count requirement.
- **VPSServer** verifies KVM/NVMe/public-IP/hourly billing and global regions, but its exact qualifying 8 GB price and port speed remain dynamic/unpinned.
- **V.PS Cloud KVM** has KVM/IPv4/IPv6/1 Gbps, but the standard Cloud family is limited to 1 TB/month; its Storage family requires an exact 8 GB price/shape capture before it can be assessed.
- **Togglebox** publishes enough unit pricing to calculate the exact minimum standard shape; 2 vCPU + 8 GB + 60 GB NVMe + IPv4 is $33.46/month, so it fails the current $15 budget despite strong HA/API/Terraform features.

### Database node

`clear_pass` remains empty.

Shortest-path candidates remain:

- **VPSnet** — private network + normalized TCO remain.
- **ServaRica** — private network + snapshots + independent backup remain.
- **VSYS Host** — selected Singapore VPS private-network applicability/effective TCO remains to be pinned.
- **Onidel** — exact current 16 GB plan/price + KVM remain.

### Managed Kubernetes

Clear pass:

1. **UpCloud Managed Kubernetes** using `PREMIUM-2xCPU-4GB` as the concrete qualifying worker.

Blocked high-priority candidates include Scaleway Kapsule, Exoscale SKS, DigitalOcean DOKS, Vultr VKE, GKE, AKS, and NAVER Cloud Platform.

## Validation readiness

Ready for measured validation:

- ServaRica KVM Slim Slice 2 — standard compute.
- HostEons Hybrid Special 2 — standard compute.
- Advin Servers KVM Premium S — standard compute.
- InterServer Cloud Compute 4 Slices — standard compute.
- UpCloud Managed Kubernetes / `PREMIUM-2xCPU-4GB` — operational/scaling validation.

No benchmark result has been executed or claimed yet.

## Data validation

The repository runs `.github/workflows/validate-research-data.yml` on relevant pull-request changes.

Validation covers YAML/schema integrity, provider identity uniqueness, follow-up/derived/benchmark references, research-status counts, and cross-file bookkeeping. Strict-pass and validation-ready count checks are being strengthened as the dataset grows.

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
- Shared port speed is not interpreted as guaranteed sustained throughput.
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
4. Continue Batch 016 beyond 136 verified providers.
5. Execute measured validation only after the exact plan/region is pinned and the user chooses to spend on the candidate instance.
