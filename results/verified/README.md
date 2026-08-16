# Verified Results

This directory stores resource data that has been checked against current official provider sources.

## Rules

- Official provider documentation, pricing pages, APIs, or official product catalogs are the primary source of truth.
- Aggregators and community posts may discover candidates, but they do not make a result verified.
- Unknown facts remain `unknown`; they are never silently treated as satisfied requirements.
- Promotional, annualized, and normal monthly prices are recorded separately.
- Regional pricing and limits are kept separate when they differ.
- A provider can be verified while a specific requirement-profile result remains `unknown`.
- A verified provider is not automatically a recommendation.

## Verification levels

- `B`: current price and core specifications verified from official sources.
- `A`: price plus material network, region, limit, and automation details verified.
- `A+`: A-level verification plus credible independent or controlled performance evidence.

## Batches

Verification is performed in batches so volatile prices can be rechecked without rewriting the discovery catalog.
