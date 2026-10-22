# Forum feedback 1 of 3

**To:** teammate post on quantum computing, cybersecurity and organizational resilience (ISO/IEC 27001 auditor perspective)
**Reuses from draft 19:** ranking #1 (Cybersecurity) and the Proxora / Ubuntu 26.10 lines from section 1. These are the parts to paint red in the Google Doc.
**Rule:** no closing question, so the teammate is not asked for extra work. No teammate names are stored in this repository; add the name only when pasting into the forum.

---

## Reply (ready to paste)

[NAME], your point about putting quantum readiness into governance and risk management really resonates with me, because cybersecurity is number one in the ranking of my own reflection. The fear of RSA breaking down under [Shor's algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm) is enough on its own to motivate quantum-ready checks worldwide, across companies and countries, starting with a Quantum-Readiness Roadmap, as [CISA, NSA and NIST recommend](https://cisa.gov/resources-tools/resources/quantum-readiness-migration-post-quantum-cryptography). Harvest now, decrypt later: the only threat that works backwards in time. That is exactly why it belongs in enterprise risk management and not only in an R&D budget.

The practical side is already moving. This October, Canonical released [Ubuntu 26.10 with post-quantum ready package signing](https://canonical.com/blog/canonical-releases-ubuntu-26-10-stonking-stingray) ([security details](https://canonical.com/blog/ubuntu-26-10-security)). As a reaction to that news, I built my repository [Proxora](https://github.com/qimono-repos/proxora) to sign its first quantum-ready Debian package with ML-DSA, the [NIST FIPS 204](https://csrc.nist.gov/pubs/fips/204/final) post-quantum signature standard. Blockchains are on the same path: [Algorand](https://algorand.co/technology/post-quantum) signs its State Proofs with Falcon.

Tools like these only matter when someone audits them, and your ISO/IEC 27001 lens is the piece that turns them into real organizational resilience. Thanks for bringing that perspective to the forum.

---

## Links used

- Shor's algorithm: https://en.wikipedia.org/wiki/Shor%27s_algorithm
- CISA, NSA, NIST, "Quantum-Readiness: Migration to Post-Quantum Cryptography" (Aug 2023): https://cisa.gov/resources-tools/resources/quantum-readiness-migration-post-quantum-cryptography
- Canonical, Ubuntu 26.10 release: https://canonical.com/blog/canonical-releases-ubuntu-26-10-stonking-stingray
- Canonical, Ubuntu 26.10 security: https://canonical.com/blog/ubuntu-26-10-security
- Proxora: https://github.com/qimono-repos/proxora
- NIST FIPS 204 (ML-DSA): https://csrc.nist.gov/pubs/fips/204/final
- Algorand post-quantum: https://algorand.co/technology/post-quantum
