# Quantum Computing: Big Investment, Bigger Questions
## Draft Version 12

Brainstorm draft. No word limit yet. Changes from v11 are listed at the bottom.

### 1. Quantum networks and global relations

In Jason Palmer's 2017 *Economist* article, every country wants quantum networks, but not for the same reason. China builds infrastructure: the Beijing to Shanghai fibre link and the Micius satellite are state projects at continental scale. South Korea and the UK (Bristol to Cambridge) build national testbeds. Europe works through standards, with ETSI defining how quantum key distribution should behave. Switzerland's ID Quantique already sold links to banks. The difference comes from who drives the project. Where the state leads, the goal is sovereignty and secure government channels. Where companies and research programmes lead, the goal is a product and a standard.[^1]

Since 2017 that split has turned into geopolitics. China connected its ground network to Micius and held a quantum-secured video call with Austria. Europe answered with its own quantum communication infrastructure programme. The United States took a different road: its security agencies prefer post-quantum cryptography, mathematics that runs on ordinary computers, over quantum key distribution hardware. So the world is not only racing; it is choosing two different answers to the same threat. [TO VERIFY: dates and figures for the China to Austria call, the China integrated network, EuroQCI and the NSA position.]

My conviction: quantum networks should be trusted infrastructure for the few links that really need them (government, critical infrastructure, financial services, large science collaborations) and should complement classical networks, not replace them. And they need shared standards. A secure channel that only works between allies is a wall, not a network.

### 2. Why invest now? Four reasons from the article

Palmer gives four reasons why "the time for investment, all agree, is now":[^1]

1. **Small machines can earn money early.** Useful work should start before fully fault-tolerant computers exist, so companies that are already in the field collect revenue and experience first.
2. **Simulation pays off.** Bosch wants post-lithium batteries, Airbus better alloys, and Microsoft's Krysta Svore points to nitrogenase: understanding how bacteria fix nitrogen could save a large share of the natural gas burned today to make fertiliser.
3. **Security cannot wait.** Data stolen today can be decrypted later ("harvest now, decrypt later"). The NSA announced its move to quantum-resistant cryptography in 2015, and Google already tested a post-quantum scheme (New Hope) in Chrome.
4. **National capability.** Governments fund quantum work because the people and the industry take years to build, and nobody wants to depend on another country's machines.

The most convincing for me are security and capability. Security, because the threat works backwards in time: a message encrypted today is only as safe as the strongest computer of the next 20 years. Capability, because expertise cannot be bought overnight when the hardware matures. Simulation is the most exciting but the least certain, and the article never defines cleanly when a quantum machine actually beats a classical one. The evolving idea of what quantum computers are good for is still being written. Optimization, including portfolio optimization in financial services, sits in the same "promising, not proven" box. A useful question to keep asking: is this a solution in search of a problem?

### 3. Quantum software and Dario Gil's claim

Gil says quantum computing "is rediscovering all the problems that computers cannot solve, and having a path to solving them." Quantum software addresses that in three ways:

1. **Languages and cloud access.** IBM put a real quantum processor online in 2016. Software turns a lab experiment into something any developer can program. Today that is QaaS: hybrid setups where a classical program calls a quantum processor for one step.
2. **Algorithms that map real problems.** NIST's Quantum Algorithm Zoo already listed dozens of algorithm families when the article was written. The hard work is translating chemistry, logistics or finance into a form a quantum circuit can attack.
3. **Better classical thinking.** 1QBit found that framing problems the quantum way improved its classical algorithms too. Quantum software teaches us to ask new questions even before the hardware is ready.

This is where Big O becomes the new currency. It is not a stopwatch, but it is the shared language to ask whether a quantum algorithm changes how cost grows with problem size.

Should we believe Gil? Partly. "Rediscovering the problems" is true: the field forces us to classify problems by how hard they really are. "A path to solving them" is too broad. For most hard problems there is no known quantum speedup. AI also competes on the same ground: AlphaFold predicted more than 200 million protein structures on classical hardware, a problem many expected quantum computers to own.[^4] So I believe Gil about the map, not about the destination.

