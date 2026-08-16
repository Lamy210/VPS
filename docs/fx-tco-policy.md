# FX and TCO Normalization Policy

This repository preserves provider prices in their native currency. Cross-currency ranking is performed only in derived comparison output using an explicit FX snapshot.

## Principles

1. Never overwrite the provider's native price with a converted value.
2. Every conversion must record the observation date, rate source, base currency, quote currency, and exact rate used.
3. Do not compare a promotional monthly equivalent with an ordinary month-to-month price without preserving the contract distinction.
4. Taxes, setup fees, required IPv4, private networking, required storage, backup, load balancer, NAT, and unavoidable egress charges belong in TCO.
5. Optional features are not added unless the active requirement profile requires them.
6. If tax depends on buyer jurisdiction and the jurisdiction is not part of the requirement profile, preserve both pre-tax and tax-unknown states rather than inventing a final price.
7. FX snapshots expire for decision-making. Historical research remains reproducible because the original rate is retained.

## Required FX snapshot fields

```yaml
observed_at: 2026-08-16T00:00:00Z
base_currency: USD
source: null
rates:
  EUR: null
  GBP: null
  JPY: null
  SGD: null
  AUD: null
  PLN: null
  TRY: null
  ZAR: null
  BDT: null
  MYR: null
  IDR: null
  VND: null
  RSD: null
  KES: null
```

## Effective monthly TCO

For a requirement profile, calculate:

```text
effective_monthly_tco =
    recurring_compute
  + required_public_ipv4
  + required_private_network
  + required_block_storage
  + required_backup
  + required_snapshot_retention
  + required_load_balancer
  + required_nat_gateway
  + expected_required_egress_overage
  + amortized_required_setup_fee
  + applicable_required_tax
```

A provider's headline VM price is therefore not the final ranking value unless every required add-on is already included.

## Contract normalization

Keep at least these price classes separate:

- ordinary month-to-month price;
- hourly price with monthly cap;
- annual-prepay effective monthly price;
- multi-year-prepay effective monthly price;
- introductory promotional price;
- recurring promotional price;
- renewal price;
- one-time setup fee.

A profile may explicitly allow long prepayment. If it does not, an annualized or multi-year price cannot silently satisfy a monthly budget constraint.

## Ranking stability

When two candidates are close enough that a normal FX move could change their order, record them as effectively tied rather than presenting a false precise ranking.

Suggested default threshold:

```text
absolute TCO difference < 3% => price tie
```

The scoring system may still break ties using network, CPU allocation, automation, reliability, and region quality.

## Refresh policy

- Discovery records: no FX conversion required.
- Shortlisting: use an FX snapshot no older than 7 days.
- Purchase decision: use a snapshot captured on the decision date.
- Historical reports: retain the original snapshot used for the report.
