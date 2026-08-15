# Verification Progress

This file tracks provider verification and strict requirement matching. It is not a recommendation list.

Machine-readable status: `results/derived/research-status.yaml`.

## Current counts

- Official-source verification batches: **16**
- Unique verified provider records: **146**
- Targeted follow-up files: **4**
- Strict standard-compute passes: **4**
- Strict database-node passes: **0**
- Strict managed-Kubernetes passes: **1**
- Benchmark / operational-validation ready resources: **5**
- Measured benchmark resources: **0**

## Latest verification batches

- Batch 014: CloudCone, BandwagonHost, GigsGigsCloud, Crunchbits, RamNode, OneProvider, Cloudzy, QuantVPS, VPSServer, Hostwinds.
- Batch 015: InterServer, BuyVM, Clouding.io, mivoCloud, EthernetServers, HostNamaste, HostSailor, V.PS, Togglebox, Bacloud.
- Batch 016: ServerCheap, Server Optima, MonoVM, Rad Web Hosting, Alpenhost, RackGenius, VoyraCloud, quicksrv, InMotion Hosting, HostArmada.

Full source history is stored as `results/verified/batch-001.yaml` through `results/verified/batch-016.yaml`.

## Strict results

### Standard compute

Clear advertised-specification passes remain:

1. **ServaRica — KVM Slim Slice 2**
2. **HostEons — Hybrid Special 2**
3. **Advin Servers — KVM Premium S (Miami)**
4. **InterServer — Cloud Compute 4 Slices**

These are advertised-specification passes only. They are not performance recommendations until measured validation is completed.

New high-priority Batch 016 unknowns:

- **ServerCheap NVMe-KVMb-10GB-New** — $6.80/month, 4 vCPU, 10 GB RAM, 80 GB NVMe, 6 TB, IPv4, KVM, snapshot and 99.9% uptime are verified. The provider's published 10 Gbps value is DDoS-protection capacity, not VPS port speed; no qualifying public-port speed is currently verified.
- **quicksrv AMS-Standard 8** — €7.99/month VAT-inclusive, 3 vCPU, 8 GB DDR5, 180 GB NVMe, 40 Gbps shared network, IPv4, KVM, daily off-site backup, no contract. The public page does not publish a numeric fair-use transfer allowance, so the >=2 TB hard requirement remains unresolved.
- **Alpenhost Silber vServer** — €14.79/month, 4 vCPU, 8 GB, 150 GB NVMe Ceph, 10 Gbps, IPv4/IPv6, KVM, backup/snapshots and 99.99% advertised availability. USD TCO remains unresolved under the repository FX policy.

Long-prepay examples remain deliberately unknown rather than passes:

- HostArmada Fusion advertises $10.74/month equivalent with 12-month prepayment while its regular reference is $21.48/month.
- InMotion's 8 GB managed VPS promotion can be below $15/month on a 24-month term but renews above the profile ceiling and the selected product's port/KVM facts are not fully pinned.

### Database node

`clear_pass` remains empty, but **Server Optima is now the shortest-path candidate**.

Server Optima `AMD EPYC 7763 Plan 1` verifies:

- $19.20/month base VM;
- 4 vCPU;
- 16 GB RAM;
- 200 GB NVMe SSD RAID10;
- 1 Gbps unmetered network;
- KVM;
- customer private networking/VLAN support;
- snapshot support;
- Full Backup feature availability;
- 99.9% service/network availability commitment.

The remaining strict blocker is **effective TCO for the required independent Full Backup**. The provider advertises Full Backup support but does not publish the selected VPS plan's backup charge on the current public VPS page. The repository therefore does not assume that backup is included in the $19.20 base price.

Other shortest-path candidates remain VPSnet, ServaRica, VSYS Host, and Onidel.

### Managed Kubernetes

Clear pass remains:

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

The repository runs `.github/workflows/validate-research-data.yml` on relevant pull-request changes. It validates YAML/schema integrity, normalized provider identity uniqueness, cross-file references, source/derived counts, strict clear-pass counts, and validation-ready queue counts.

## Data-quality rules

- Unknown hard fields never silently pass.
- DDoS-protection capacity is not treated as VPS port speed.
- `Up to` bandwidth is not automatically treated as a guaranteed hard floor.
- Shared port speed is not interpreted as guaranteed sustained throughput.
- VPS/VDS naming does not prove KVM, IPv4, private networking, or dedicated CPU.
- Physical threads are not silently substituted for explicit vCPU/core requirements.
- Marketing geography does not prove datacenter geography.
- Snapshots do not automatically satisfy independent-backup requirements.
- Backup feature availability does not prove backup cost is included in base VM pricing.
- Provider-advertised performance is not benchmark evidence.
- Promotional or annualized prepaid pricing is not ordinary month-to-month pricing.

## Next work

1. Capture Server Optima Full Backup price and determine whether effective database-node TCO remains <= $30/month.
2. Find explicit ServerCheap VPS public-port speed and quicksrv numeric fair-use transfer allowance.
3. Reduce VPSnet / ServaRica / VSYS Host / Onidel database blockers.
4. Continue standard-compute unknown reduction for HostBrr, Onie Cloud, Crunchbits, VPSServer, OrangeVPS, and BulutVDS.
5. Continue Batch 017 beyond 146 verified providers.
6. Execute measured validation only after an exact plan/region is pinned and spend is explicitly chosen.
