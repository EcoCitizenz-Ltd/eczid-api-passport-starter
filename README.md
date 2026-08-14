# ECZ-ID API Passport Starter

![ECZ-ID API Passport identity, authority and evidence visual](https://raw.githubusercontent.com/EcoCitizenz-Ltd/.github/main/assets/repository-visuals/eczid-api-passport-starter.jpg)

## Give APIs an identity and evidence surface that relying systems can re-check.

APIs increasingly act as machine-to-machine trust boundaries.

An endpoint alone does not tell a relying party:

- who operates it
- which organisation stands behind it
- what authority relationship is being asserted
- where supporting evidence can be reviewed
- whether that evidence is still current

This repository is a practical starting point for thinking about resolvable API identity.

### Start here

[Explore the ECZ-ID Developer Gateway](https://developers.ecocitizenz.com?utm_source=github&utm_medium=repository&utm_campaign=api-passport&utm_content=developers)

[Start with ECZ-ID / TrustOps](https://trustops.ecocitizenz.com/start?utm_source=github&utm_medium=repository&utm_campaign=api-passport&utm_content=start)

[View live Resolver proof](https://resolver.ecocitizenz.org/passport/ECZ-GB-RBS1NW)

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

The purpose is not to turn an API description into a security guarantee.

The purpose is to make identity, authority and evidence easier to resolve and review.

---

## Parent and child identity

A useful machine-identity model separates the organisation that operates a service from the individual API, agent, software surface or machine that acts beneath it.

ECZ-ID uses parent/child identity relationships so a relying party can review the organisational anchor and the specific machine surface independently.

---

## Resolver-first review

A relying party should be able to:

1. receive an ECZ-ID reference
2. resolve current public evidence
3. inspect what is actually asserted
4. check freshness and lifecycle state
5. apply its own local policy

[Open the ECZ-ID Resolver](https://resolver.ecocitizenz.org/passport/ECZ-GB-RBS1NW)

---

## Developer starting points

Use the ECZ-ID Developer Gateway for current developer resources and product paths.

[Developer Gateway](https://developers.ecocitizenz.com?utm_source=github&utm_medium=repository&utm_campaign=api-passport&utm_content=gateway)

[Start / obtain ECZ-ID](https://trustops.ecocitizenz.com/start?utm_source=github&utm_medium=repository&utm_campaign=api-passport&utm_content=trustops)

---

## Public proof example

**ECZ-ID public identity evidence - ECZ-GB-RBS1NW**
[View current public identity and evidence](https://resolver.ecocitizenz.org/passport/ECZ-GB-RBS1NW)

Resolver evidence is information for review. It does not replace the relying party's security, procurement or authorization decision.