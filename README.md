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

This repository provides a public reference implementation of the ECZ-ID **Passport Carry-Card v1.0** interoperability profile.

Reference files:

- [Public interoperability guide](docs/PASSPORT_CARRY_CARD.md)
- [JSON Schema](passport-card.schema.json)
- [Example Card](.eczid/passport-card.example.json)
- [Validator](scripts/validate_passport_card.py)

Validate the example:

```bash
python scripts/validate_passport_card.py .eczid/passport-card.example.json --allow-example
```

The Carry-Card carries stable identity pointers. Current proof must be re-checked through the canonical Resolver.

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

The Parent identifies the accountable human or organisation context. The API Passport identifies the specific API surface beneath it.

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
