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

The InterServer shape is $12/month with 2 CPU cores, 8 GB RAM, 160 GB SSD, 8 TB transfer, one IPv4, KVM, month-to-month billing, and a 10 Gbps shared port. The shared port qualifies as the configured interface speed but is not interpreted as guaranteed sustained throughput; contention testing is explicitly required.

These are advertised-specification passes only. They are not performance recommendations until measured validation is completed.

High-priority blocked candidates include Onie Cloud, HostBrr, CloudCone, Crunchbits, VPSServer, CloudXact, Kencang, ServerUtama, Rumahweb, OrangeVPS, BulutVDS, Aruba Cloud, and LayerStack.

Notable recent classifications:

- **CloudCone SSD VPS 5** technically clears CPU/RAM/storage/transfer/port/IPv4/KVM but is billed $57.59 annually in advance; its displayed $4.79/month is not treated as an ordinary monthly contract.
- **Crunchbits Xeon 6146 VDS 8 GB** is $8/month with one dedicated physical core / two threads, 150 GB NVMe, 20 TB and 2.5 Gbps. Thread count is not silently mapped to the profile's vCPU/core-count requirement.
- **VPSServer** verifies KVM/NVMe/public-IP/hourly billing and global regions, but its exact qualifying 8 GB price and selected-port speed remain dynamic/unpinned.
- **V.PS Cloud KVM** uses KVM with IPv4/IPv6 and a 1 Gbps port, but the standard Cloud family has 1 TB transfer. Storage KVM has more transfer but still needs an exact 8 GB shape/price capture.
- **Togglebox** publishes enough unit rates to calculate 2 vCPU + 8 GB + 60 GB NVMe + IPv4 at $33.46/month, so it fails the current $15 budget despite strong HA/API/Terraform features.

### Database node

`clear_pass` remains empty.

Shortest-path candidates:

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

The repository runs `.github/workflows/validate-research-data.yml` on relevant pull-request changes. It validates YAML/schema integrity, provider identity uniqueness, follow-up/derived/benchmark references, source/derived provider counts, strict clear-pass counts, and validation-ready queue counts.

## FX and TCO

`docs/fx-tco-policy.md` retains provider-native prices and applies timestamped FX only in derived output. Ordinary monthly, hourly-cap, prepay, promotion, renewal, setup fee, required IPv4/private network/storage/backup/LB/NAT/egress/tax costs remain separate inputs to effective TCO.

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

1. Reduce remaining database-node unknowns for VPSnet, ServaRica, VSYS Host, and Onidel.
2. Resolve standard-compute unknowns for Onie Cloud, HostBrr, CloudCone, Crunchbits, VPSServer, OrangeVPS, and BulutVDS.
3. Pin concrete managed-Kubernetes worker architectures for Scaleway, Exoscale, and DigitalOcean.
4. Continue Batch 016 beyond 136 verified providers.
5. Execute measured validation only after an exact plan/region is pinned and spend is explicitly chosen.
