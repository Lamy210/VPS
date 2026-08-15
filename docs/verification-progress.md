# Verification Progress

This file tracks provider verification and strict requirement matching. It is not a recommendation list.

Machine-readable status: `results/derived/research-status.yaml`.

## Current counts

- Official-source verification batches: **18**
- Unique verified provider records: **166**
- Targeted follow-up files: **5**
- Strict standard-compute passes: **4**
- Strict database-node passes: **0**
- Strict managed-Kubernetes passes: **1**
- Benchmark / operational-validation ready resources: **5**
- Measured benchmark resources: **0**

## Latest verification batches

- Batch 016: ServerCheap, Server Optima, MonoVM, Rad Web Hosting, Alpenhost, RackGenius, VoyraCloud, quicksrv, InMotion Hosting, HostArmada.
- Batch 017: Hivelocity, Fasthosts, HostUp, Hostman, Webyne, Serverwala, ScalaHosting, Arct Cloud, Raff, 1Gbits.
- Batch 018: BlastVPS, dogado, Genesis Public Cloud, Linkdata, OnetSolutions, SprintCDN, NoBull Networks, TakeHost, Hexabyte, GS Webservices.

Full source history is stored as `results/verified/batch-001.yaml` through `results/verified/batch-018.yaml`.

## Latest targeted follow-up

`results/verified/followup-005.yaml` revisited SprintCDN, dogado and Server Optima without increasing the unique-provider count:

- SprintCDN: provider-owned IP space and BYOIP are confirmed, but plan-level included IPv4 for VPS 4 is still not explicitly published.
- dogado: Cloud Server 4.0 REST API, Private Network add-on and custom ISO support are confirmed, while the selected unmanaged Cloud Server still exposes only generic full-virtualization wording rather than explicit KVM/QEMU-KVM.
- Server Optima: Full Backup support is reconfirmed, but the selected VPS plan's independent-backup price remains unpublished; dedicated-server backup selectors are not reused as VPS pricing.

## Strict results

### Standard compute

Clear advertised-specification passes remain:

1. **ServaRica — KVM Slim Slice 2**
2. **HostEons — Hybrid Special 2**
3. **Advin Servers — KVM Premium S (Miami)**
4. **InterServer — Cloud Compute 4 Slices**

These are advertised-specification passes only. They are not performance recommendations until measured validation is completed.

Highest-value unresolved candidates now include:

- **SprintCDN VPS 4** — $13/month, 4 vCPU, 8 GB RAM, 160 GB NVMe, unmetered 1 Gbps shared port, KVM, API/CLI and hourly/monthly billing. The only unresolved standard-compute hard field is plan-level included IPv4.
- **dogado Cloud Server M 4.0** — €10.99 regular monthly, 4 vCPU, 8 GB, 200 GB NVMe, traffic flat, 1 Gbps, IPv4/IPv6 and one-month minimum term. At the current EUR/USD snapshot the budget passes; the selected product still says only full virtualization rather than explicitly KVM/QEMU-KVM.
- **ServerCheap NVMe-KVMb-10GB-New** — $6.80/month, 4 vCPU, 10 GB, 80 GB NVMe, 6 TB, IPv4/IPv6 and KVM. Public VPS port speed remains unverified; the provider's 10 Gbps DDoS capacity is not reused as a port-speed fact.
- **quicksrv AMS-Standard 8** — €7.99 VAT-inclusive, 3 vCPU, 8 GB DDR5, 180 GB NVMe, 40 Gbps shared port, IPv4, KVM, off-site backups and no contract. FX budget passes; a numeric fair-use transfer allowance remains the only strict blocker.
- **OnetSolutions HP-8** — technically strong with EPYC, 8 GB DDR5, 80 GB NVMe, 1 Gbps, IPv4/IPv6, KVM, VPC, off-site backups and snapshots. Current official pages expose conflicting HP-8 prices, so price/VAT/TCO remains unresolved instead of selecting the cheaper value.
- **Hexabyte e3.large** — €7.69 monthly cap, 4 vCPU, 8 GB, 80 GB triple-replicated NVMe, 20 TB and IPv4/IPv6. FX budget passes, but KVM acceleration, public port speed and current stock remain blockers; the provider page reported cloud instances out of stock.

### FX snapshot effects

`results/derived/fx-snapshot-2026-08-16.yaml` records a live snapshot of **1 EUR = 1.1569 USD** at `2026-08-15T20:54:00Z`.

At that snapshot:

- GS Webservices `ng-Cloud L`: €13.03 -> $15.0744, so it **fails** the hard $15 budget by a very small margin despite meeting the technical requirements.
- dogado `Cloud Server M 4.0`: €10.99 -> $12.7143, so the budget passes and KVM is the remaining blocker.
- Hexabyte `e3.large`: €7.69 -> $8.89656, so budget passes.
- quicksrv `AMS-Standard 8`: €7.99 -> $9.24363, so budget passes.
- Alpenhost `Silber vServer`: €14.79 -> $17.1106, so it fails the hard budget at this snapshot.

FX-derived decisions expire under `docs/fx-tco-policy.md` and should be refreshed on a purchase decision date.

### Database node

`clear_pass` remains empty, but **Server Optima is still the shortest-path candidate**.

`AMD EPYC 7763 Plan 1` verifies a $19.20 base VM, 4 vCPU, 16 GB RAM, 200 GB NVMe RAID10, 1 Gbps unmetered network, KVM, private networking/VLAN, snapshots, Full Backup support and 99.9% availability/network SLA. The remaining strict blocker is effective TCO for the required independent Full Backup: feature availability is verified, selected-plan backup pricing is not.

Other shortest-path candidates remain VPSnet, ServaRica, VSYS Host and Onidel.

### Managed Kubernetes

Clear pass remains:

1. **UpCloud Managed Kubernetes** using `PREMIUM-2xCPU-4GB` as the concrete qualifying worker.

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
- `Up to` or shared network is not interpreted as guaranteed sustained throughput.
- Full virtualization does not automatically prove KVM.
- OpenStack/QEMU does not automatically prove KVM acceleration.
- Official-page pricing conflicts remain unresolved until the effective price is pinned.
- FX-derived budget results are timestamped and expire.
- Physical threads are not silently substituted for explicit vCPU/core requirements.
- Snapshots do not automatically satisfy independent-backup requirements.
- Provider-advertised performance is not benchmark evidence.
- Promotional or annualized prepaid pricing is not ordinary month-to-month pricing.

## Next work

1. Resolve SprintCDN IPv4 inclusion; it is one hard field from a strict standard-compute pass.
2. Resolve dogado KVM implementation, ServerCheap public port speed and quicksrv numeric traffic allowance.
3. Resolve OnetSolutions price/VAT inconsistency and Hexabyte KVM/port/stock blockers.
4. Capture Server Optima Full Backup price for the first possible strict database-node pass.
5. Continue Batch 019 beyond 166 verified providers.
6. Execute measured validation only after an exact plan/region is pinned and spend is explicitly chosen.
