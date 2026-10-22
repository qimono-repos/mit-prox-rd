# The Tipping Point of Quantum Computing
## Draft Version 16

Brainstorm draft. No word limit yet. Built on draft 15 after reviewing the forum's overall sentiment (cautious, near-identical four-reason lists, everyone agreeing with Gil only "directionally"). This draft is deliberately not cautious: clear positions, no hedging. Throughout, "I" can be read as Qimono (TM), my entrepreneurial venture. Drafts 12 to 15 are untouched.

## Prompt checklist (must be covered in every draft)

- [x] 1. Networks: how ambitions differ across countries and why; impact on global relations since 2017; my own conviction on the role networks should play
- [x] 2. Investment: four reasons "the time for investment, all agree, is now"; which are most convincing
- [x] 3. Gil: three ways quantum software addresses his quote; argue whether to believe him
- [x] 4. Speak quantum: how the article presents it (corporate and government examples); examples from my own experience

---

### 1. The three-year promise

In 2004, the Bank of Austria and Vienna's city hall made the first quantum-encrypted bank transfer in history. Anton Zeilinger, the physicist whose lab made it possible, said he hoped "all problems of implementation will be solved within three years."[^1]

Jason Palmer, writing in *The Economist* thirteen years later, needs three words to deliver the verdict: "They were not."

Why not? The physics worked. The problem was everything around the physics. Quantum states cannot be copied, so a signal cannot simply be amplified along the way. Fibre links should be "no longer than about 200km." Every relay station in between is a point where the secret must be decrypted and trusted. Even the US Air Force's scientific advisers concluded that quantum key distribution had "little advantage over the best classical alternatives."

I call this **the three-year promise**: the gap between a physics experiment that works and a network that works. Once you see it, the map of who builds what makes sense.

China's network is "funded by the central government." It runs from Beijing to Shanghai via Jinan and Hefei, serves banks, the banking regulator and the Xinhua news agency, and the Micius satellite reaches for Urumqi, some 3,000 km away. South Korea funds a 250 km link between metro networks. Britain plans Bristol to Cambridge via London. Australia builds "a closed government network" in Canberra. In Europe, companies and standards lead: ID Quantique sells links to banks and data centres, and ETSI works so that "kit from multiple vendors can work together."

So why do ambitions differ? Ask who pays for the three-year promise. Where the state pays, the goal is sovereignty, and patience is a policy. Where companies pay, the goal is a product and a standard, and patience has a quarterly deadline.

Since 2017 that split has become geopolitics. On September 29, 2017, Micius relayed the first intercontinental quantum-secured video call, between Beijing and Vienna, some 7,600 km apart.[^8] By 2021 China had integrated satellite and fibre into a 4,600 km network serving more than 150 users, from banks to power-grid control centres.[^9] Europe answered with EuroQCI, backed by all 27 EU member states and aimed at a continent-wide network by 2030. But the West did not follow China's bet. The NSA does not support QKD for national security systems and prefers quantum-resistant encryption; France, Germany, the Netherlands and Sweden called QKD "not yet sufficiently mature" in 2024; and the UK's NCSC said in 2025 it would not support QKD for government or military use.[^10] The map split in two: China bets on physics, the US and Europe's security agencies bet on mathematics.

My conviction: the question "global effort or national shield?" is the wrong question. The real dilemma is feasibility. Each country will build its own shield, and the networks will grow organically, link by link, wherever they are feasible. Some classmates imagine a global quantum initiative, led by a body like the WHO. Countries will cooperate on what quantum computers discover, like medicines. They will never share the network that protects their secrets. Trust does not cross a relay station in a rival country.

And a safer internet does not have to wait for any quantum network. The article blends two different things: quantum communication (QKD, sharing secret keys), which exists today, and a quantum internet that shares entanglement between quantum computers, which is a longer-term goal. The safer internet comes from neither. Post-quantum signatures are not quantum protocols. They are classical mathematics designed to resist quantum computers, which is exactly why they must ship before quantum computers arrive. In my repository Proxora I am building my first quantum-ready Debian package, with releases signed using ML-DSA (NIST FIPS 204).[^2] Canonical's Ubuntu 26.10 delivers post-quantum ready package signing, replacing GnuPG with Sequoia PGP to verify APT repository signatures, and makes ML-KEM, ML-DSA and SLH-DSA available to users.[^3] Algorand has signed its State Proofs with Falcon, a post-quantum signature scheme, since 2022, and ran its first post-quantum mainnet transaction with Falcon-1024 in November 2025.[^4]

