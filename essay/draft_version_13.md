# The tipping point of the Quantum Computing
## Draft Version 13

Brainstorm draft. No word limit yet. Built from draft 12 plus the live question-by-question session of 2026-10-21. Draft 12 is untouched.

## Prompt checklist (must be covered in every draft)

- [x] 1. Networks: how ambitions differ across countries and why; impact on global relations since 2017; my own conviction on the role networks should play
- [x] 2. Investment: four reasons "the time for investment, all agree, is now"; which are most convincing
- [x] 3. Gil: three ways quantum software addresses his quote; argue whether to believe him
- [x] 4. Speak quantum: how the article presents it (corporate and government examples); examples from my own experience

---

### 1. Quantum networks: feasibility, not a choice between world and nation

In Jason Palmer's 2017 *Economist* article, every country wants quantum networks, but not for the same reason.[^1] China's network is "funded by the central government": Beijing to Shanghai via Jinan and Hefei, with banks, the banking regulator and Xinhua as customers, and the Micius satellite aiming at Urumqi, some 3,000 km away. South Korea funds a 250 km link between metro networks, Britain plans Bristol to Cambridge via London, and Australia builds "a closed government network" in Canberra. In Europe, companies and standards lead: ID Quantique sells links to banks and data centres, and ETSI works so that "kit from multiple vendors can work together." The why is who drives it. Where the state leads, the goal is sovereignty. Where companies lead, the goal is a product and a standard.

