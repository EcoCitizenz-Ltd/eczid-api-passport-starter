# ECZ-ID API Passport Starter

![ECZ-ID API Passport identity, authority and evidence visual](https://raw.githubusercontent.com/EcoCitizenz-Ltd/.github/main/assets/repository-visuals/eczid-api-passport-starter.jpg)

## Give an API a free, resolvable identity that other systems can re-check.

APIs increasingly act as machine-to-machine trust boundaries. An endpoint alone does not tell a relying party who operates it, which organisation stands behind it, what relationships are asserted, where public evidence can be reviewed, or whether that evidence is still current.

The **API Passport is a free ECZ-ID child Passport**. Paid ECZ-ID products add operating capacity, monitoring, evidence, assurance and specialist services; they do not make the API identity itself paid.

### Start free

[Get a free API Passport](https://trustops.ecocitizenz.com/start?utm_source=github&utm_medium=repository&utm_campaign=api-passport&utm_content=get-free-passport)

[Explore the ECZ-ID Developer Gateway](https://developers.ecocitizenz.com?utm_source=github&utm_medium=repository&utm_campaign=api-passport&utm_content=developers)

[View live Resolver proof](https://resolver.ecocitizenz.org/passport/ECZ-GB-RBS1NW)

---

## Passport Carry-Card

This repository implements the ECZ-ID **Passport Carry-Card v1.0** reference pattern so an ECZ-ID can travel through repositories, packages, SDKs, services, CI and marketplaces without creating another source of truth.

The Card carries stable pointers such as the ECZ-ID, Passport family and Resolver URL. Current lifecycle state, assurance, evidence and authority must be re-checked through canonical ECZ-ID proof.

Reference files:

- [Carry-Card specification](docs/PASSPORT_CARRY_CARD.md)
- [JSON Schema](passport-card.schema.json)
- [Example Card](.eczid/passport-card.example.json)
- [Zero-dependency validator](scripts/validate_passport_card.py)

Validate the example:

```bash
python scripts/validate_passport_card.py .eczid/passport-card.example.json --allow-example
```

The frictionless loop is:

```text
use free starter
  -> get free API Passport
  -> return and configure Carry-Card
  -> verify through Resolver
  -> display/share Resolver-linked proof
  -> next developer or machine encounters ECZ-ID
  -> next relevant free Passport adoption
```

No telemetry is required for that adoption loop.

---

## API identity review checklist

Before relying on an important API integration, record:

- [ ] API/operator name
- [ ] operator organisation
- [ ] production endpoint
- [ ] environment or deployment boundary
- [ ] responsible owner
- [ ] authentication model
- [ ] authorization model
- [ ] linked machine or agent identities
- [ ] public evidence location
- [ ] evidence freshness / last review
- [ ] lifecycle or revocation path
- [ ] incident contact route

The purpose is not to turn an API description into a security guarantee. It is to make identity, authority and evidence easier to resolve and review.

---

## Parent and child identity

The Parent identifies the accountable human or organisation context. The API Passport identifies the specific API surface beneath it. A relying party can review both without confusing organisational identity with the machine surface itself.

The ECZ-ID launch model uses seven free child Passport families:

- Agent
- MCP
- Plugin
- API
- IoT
- SDK
- Service & Workload

---

## Resolver-first review

A relying party should be able to:

1. receive an ECZ-ID reference
2. resolve current public proof
3. inspect what is actually asserted
4. check freshness and lifecycle state
5. apply its own local policy

[Open the ECZ-ID Resolver](https://resolver.ecocitizenz.org/passport/ECZ-GB-RBS1NW)

Resolver evidence is information for review. It does not replace the relying party's security, procurement or authorization decision.

---

## Interoperability

Carry-Card adapters may point from package metadata, OCI/container labels, CI output, marketplace descriptions, websites/services and compatible Agent/MCP manifests.

Adapters should point to the Card or Resolver rather than fork ECZ-ID semantics.

Machine fields such as ECZ-IDs, schema keys, API fields, hashes, signatures, SKUs, ReasonCodes and protocol tokens remain canonical and language-neutral. Human-facing help and documentation can be localized separately.