MIT's Seth Lloyd describes the promise of the quantum internet as "establishing trust while protecting privacy." The first part of that promise is arriving now, without new fibre at all.

### 2. A quantum computer for the price of a car

On October 20, 2026, I received an email from Shenzhen. SpinQ's sales team quoted me USD 12,000 for its 2-qubit Gemini Mini Pro and USD 17,000 for its 3-qubit Triangulum Mini, before import taxes.[^5]

Think about that for a second. A quantum computer, a real one with real qubits, for less than a new car.

That email changed how I read Palmer's sentence: "the time for investment, all agree, is now."[^1] The article gives four reasons: small machines can earn money before fully fault-tolerant computers exist; simulation of chemistry and materials pays off; security cannot wait, because data stolen today can be decrypted tomorrow; and nations need years to build people and industry.

I rank them in this order:

**1. Cybersecurity.** It is the only threat that works backwards in time: **harvest now, decrypt later**. The secret you send today is already exposed to the computer of tomorrow. The NSA announced its move to quantum-resistant cryptography in 2015, and Google tested a post-quantum scheme (New Hope) in Chrome. The answer is the one from section 1: post-quantum signatures, deployed now. Nothing else on the list has a deadline that has already passed.

**2. Small machines.** They **lower the entry barrier**. USD 12,000 is not a commercial advantage, it is a door: the most feasible way for a local startup like Qimono (TM) to start working with real quantum hardware. And small machines earn first where the problems are smallest and most valuable: financial services, and portfolio optimization above all. At Qimono (TM) we are building Porketo, a portfolio management system. Its newest piece is an MCP server (Model Context Protocol), so the automation can call Proxora's prediction processes, with the predictions and the portfolio optimization done in Qiskit. Porketo calling Proxora is the master plan.

**3. Simulation.** Bosch wants better batteries, Airbus lighter alloys, and Microsoft's Krysta Svore points to nitrogenase: understanding how bacteria fix nitrogen could save a large share of the natural gas burned today to make fertiliser. I put simulation third for one reason: optimizing a portfolio is a far smaller problem than simulating nature, so it pays first. But simulation is where the largest prize is, and robotics shows why. Elon Musk describes Tesla's cars as "semi-sentient robots on wheels."[^12] A self-driving car is a robot living inside reality, interacting with other cars, people and weather, so it is only as good as its model of that reality. Simulation is how we build that model, and quantum simulation is how we will make it exact, down to the chemistry of the battery that moves it.

**4. National capability.** Argentina proves it. UNAHUR installed the first quantum computer in the Argentine public university system, and CNEA is building an experimental fluxonium processor (FLUXOPRO). At the same time, 2025 was the lowest science and technology budget since at least 1972, at 0.167% of GDP, and 2026 is projected to go lower still, at 0.164%.[^6] I call this **Argentina-no-continuity**: capability takes years to build and one budget to break. That is why QaaS and hybrid setups matter so much here. When the hardware budget disappears, the cloud does not. I rank it last not because it matters least, but because it is the one reason a startup cannot fix by itself.

### 3. The race I rigged on purpose

In my repository Proxora there is a race that the quantum model always wins.

I rigged it.

On one side of the track runs a quantum regression. On the other side runs a classical linear regression, a model that can only draw a straight line. Any nonlinear model will beat a straight line. The quantum one wins, every time, and it proves nothing about quantum advantage.

So why build it? Because the point was never the winner. The point was the habit.

Former IBM vice president Dario Gil says: "The power of quantum computing is rediscovering all the problems that computers cannot solve, and having a path to solving them."[^1] Quantum software addresses that idea in three ways:

1. **Languages and cloud access.** IBM put a real quantum processor online in 2016. Software turns a lab experiment into something any developer can program. Today that is QaaS: hybrid setups where a classical program calls a quantum processor for one step.
2. **Algorithms that map real problems.** NIST's Quantum Algorithm Zoo already listed dozens of algorithm families. The hard work is translating chemistry, logistics or finance into a form a quantum circuit can attack.
3. **Better classical thinking.** 1QBit, a startup that sits between quantum experts and industry, found that framing problems the quantum way improved its classical algorithms too. "By taking the lens of how you would formulate an algorithm on a quantum computer you often find very good improvements on classical algorithms," says co-founder Landon Downs. "That's where lots of our successes come from."