Since 2017 that split became geopolitics. [TO VERIFY: China to Austria quantum-secured call via Micius, China's integrated ground and satellite network, EuroQCI, and the US preference for post-quantum cryptography over QKD.]

My conviction: the real dilemma is not a global effort versus national shields. It is feasibility. Palmer's own history shows it: in 2004 Anton Zeilinger hoped "all problems of implementation will be solved within three years." "They were not." Fibre links should be "no longer than about 200km", and quantum states cannot be copied, so every repeater is a security loophole. Even the US Air Force advisers found QKD had "little advantage over the best classical alternatives." Palmer leaves the role open: networks "may begin to look like a strategic must-have; if so, consumer applications are likely to proliferate." So each country will build its shield, and the networks will grow organically, link by link, where they are feasible.

I also separate two things the article blends. Quantum communication (QKD, sharing secret keys) exists today. A quantum internet that shares entanglement between quantum computers is a longer-term goal. And a safer internet does not have to wait for either. Post-quantum signatures are not quantum protocols: they are classical mathematics that resists quantum computers, which is exactly why they can and should ship before quantum computers arrive. In my repository Proxora I am building my first quantum-ready Debian package, with releases signed using ML-DSA (NIST FIPS 204).[^2] Canonical's Ubuntu 26.10 delivers post-quantum ready package signing, replacing GnuPG with Sequoia PGP to verify APT repository signatures, and makes ML-KEM, ML-DSA and SLH-DSA available to users.[^3] Algorand has signed its State Proofs with Falcon, a post-quantum signature scheme, since 2022, and ran its first post-quantum mainnet transaction with Falcon-1024 in November 2025.[^4] This is how we reach MIT's Seth Lloyd's goal for the quantum internet, "establishing trust while protecting privacy," today.

### 2. Why invest now? Four reasons from the article

Palmer gives four reasons why "the time for investment, all agree, is now":[^1]

1. **Small machines.** Useful work can start before fully fault-tolerant computers exist.
2. **Simulation pays off.** Bosch wants better batteries, Airbus better alloys, and Microsoft's Krysta Svore points to nitrogenase: understanding how bacteria fix nitrogen could save a large share of the natural gas burned today to make fertiliser.
3. **Security cannot wait.** Data stolen today can be decrypted later ("harvest now, decrypt later"). The NSA announced its move to quantum-resistant cryptography in 2015, and Google tested a post-quantum scheme (New Hope) in Chrome.
4. **National capability.** The people and the industry take years to build, and nobody wants to depend on another country's machines.

All four convince me, each for a concrete reason.

Security, because the threat works backwards in time, and the answer is the one from section 1: post-quantum signatures, deployed now, before the hardware.

Small machines, because they lower the entry barrier. SpinQ quoted me USD 12,000 for its 2-qubit Gemini Mini Pro and USD 17,000 for its 3-qubit Triangulum Mini, before import taxes.[^5] They are teaching machines, not commercial winners, but USD 12,000 is the most feasible way for a local startup like Qimono (TM) to start working with real quantum hardware.

National capability, because Argentina shows both sides. UNAHUR installed the first quantum computer in the Argentine public university system, and CNEA is building an experimental fluxonium processor (FLUXOPRO). At the same time, 2025 was the lowest science and technology budget since at least 1972, at 0.167% of GDP, and 2026 is projected to go lower still, at 0.164%.[^6] I call this Argentina-no-continuity: capability takes years to build and one budget to break. That is why QaaS and hybrid setups matter here.

Simulation is the most exciting, but the article never defines cleanly when a quantum machine actually beats a classical one. The evolving idea of what quantum computers are good for is still being written. Optimization, including portfolio optimization in financial services, sits in the same "promising, not proven" box.

### 3. Quantum software and Dario Gil's claim

Gil says: "The power of quantum computing is rediscovering all the problems that computers cannot solve, and having a path to solving them."[^1] Quantum software addresses that in three ways:

1. **Languages and cloud access.** IBM put a real quantum processor online in 2016. Software turns a lab experiment into something any developer can program. Today that is QaaS: hybrid setups where a classical program calls a quantum processor for one step.
2. **Algorithms that map real problems.** NIST's Quantum Algorithm Zoo already listed dozens of algorithm families. The hard work is translating chemistry, logistics or finance into a form a quantum circuit can attack.
3. **Better classical thinking.** 1QBit found that framing problems the quantum way improved its classical algorithms too.

The third way is my own experience. Proxora keeps a classical and a quantum implementation in the same project. Today it is linear regression against quantum regression, and the quantum one always wins, but on purpose: a nonlinear model beating a straight line proves nothing about quantum advantage. The point is the habit of building both side by side, which is how you learn to think in quantum. The next version will compare a classical support vector machine with a quantum support vector machine, a fair fight because both are kernel methods. Big O is the shared language for that comparison: not a stopwatch, but a way to ask whether quantum changes how cost grows with problem size.

Should we believe Gil? Partly. "Rediscovering the problems" is true: the field forces us to classify problems by how hard they really are. "A path to solving them" is too broad. For most hard problems there is no known quantum speedup, and AI competes on the same ground: AlphaFold predicted more than 200 million protein structures on classical hardware.[^7] I believe Gil about the map, not about the destination.

### 4. When physics becomes everyone's business

The article shows "speaking quantum" spreading from labs into industry and government.[^1] Intel works with Urenco and Air Liquide on isotopically pure silicon. Element Six, part of De Beers, engineers diamonds for sensors. ID Quantique sells quantum links to banks. Ford built SQUID sensors back in 1964. Governments fund national networks in China, South Korea and the UK, and ETSI writes the standards.

The strongest example for me is robotics. Bosch's Michael Bolle describes autonomous vehicles where quantum sensors, quantum cryptography and quantum computing work together: sense the world, communicate securely, decide. A robot engineer of the next decade will need all three.

As a person born in South America I can give this personal experience in Argentina. UNAHUR's machine is an educational SpinQ: 3 qubits, NMR at room temperature, shared with other institutions and combined with cloud access to larger machines. [PLACEHOLDER: interview with Dr. Federico Holik, if it happens.] As founder of Qimono (TM), I live the same gap: the learning is open to anyone, the hardware is not.

My own way of learning to speak quantum is in my repository qu. It has a full Q# section, Microsoft's quantum language, and through it I want to open the debate on Majorana. Microsoft bets on Majorana-based topological qubits, announced its Majorana 1 chip in February 2025, and physicists still dispute the evidence. One of my goals in this MIT xPRO course is to be able to put Microsoft's Majorana claims under test myself, with help from classmates and teachers at MIT. Speaking quantum, for me, means more than using a company's language: it means learning enough to question it.

---

## Footnotes

[^1]: Jason Palmer, "Here, there and everywhere: Quantum technology is beginning to come into its own," *The Economist*, Technology Quarterly, March 2017, Sections 3 to 6. Repo copy: `assets/Here_there_everywhere_Economist.md` (networks section: PDF pages 17 to 24).

[^2]: qimono-repos/proxora, `packaging/` (build-deb.sh, sign-release.sh, verify-release.sh). https://github.com/qimono-repos/proxora

[^3]: Canonical, "Canonical releases Ubuntu 26.10 Stonking Stingray," October 2026, https://canonical.com/blog/canonical-releases-ubuntu-26-10-stonking-stingray ; Canonical, "What's new in security for Ubuntu 26.10?", https://canonical.com/blog/ubuntu-26-10-security

[^4]: Algorand, "Post-Quantum Technology," https://algorand.co/technology/post-quantum ; first post-quantum mainnet transaction with Falcon-1024 on November 3, 2025 (reported by BSCN).

[^5]: Email from Rachel Lin, Overseas Sales Manager, Shenzhen SpinQ Technology, October 20, 2026. Includes hardware, software, teaching materials and DHL shipping; tax and duty not included. Informal price, not a formal quotation.

[^6]: Grupo EPC–ANPRES (2025 series and historical markers); CIICTI–ANPRES No. 32 (2026 projection). Charts: https://github.com/qimono-repos/mit-prox-rd/blob/trunk/essay/argentina-science-budget.svg and https://github.com/qimono-repos/mit-prox-rd/blob/trunk/essay/argentina-science-budget-2016-present.svg . Selected observations only; 2026 is a projection based on execution through September.

[^7]: AlphaFold Protein Structure Database, EMBL-EBI and Google DeepMind.

---

## Changes from v12

- Added the prompt checklist at the top.
- Section 1: conviction rewritten. The dilemma is feasibility, not global versus national; organic growth. Article quotes now verified against the repo copy (Zeilinger, 200 km, Air Force board, "may... if so", ETSI, Lloyd). Quantum communication separated from quantum internet. Post-quantum signatures as the safer internet today: Proxora (ML-DSA), Ubuntu 26.10 (source verified), Algorand (Falcon), linked to Seth Lloyd.
- Section 2: all four reasons convincing. Small machines reframed as "lower the entry barrier" with the SpinQ prices. National capability linked to Argentina and the 1972 to 2026 budget chart.
- Section 3: full Gil quote. Proxora side-by-side classical and quantum as own experience; SVM versus QSVM as next step.
- Section 4: qu repository, Q#, and the Majorana debate as a personal course goal.
- Still to verify: post-2017 network events; Microsoft Majorana dates and the state of the dispute.
