# VPS / Cloud Resource Research Workspace

A generic, public, requirement-driven workspace for finding and comparing infrastructure resources.

The goal is not to maintain a static list of “best VPS providers.” The workflow starts from explicit requirements, discovers relevant infrastructure products broadly, verifies current facts from primary sources, applies hard constraints, calculates comparable TCO, and only then benchmarks or ranks viable candidates.

## Scope

Relevant resource classes include:

- VPS / VDS / cloud VM
- dedicated-resource virtual machines and root servers
- bare metal
- managed Kubernetes
- container/serverless runtimes
- managed databases and caches
- object/block storage
- load balancers and related network resources

The repository is intentionally generic and public-safe. Do not add organization-specific infrastructure, credentials, customer information, private architecture, internal project names, or confidential requirements.

## Workflow

1. Define requirements from `requirements/template.yaml` or a reusable profile.
2. Discover candidates broadly using provider catalogs, regional/local-language search, IX/ASN sources, cloud ecosystems, and comparison indexes.
3. Normalize provider identity and aliases.
4. Verify current pricing, specifications, regions, networking, automation, contract terms, and important limitations from official sources.
5. Apply hard filters. An unknown hard field stays `unknown`; it is never silently treated as pass.
6. Calculate effective monthly TCO rather than comparing headline VM price only.
7. Generate derived shortlists without overwriting observed source data.
8. Benchmark only candidates that survive strict requirement filtering.

## Current repository structure

```text
requirements/
  template.yaml
  profiles/

data/
  provider-template.yaml
  provider-candidates.seed.yaml

docs/
  research-methodology.md
  discovery-sources.md
  search-taxonomy.md
  scoring.md
  provider-normalization.md
  verification-progress.md

results/
  template.yaml
  verified/
    batch-001.yaml ... batch-009.yaml
    followup-001.yaml
  derived/
    standard-compute-strict.yaml
    database-node-strict.yaml
    managed-kubernetes-strict.yaml
  benchmark/
    queue.yaml
```

## Current status

As of 2026-08-16:

- 9 official-source verification batches
- 81 unique provider records in those batches
- 1 targeted follow-up file for existing-provider unknowns
- strict derived shortlists for standard compute, database nodes, and managed Kubernetes
- 1 benchmark-ready resource in the current strict queue
- 0 measured benchmark results

See `docs/verification-progress.md` for the current queue and classification notes.

## Data quality principles

- Prefer official product/pricing/documentation sources for verification.
- Keep discovery leads separate from verified facts.
- Preserve promotional, annualized, renewal, tax, setup, and ordinary monthly prices separately.
- Preserve native currency; apply FX only through an explicit comparison policy.
- Keep marketing geography separate from actual datacenter geography.
- Distinguish shared, burstable, dedicated, and unknown CPU allocation.
- Do not treat snapshots as backups unless the profile allows that interpretation.
- Do not treat “unlimited” traffic as unconstrained without checking fair-use rules.
- Do not infer KVM, IPv4, private networking, API access, or SLA from a product label.
- Provider-advertised performance claims are not benchmark evidence.

## Confidence model

- **D** — discovery lead only
- **C** — official site/resource type confirmed
- **B** — current price/specification materially verified
- **A** — price, network/operations, material limits, and important terms verified
- **A+** — A-level verification plus credible independent or controlled benchmark evidence

A provider can be A-level verified and still fail a requirement profile.

## Benchmark policy

`results/benchmark/queue.yaml` separates resources that are ready to measure from resources still blocked by verification gaps. A future benchmark result must pin exact region, plan, OS image, kernel, tool versions, commands, repetition count, and raw-output location.

No benchmark result is implied merely because a provider appears in the queue.