That third way is the strangest and the most important. A quantum startup's biggest successes came from better classical code. Rewriting a problem for a quantum machine forces you to ask what the problem really is.

That is what my rigged race is for. Proxora keeps a classical and a quantum implementation in the same project, side by side. I call it **the side-by-side habit**, and it is how you learn to think in quantum. The next version replaces the straight line with a classical support vector machine against a quantum support vector machine: a fair fight, because both are kernel methods. And the referee is Big O, the new currency of the comparison. Not a stopwatch, but a way to ask whether quantum changes how cost grows with the size of the problem.

So should we believe Gil? Yes, fully. Read his sentence again: it has two halves, and both are already happening. "Rediscovering all the problems that computers cannot solve": that is exactly what 1QBit did, and what my side-by-side habit does every time I run it. You cannot write a problem for a quantum machine without rediscovering it. "Having a path to solving them": the path is the three ways above. Languages put the machine in every developer's hands, algorithms map the problems, and the quantum lens already improves the classical answers today. Gil did not promise that quantum computers will solve everything tomorrow. He promised a path. Software is that path, and we are already walking on it.

### 4. The car company that built a quantum sensor in 1964

Here is a fact that surprised me. The first SQUID, a superconducting quantum interference device and an exquisitely sensitive magnetic-field sensor, was developed in 1964 at Ford Research Laboratory.[^1] A car company. More than sixty years ago. Today SQUIDs sit inside MRI machines.

Quantum physics was never as far from industry as we like to think. What the article describes is the moment it stopped being a footnote. Intel works with Urenco and Air Liquide on isotopically pure silicon. Element Six, part of De Beers, engineers diamonds for sensors. ID Quantique sells quantum links to banks. Governments fund national networks in China, South Korea and the UK, and ETSI writes the standards. "Subjects that used to be mere footnotes to physics will rule," Palmer writes, "and engineers (and perhaps even consumers) will have to learn to speak quantum."

And the car comes back. Bosch's Michael Bolle describes autonomous vehicles where quantum sensors, quantum cryptography and quantum computing work together: sense the world, communicate securely, decide. Ford's 1964 sensor was a curiosity. Bosch's vehicle is a system. A robotics engineer of the next decade will need to speak all three dialects.

As a person born in South America I can give this personal experience in Argentina. UNAHUR's machine is an educational SpinQ: 3 qubits, NMR at room temperature, shared with other institutions and combined with cloud access to larger machines. [PLACEHOLDER: interview with Dr. Federico Holik, if it happens.] There will be more than one winning modality, and Argentina alone already touches three: NMR at UNAHUR, fluxonium at CNEA, and the topological approach I study through Microsoft's language. As founder of Qimono (TM), I live the same gap every day: the learning is open to anyone, the hardware is not.

My own way of learning to speak quantum lives in my repository qu. It has a full Q# section, Microsoft's quantum language, and through it I want to open the debate on Majorana. Microsoft bets on Majorana-based topological qubits: instead of correcting noise after the fact, it stores information non-locally, so local noise cannot touch it. That is topological protection. Majorana 1 arrived in February 2025 and was heavily disputed. On June 2, 2026, Microsoft presented Majorana 2, reporting a mean parity lifetime of about 20 seconds, with some runs reaching a minute, over 1,000 times longer than its earlier devices, and a topological gap that more than doubled.[^11] Parity lifetime is how long the qubit's fermion parity survives before a stray quasiparticle flips it. It is not the same as a full coherence time, and the paper is not peer-reviewed.

The right measuring stick is the one Google chose. With Willow, the goal was never a million qubits; it was going below the error-correction threshold, so that adding qubits makes errors smaller, not bigger.[^13] The race is how many gates you can run without errors. So the real test of twenty seconds of parity is the error rate per operation. One of my goals in this MIT xPRO course is to put Microsoft's Majorana claims to that test myself, with help from classmates and teachers at MIT.

Speaking a language is not the same as repeating what its teachers say. Speaking quantum, for me, means learning enough to ask the company that wrote the language: are you sure?

Zeilinger gave himself three years. It took far longer, and it is still not finished. That is the real lesson of the tipping point: it never arrives on the date the physicists promise. It arrives when enough engineers, in enough countries, have learned to speak the language.

---

## Footnotes

