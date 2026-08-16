# Discovery Sources

This repository uses multiple independent discovery paths. No single directory is treated as authoritative for pricing, availability, or provider quality.

## Source classes

### Tier 1: Official provider sources

Use for final verification.

- Official pricing pages and order forms
- Official product documentation
- Official status pages
- Official API documentation
- Official Terraform/OpenTofu provider documentation
- Official network, region, SLA, backup, and billing documentation

A resource should not reach `verified` status without at least one current official source supporting its material claims.

### Tier 2: Ecosystem and infrastructure directories

Use for provider discovery and feature cross-checks.

- OpenStack Marketplace: https://www.openstack.org/marketplace/public-clouds/
- OpenNebula Provider Catalog: https://opennebula.io/provider-catalog/
- PeeringDB: https://www.peeringdb.com/
- Internet exchange member directories
- Terraform Registry: https://registry.terraform.io/
- Kubernetes Cluster Autoscaler / Cluster API provider ecosystems

These sources are useful for discovering regional, sovereign, networking-focused, and automation-capable providers that generic VPS searches often miss.

### Tier 3: VPS and cloud comparison sources

Use for broad discovery, price leads, and independent performance evidence.

- VPSBenchmarks: https://www.vpsbenchmarks.com/
- VPS Price Tracker: https://vpspricetracker.com/
- ServerHunter: https://www.serverhunter.com/
- GetDeploying: https://getdeploying.com/providers

Aggregator prices are discovery data only until confirmed on the provider's current official page or order flow.

### Tier 4: Community and promotion sources

Use to discover emerging providers, new locations, and short-lived deals.

- LowEndTalk offers
- LowEndBox
- WebHostingTalk
- Regional hosting communities
- Provider announcement forums

Promotion data must record billing term, renewal price, setup fee, stock limitations, and expiration when known.

## Verification states

- `discovered`: provider/resource name found, not yet verified.
- `official-found`: official provider site or product page located.
- `spec-verified`: material plan specifications verified from an official source.
- `cost-verified`: effective recurring cost and mandatory add-ons verified.
- `network-verified`: transfer, port, private network, IP, and region details verified.
- `automation-verified`: API, cloud-init, Terraform/OpenTofu, or autoscaling behavior verified.
- `benchmarked`: independent benchmark data or controlled tests available.
- `shortlisted`: satisfies the requirement profile after hard filters and TCO analysis.

## Discovery principle

Discovery and verification are separate steps. A provider can be useful as a discovery lead without being suitable for a final recommendation.

## Data freshness

Record `observed_at` and source URLs for all volatile fields, especially:

- monthly price
- promotional price
- renewal price
- stock
- included transfer
- regional availability
- public IPv4 fees
- backup fees
- block storage fees
- managed control-plane fees

Recheck volatile data before any purchase or final recommendation.
