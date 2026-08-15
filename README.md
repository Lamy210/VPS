# Infrastructure Resource Finder

Public workspace for finding infrastructure resources from explicit technical and cost requirements.

The repository is not tied to any particular application or private architecture. It is intended to answer questions such as:

- What compute resources satisfy a given CPU, memory, storage, region, and budget requirement?
- Which VPS, VDS, cloud VM, managed Kubernetes, database, cache, object storage, or container service best fits those requirements?
- What are the trade-offs in monthly cost, traffic, private networking, automation, reliability, and future scaling?
- Which claims are verified by official sources, and when were they last checked?

## Workflow

1. Define requirements.
2. Discover possible resource types and providers broadly.
3. Filter candidates using hard constraints.
4. Verify price, specifications, regions, networking, and limitations against official sources.
5. Calculate comparable monthly TCO.
6. Rank candidates by the requested priorities.
7. Keep alternatives and rejected options with reasons so the search can be revisited later.

## Requirement dimensions

Typical inputs include:

- Region and latency constraints
- CPU count and shared/dedicated CPU preference
- Memory
- Local NVMe/block storage
- Monthly transfer and port speed
- IPv4/IPv6 requirements
- VPC/private LAN/private traffic requirements
- API, Terraform/OpenTofu, cloud-init, and hourly billing
- Container/Kubernetes support
- Backup, snapshot, floating IP, load balancer, and HA requirements
- Monthly and annual budget
- Scaling expectations

Requirements should describe capabilities rather than a private application or internal system.

## Public-repository rules

- Do not store credentials, tokens, private infrastructure details, customer data, confidential project information, or private service names.
- Keep requirement files generic and reusable.
- Use public, source-based facts only.
- Aggregators and community posts are discovery sources; important claims should be rechecked against official provider documentation or pricing.
- Record verification dates because pricing, stock, regions, limits, and product names change.

## Scope

Possible resource categories include compute, VPS/VDS, cloud VMs, dedicated-resource instances, managed Kubernetes, container platforms, managed databases, Redis-compatible caches, object storage, block storage, networking, load balancers, and backup resources.

The objective is not to maintain an exhaustive provider directory for its own sake. Provider and plan data exists to support requirement-driven resource selection.