[^1]: Jason Palmer, "Here, there and everywhere: Quantum technology is beginning to come into its own," *The Economist*, Technology Quarterly, March 2017, Sections 3 to 6. Repo copy: `assets/Here_there_everywhere_Economist.md` (networks section: PDF pages 17 to 24).

[^2]: qimono-repos/proxora, `packaging/` (build-deb.sh, sign-release.sh, verify-release.sh). https://github.com/qimono-repos/proxora

[^3]: Canonical, "Canonical releases Ubuntu 26.10 Stonking Stingray," October 2026, https://canonical.com/blog/canonical-releases-ubuntu-26-10-stonking-stingray ; Canonical, "What's new in security for Ubuntu 26.10?", https://canonical.com/blog/ubuntu-26-10-security

[^4]: Algorand, "Post-Quantum Technology," https://algorand.co/technology/post-quantum ; first post-quantum mainnet transaction with Falcon-1024 on November 3, 2025 (reported by BSCN).

[^5]: Email from Rachel Lin, Overseas Sales Manager, Shenzhen SpinQ Technology, October 20, 2026. Includes hardware, software, teaching materials and DHL shipping; tax and duty not included. Informal price, not a formal quotation.

[^6]: Grupo EPC–ANPRES (2025 series and historical markers); CIICTI–ANPRES No. 32 (2026 projection). Charts: https://github.com/qimono-repos/mit-prox-rd/blob/trunk/essay/argentina-science-budget.svg and https://github.com/qimono-repos/mit-prox-rd/blob/trunk/essay/argentina-science-budget-2016-present.svg . Selected observations only; 2026 is a projection based on execution through September.

[^8]: Chinese Academy of Sciences, "Austrian and Chinese Academies of Sciences successfully conducted first inter-continental quantum video call," September 2017, https://english.cas.cn/newsroom/news/201709/t20170928_183577.shtml ; Austrian Academy of Sciences, "Secure quantum communication over 7600 kilometers," https://www.oeaw.ac.at/en/news-1/secure-quantum-communication-over-7600-kilometers

[^9]: Optica, "Quantum keys sent along fiber and into space," January 2021, https://optica-opn.org/home/newsroom/2021/january/quantum_keys_sent_along_fiber_and_into_space

[^10]: Marin Ivezic, "How countries differ on QKD," PostQuantum, December 2025, https://postquantum.com/post-quantum/qkd-countries-differ/ (summarises the NSA, NCSC and joint ANSSI/BSI/Dutch/Swedish positions; primary agency statements still worth linking directly).

[^11]: Microsoft, "Majorana 2, made more reliable with Microsoft Discovery agentic AI," June 2, 2026, https://news.microsoft.com/source/features/innovation/majorana-2-microsoft-discovery-agentic-ai/ ; The Quantum Insider, "Microsoft reports advances in Majorana 2 following debate over last year's topological claims," June 2, 2026, https://thequantuminsider.com/2026/06/02/microsoft-reports-advances-in-majorana-2-following-debate-over-last-years-topological-claims/

[^12]: Elon Musk, Tesla AI Day, August 2021: Tesla is "arguably the biggest robotics company in the world" because its cars are like "semi-sentient robots on wheels." [TO VERIFY: exact wording and source link.]

[^13]: Google, "Meet Willow, our state-of-the-art quantum chip," December 2024, https://blog.google/technology/research/google-willow-quantum-chip/

---

## Changes from v15

- Tone: deliberately committed, not cautious, in contrast with the forum's overall sentiment. Note that "I" can be read as Qimono (TM).
- Section 1: answered the classmate idea of a WHO-led global quantum initiative: cooperation on discoveries, never on the networks that protect secrets.
- Section 2: explicit ranking, numbered: 1 cybersecurity, 2 small machines (SpinQ price, portfolio optimization, Porketo + MCP calling Proxora, Qiskit), 3 simulation (optimization is smaller than simulating nature; robotics link via Musk's "robots on wheels"), 4 national capability (Argentina-no-continuity). Removed "All four convince me" and "promising, not proven".
- Section 3: full belief in Gil, argued half by half. Removed "Partly", "the map, not the destination" and the AlphaFold counterpoint (footnote 7 dropped).
- Section 4: "more than one winning modality" (NMR, fluxonium, topological) from the forum; Willow's below-threshold goal as the measuring stick for Majorana 2.
- Still open: Musk quote wording (footnote 12); Holik interview placeholder; primary links for the NSA, NCSC and ANSSI/BSI positions.
