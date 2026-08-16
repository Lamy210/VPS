# Research Methodology

This repository uses a requirement-driven process. Provider discovery is broad, but a provider or plan is only useful when it can satisfy an explicit requirement set.

## 1. Start from requirements

Create a requirement file from `requirements/template.yaml` and fill only the constraints that matter for the search.

Separate requirements into:

- hard constraints: a candidate must satisfy them;
- preferences: useful for ranking but not exclusion;
- unknowns: facts that still need verification.

Examples of hard constraints include minimum RAM, required region, private networking, a maximum monthly budget, or an API requirement.

## 2. Discover resource types before providers

Do not assume that a VPS is always the correct resource. Consider relevant alternatives such as:

- VPS / VDS
- cloud VM
- dedicated-resource VM or root server
- bare metal
- managed Kubernetes worker nodes
- container platforms
- managed PostgreSQL or other databases
- Redis-compatible managed caches
- block storage
- object storage
- load balancers and networking resources

The search should compare architectures as well as vendors when the requirements allow it.

## 3. Discover candidates broadly

Use multiple discovery paths because no single index is complete:

- provider pricing pages and product catalogs;
- VPS and cloud comparison indexes;
- local-language searches;
- regional cloud and sovereign cloud searches;
- IX/PeeringDB and ASN reverse discovery;
- OpenStack, CloudStack, OpenNebula, Proxmox, VirtFusion, and similar ecosystems;
- Terraform/OpenTofu and API ecosystems;
- community offer sites for discovery only.

Search vocabulary should include VPS, VDS, virtual server, cloud server, cloud VM, compute instance, root server, dedicated vCPU, regional cloud, sovereign cloud, private cloud, and equivalent local-language terms.

## 4. Normalize before comparing

Do not treat every brand string as a separate provider. Track:

- canonical provider name;
- parent company;
- official domain;
- brands and aliases;
- ASN when useful;
- actual regions and datacenters.

Keep reseller or white-label services identifiable when possible.

## 5. Verification levels

Use a simple confidence model:

- D — name discovered only;
- C — official site exists and relevant resource type is present;
- B — current price and core specifications verified from an official source;
- A — price, network, regions, limits, API/automation, company information, and important terms verified;
- A+ — A-level verification plus credible performance/network evidence or direct benchmark data.

Aggregator and community data should not produce an A-level result by themselves.

## 6. Comparable cost

Compare total monthly cost rather than headline VM price.

Include relevant items such as:

- compute;
- public IPv4;
- additional storage;
- private networking;
- load balancer;
- NAT gateway;
- snapshots and backups;
- traffic overages;
- managed Kubernetes control-plane charges;
- required support tier;
- setup fees amortized over the expected term.

Record promotional and renewal pricing separately.

## 7. Resource-specific metrics

### Compute

Compare RAM, vCPU count, shared/dedicated allocation, CPU family, disk capacity/type, transfer, port speed, and virtualization.

### Database-oriented compute

Give additional weight to predictable CPU allocation, storage latency, IOPS, durable backups, network latency, and private networking.

### Kubernetes and elastic compute

Check API provisioning, Terraform/OpenTofu support, cloud-init, hourly billing, load balancers, floating IPs, private networks, node-pool autoscaling, and Cluster Autoscaler compatibility.

### Network-heavy workloads

Check transfer accounting, ingress/egress rules, private traffic accounting, port limits, fair-use policies, ASN/peering, and regional routing.

## 8. Ranking

First remove candidates that fail hard constraints. Rank the remainder using the weights in the requirement file.

Always keep:

- the highest-scoring options;
- materially different alternatives;
- rejected candidates with short rejection reasons;
- uncertainty markers for facts that could not be verified.

## 9. Freshness

Prices, availability, regions, traffic limits, and product names change frequently. Every verified result should include a verification date and source. Recheck volatile facts before making a purchase or deployment decision.