### 4. When physics becomes everyone's business

The article shows "speaking quantum" spreading from labs into industry and the state.[^1] Intel works with Urenco and Air Liquide on isotopically pure silicon for qubits. Element Six, part of De Beers, engineers diamonds with nitrogen vacancies for sensors. ID Quantique sells quantum links to banks. Ford was building SQUID sensors back in 1964. Governments fund national networks in China, South Korea and the UK, and ETSI writes the standards.

For me the strongest example is robotics. Bosch's Michael Bolle describes autonomous vehicles where quantum sensors, quantum cryptography and quantum computing work together: sense the world, communicate securely, decide. A robot engineer of the next decade will need to understand all three.

A current example from my own field: Ubuntu 26.10 introduced post-quantum package signing in October 2026.[^5] This is not a quantum computer running Linux. It is ordinary software changing now because of a future quantum threat. NIST standardized the signature schemes (ML-DSA and SLH-DSA) in 2024.[^6] Speaking quantum does not mean every engineer becomes a physicist. It means knowing where the risk is and which standard to pick. [TO VERIFY: Ubuntu 26.10 claims and sources.]

As a person born in South America I can give this personal experience in Argentina. UNAHUR (Universidad Nacional de Hurlingham) installed the first quantum computer in the Argentine public university system: an educational SpinQ, 3 qubits, NMR at room temperature, shared with other institutions and combined with cloud access to larger machines. A 3-qubit SpinQ teaching machine costs about USD 17,000 before import taxes, according to SpinQ's sales team; the 2-qubit model costs about USD 12,000.[^7] [PLACEHOLDER: interview with Dr. Federico Holik, if it happens.] CNEA is building an experimental fluxonium processor (FLUXOPRO), while the national science budget faces deep cuts.[^3] I call this Argentina-no-continuity: real talent and real projects, unstable support. That is why QaaS and hybrid setups matter here; they let a country learn to speak quantum before it can afford to build. As founder of Qimono (TM), I live this gap every day: the learning is open to anyone, the hardware is not.

---

## Footnotes

[^1]: Jason Palmer, "Here, there and everywhere: Quantum technology is beginning to come into its own," *The Economist*, Technology Quarterly, March 2017, Sections 3 to 6. Repo copy: `assets/Here_there_everywhere_Economist.md`.

[^3]: CNEA, "Tecnologías cuánticas: tres proyectos de la CNEA obtuvieron financiamiento," 2026; Grupo EPC, ANPRES No. 19, August 2025; CIICTI, "La ciencia argentina se queda sin recursos para funcionar." Same sources as v11.

[^4]: AlphaFold Protein Structure Database, EMBL-EBI and Google DeepMind.

[^5]: Canonical, "Canonical releases Ubuntu 26.10," October 2026. Same source as v11, still to verify.

[^6]: NIST FIPS 204 and FIPS 205, August 13, 2024.

[^7]: Email from Rachel Lin, Overseas Sales Manager, Shenzhen SpinQ Technology, to the author, October 20, 2026: "Gemini Mini Pro (2-qubit): USD12,000, Triangulum Mini (3-qubit): USD17,000." Includes hardware, software, teaching materials and DHL shipping; tax and duty not included. Informal price, not a formal quotation. The exact model UNAHUR owns is not confirmed.

---

## Changes from v11

- Section 2: the four reasons now come from Palmer's text, not McKinsey. Footnote 2 removed. Security became reason 3 instead of a side note.
- Section 1: added the "why" (state-led versus company-led) and the "since 2017" geopolitics; facts flagged to verify.
- Section 3: the three ways use the article's own examples (IBM cloud, Algorithm Zoo, 1QBit). Clearer position on Gil: believe the map, not the destination.
- Section 4: added the article's corporate examples, the Bosch robotics hook, UNAHUR, the SpinQ price (first-hand email quote), and Qimono (TM).
- Kept: required South America sentence, QaaS, hybrid setups, financial services, the evolving idea, portfolio optimization, Argentina-no-continuity, Big O as new currency, quantum advantage not cleanly defined in the article.
