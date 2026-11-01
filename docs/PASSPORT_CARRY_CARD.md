# ECZ-ID Passport Carry-Card v1.0

This repository includes the public interoperability profile for the ECZ-ID Passport Carry-Card.

The Carry-Card is a small pointer envelope that lets software carry an ECZ-ID reference without copying current Resolver state into the distribution asset.

## Required fields

- `schema`: `eczid.passport-carry-card`
- `schema_version`: `1.0`
- `ecz_id`: current public parent or child ECZ-ID reference
- `passport_family`: `parent`, `agent`, `mcp`, `plugin`, `api`, `iot`, `sdk`, or `service-workload`
- `resolver_url`: canonical HTTPS human Resolver URL

Optional fields are defined by the checked-in JSON Schema.

## Current identifier contract

Parent ECZ-ID syntax:

```text
ECZ-CC-XXXXXX
```

Current child syntax:

```text
{parent_ecz_id}::{CURRENT_TYPE_CODE}-XXXXXX
```

The seven current free machine Passport family type codes are:

| `passport_family` | Child type code |
| --- | --- |
| `agent` | `AGENT_PASSPORT` |
| `mcp` | `MCP_PASSPORT` |
| `plugin` | `PLUGIN_PASSPORT` |
| `api` | `API_PASSPORT` |
| `iot` | `IOT_DEVICE` |
| `sdk` | `SDK_PASSPORT` |
| `service-workload` | `SERVICE_WORKLOAD_PASSPORT` |

Historical catalogue-era codes are not current child Passport family identifiers.

A child identifier carries its parent directly. If `parent_ecz_id` is also present in a Carry-Card, it must match that encoded parent.

## Canonical proof pointers

URL-encode the complete ECZ-ID before placing it in a path.

Human Resolver:

```text
https://resolver.ecocitizenz.org/p/{URL-encoded ecz_id}
```

Machine proof document:

```text
https://api.ecocitizenz.com/api/p/{URL-encoded ecz_id}.json
```

A Carry-Card may include `machine_proof_url`. When present, the validator requires the canonical machine proof route above.

## Repository convention

Use:

```text
.eczid/passport-card.json
```

Reference fixtures may use:

```text
.eczid/passport-card.example.json
```

Validate a production card locally:

```bash
python scripts/validate_passport_card.py .eczid/passport-card.json
```

Validate the checked-in example fixture:

```bash
python scripts/validate_passport_card.py .eczid/passport-card.example.json --allow-example
```

A fixture marked `extensions.example_fixture=true` is deliberately non-issued and is rejected unless `--allow-example` is explicitly supplied. Never publish an example fixture as if it were live proof.

## Verification rule

A Carry-Card is not proof by itself.

Current lifecycle state, assurance, evidence, bindings and authority must be checked through the canonical ECZ-ID Resolver or approved machine-readable proof endpoint when a relying decision is made.

A 404/no record is absence of public ECZ-ID proof, not a safety or trust verdict. An unreadable Resolver is unreadable; it must not be silently converted into absence.

## Public safety rules

- Do not put secrets or private environment data in a public card.
- Production URLs use HTTPS.
- Treat optional extension content as untrusted input.
- The card does not create VERIFIED, ASSURED, BOUND or ENFORCED state.
- Possession of a card does not mean safe, compliant, certified or approved.
- A Resolver-linked badge or reference is a pointer to proof, not proof by itself.
- Parent strength applies to the accountable organisation; it is not inherited by a child machine Passport.

## Versioning

v1.x may add optional fields without breaking the required core.

Corrections that make fixtures/validators conform to the already-current ECZ-ID identifier and Resolver contract do not create a new proof meaning. A breaking required-field or Carry-Card semantic change requires a new major schema version.
