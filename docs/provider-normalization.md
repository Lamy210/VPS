# Provider Normalization

Discovery sources frequently contain duplicate brands, aliases, parent companies, regional brands, and historical names. Normalize identity before counting unique providers or comparing market coverage.

## Canonical identity keys

Use multiple signals together:

1. Official domain
2. Legal / parent company name
3. ASN ownership
4. Billing entity
5. Product branding
6. Acquisition or rebrand history

Do not merge providers only because their names look similar.

## Examples of relationships

Possible relationships include:

- exact alias
- regional brand
- product brand
- parent / subsidiary
- reseller
- acquired brand
- historical name
- unrelated name collision

Keep these relationships explicit instead of deleting useful aliases.

## Normalization workflow

1. Start from the discovery name.
2. Locate the official provider site.
3. Record the official domain.
4. Find company / legal identity information where available.
5. Record ASN information when the provider operates its own network.
6. Check whether another candidate uses the same domain, legal entity, or clearly documented brand relationship.
7. Select a stable `canonical_name`.
8. Preserve all discovered names in `aliases` or `brand_names`.
9. Mark unresolved collisions for manual review.

## Do not over-merge

The following are not enough by themselves to prove two providers are the same:

- same datacenter
- same upstream transit
- same WHMCS theme
- same virtualization platform
- similar plan specifications
- similar company name
- same country

## Resellers

A reseller can remain in the catalog when it provides materially different value such as:

- lower or different pricing
- different billing terms
- support layer
- regional payment methods
- additional network services
- managed operations

Record `reseller_of` when confirmed rather than automatically removing the entry.

## Count definitions

Use separate counts:

- `raw_candidates`: unnormalized discovery names
- `canonical_providers`: normalized providers / brands treated as independent buying choices
- `verified_providers`: canonical providers with current public resource offering confirmed
- `qualified_providers`: verified providers matching at least one active requirement profile

This prevents discovery-pool size from being confused with the number of viable providers.
