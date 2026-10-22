# The Tipping Point of Quantum Computing
## Draft Version 14

Brainstorm draft. No word limit yet. Same content as draft 13, rewritten in a Gladwell-inspired narrative style blended with my own voice: start with a mystery, investigate it with evidence, let the thesis emerge. Drafts 12 and 13 are untouched.

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

I call this **the three-year promise**: the gap between a physics experiment that works and a network that works. And once you see it, the map of who builds what starts to make sense.

China's network is "funded by the central government." It runs from Beijing to Shanghai via Jinan and Hefei, serves banks, the banking regulator and the Xinhua news agency, and the Micius satellite reaches for Urumqi, some 3,000 km away. South Korea funds a 250 km link between metro networks. Britain plans Bristol to Cambridge via London. Australia builds "a closed government network" in Canberra. In Europe, companies and standards lead: ID Quantique sells links to banks and data centres, and ETSI works so that "kit from multiple vendors can work together."

So why do ambitions differ? Ask who pays for the three-year promise. Where the state pays, the goal is sovereignty, and patience is a policy. Where companies pay, the goal is a product and a standard, and patience has a quarterly deadline.

Since 2017 that split has become geopolitics. [TO VERIFY: China to Austria quantum-secured call via Micius, China's integrated ground and satellite network, EuroQCI, and the US preference for post-quantum cryptography over QKD.]

Which brings me to my conviction. The usual question is: should quantum networks be a global effort or a national shield? I think that is the wrong question. The real dilemma is feasibility. Palmer himself leaves the door open: networks "may begin to look like a strategic must-have; if so, consumer applications are likely to proliferate." May. If so. Each country will build its shield, and the networks will grow organically, link by link, wherever they are feasible.

But here is the twist that the article blends away. Quantum communication (QKD, sharing secret keys) exists today. A quantum internet that shares entanglement between quantum computers is a longer-term goal. And a safer internet does not have to wait for either.

Post-quantum signatures are not quantum protocols. They are classical mathematics designed to resist quantum computers, which is exactly why they can, and should, ship before quantum computers arrive. In my repository Proxora I am building my first quantum-ready Debian package, with releases signed using ML-DSA (NIST FIPS 204).[^2] Canonical's Ubuntu 26.10 delivers post-quantum ready package signing, replacing GnuPG with Sequoia PGP to verify APT repository signatures, and makes ML-KEM, ML-DSA and SLH-DSA available to users.[^3] Algorand has signed its State Proofs with Falcon, a post-quantum signature scheme, since 2022, and ran its first post-quantum mainnet transaction with Falcon-1024 in November 2025.[^4]

MIT's Seth Lloyd describes the promise of the quantum internet as "establishing trust while protecting privacy." The irony is that the first part of that promise is arriving without new fibre at all.

### 2. A quantum computer for the price of a car

On October 20, 2026, I received an email from Shenzhen. SpinQ's sales team quoted me USD 12,000 for its 2-qubit Gemini Mini Pro and USD 17,000 for its 3-qubit Triangulum Mini, before import taxes.[^5]

Think about that for a second. A quantum computer, a real one with real qubits, for less than a new car.

It is not a powerful machine. It is a teaching machine. But that email changed how I read Palmer's sentence: "the time for investment, all agree, is now."[^1] Why now, if the machines are still this small? The article gives four reasons:

1. **Small machines.** Useful work can start before fully fault-tolerant computers exist.
2. **Simulation pays off.** Bosch wants better batteries, Airbus better alloys, and Microsoft's Krysta Svore points to nitrogenase: understanding how bacteria fix nitrogen could save a large share of the natural gas burned today to make fertiliser.
3. **Security cannot wait.** Data stolen today can be decrypted tomorrow: **harvest now, decrypt later**. The NSA announced its move to quantum-resistant cryptography in 2015, and Google tested a post-quantum scheme (New Hope) in Chrome.
4. **National capability.** The people and the industry take years to build, and nobody wants to depend on another country's machines.

All four convince me, each for a concrete reason.

Security, because it is the only threat that works backwards in time. The secret you send today is already exposed to the computer of 2035. The answer is the one from section 1: post-quantum signatures, deployed now.

Small machines, because they **lower the entry barrier**. USD 12,000 is not a commercial advantage. It is a door. It is the most feasible way for a local startup like Qimono (TM) to start working with real quantum hardware.

National capability, because Argentina shows both sides of the coin. UNAHUR installed the first quantum computer in the Argentine public university system, and CNEA is building an experimental fluxonium processor (FLUXOPRO). At the same time, 2025 was the lowest science and technology budget since at least 1972, at 0.167% of GDP, and 2026 is projected to go lower still, at 0.164%.[^6]

I call this **Argentina-no-continuity**: capability takes years to build and one budget to break. That is why QaaS and hybrid setups matter so much here. When the hardware budget disappears, the cloud does not.

And simulation? It is the most exciting reason, and the least defined. The article never says cleanly when a quantum machine actually beats a classical one. The evolving idea of what quantum computers are good for is still being written. Optimization, including portfolio optimization in financial services, sits in the same box, the one labelled "promising, not proven."

### 3. The race I rigged on purpose

In my repository Proxora there is a race that the quantum model always wins.

I rigged it.

On one side of the track runs a quantum regression. On the other side runs a classical linear regression, a model that can only draw a straight line. Any nonlinear model will beat a straight line. The quantum one wins, every time, and it proves nothing about quantum advantage.

So why build it? Because the point was never the winner. The point was the habit.

Former IBM vice president Dario Gil says: "The power of quantum computing is rediscovering all the problems that computers cannot solve, and having a path to solving them."[^1] Quantum software addresses that idea in three ways:

1. **Languages and cloud access.** IBM put a real quantum processor online in 2016. Software turns a lab experiment into something any developer can program. Today that is QaaS: hybrid setups where a classical program calls a quantum processor for one step.
2. **Algorithms that map real problems.** NIST's Quantum Algorithm Zoo already listed dozens of algorithm families. The hard work is translating chemistry, logistics or finance into a form a quantum circuit can attack.
3. **Better classical thinking.** 1QBit, a startup that sits between quantum experts and industry, found that framing problems the quantum way improved its classical algorithms too. "By taking the lens of how you would formulate an algorithm on a quantum computer you often find very good improvements on classical algorithms," says co-founder Landon Downs. "That's where lots of our successes come from."

That third way is the strangest and, to me, the most important. A quantum startup's biggest successes came from better classical code. Why? Because rewriting a problem for a quantum machine forces you to ask what the problem really is.

That is what my rigged race is for. Proxora keeps a classical and a quantum implementation in the same project, side by side. I call it **the side-by-side habit**, and it is how you learn to think in quantum. The next version will replace the straight line with a classical support vector machine against a quantum support vector machine: a fair fight, because both are kernel methods. And the referee is Big O, the new currency of the comparison. Not a stopwatch, but a way to ask whether quantum changes how cost grows with the size of the problem.

So should we believe Gil? Partly. "Rediscovering the problems" is true: the field forces us to classify problems by how hard they really are. "A path to solving them" is too broad. For most hard problems there is no known quantum speedup, and AI competes on the same ground: AlphaFold predicted more than 200 million protein structures on classical hardware.[^7]

I believe Gil about **the map, not the destination**.

### 4. The car company that built a quantum sensor in 1964

Here is a fact that surprised me. The first SQUID, a superconducting quantum interference device and an exquisitely sensitive magnetic-field sensor, was developed in 1964 at Ford Research Laboratory.[^1] A car company. More than sixty years ago. Today SQUIDs sit inside MRI machines.

Quantum physics was never as far from industry as we like to think. What the article describes is the moment it stopped being a footnote. Intel works with Urenco and Air Liquide on isotopically pure silicon. Element Six, part of De Beers, engineers diamonds for sensors. ID Quantique sells quantum links to banks. Governments fund national networks in China, South Korea and the UK, and ETSI writes the standards. "Subjects that used to be mere footnotes to physics will rule," Palmer writes, "and engineers (and perhaps even consumers) will have to learn to speak quantum."

And the car comes back. Bosch's Michael Bolle describes autonomous vehicles where quantum sensors, quantum cryptography and quantum computing work together: sense the world, communicate securely, decide. Ford's 1964 sensor was a curiosity. Bosch's vehicle is a system. A robotics engineer of the next decade will need to speak all three dialects.

As a person born in South America I can give this personal experience in Argentina. UNAHUR's machine is an educational SpinQ: 3 qubits, NMR at room temperature, shared with other institutions and combined with cloud access to larger machines. [PLACEHOLDER: interview with Dr. Federico Holik, if it happens.] As founder of Qimono (TM), I live the same gap every day: the learning is open to anyone, the hardware is not.

My own way of learning to speak quantum lives in my repository qu. It has a full Q# section, Microsoft's quantum language, and through it I want to open the debate on Majorana. Microsoft bets on Majorana-based topological qubits, announced its Majorana 1 chip in February 2025, and physicists still dispute the evidence. One of my goals in this MIT xPRO course is to be able to put Microsoft's Majorana claims under test myself, with help from classmates and teachers at MIT.

Because speaking a language is not the same as repeating what its teachers say. Speaking quantum, for me, means learning enough to ask the company that wrote the language: are you sure?

Zeilinger gave himself three years. It took far longer, and it is still not finished. Maybe that is the real lesson of the tipping point: it never arrives on the date the physicists promise. It arrives when enough engineers, in enough countries, have learned to speak the language.

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

## Changes from v13

- Style: Gladwell-inspired narrative blended with my voice. Each section now opens with a concrete story, zooms out to the mechanism, and zooms back in. Thesis emerges after the story, not before.
- Section hooks: Zeilinger's 2004 bank transfer (1), the SpinQ email (2), the rigged Proxora race (3), Ford's 1964 SQUID sensor (4). The essay closes by returning to Zeilinger's three years.
- Named frameworks: "the three-year promise", "harvest now, decrypt later", "lower the entry barrier", "Argentina-no-continuity", "the side-by-side habit", "the map, not the destination".
- Title fixed to "The Tipping Point of Quantum Computing" (also a nod to Gladwell's *The Tipping Point*).
- Content, sources and required terms carried over from v13; only additions are the Ford SQUID detail and the Landon Downs quote.
- Still to verify: post-2017 network events; Microsoft Majorana dates and the state of the dispute. Verified against the repo copy of the article: Ford's 1964 SQUID (now the section 4 hook), the Landon Downs / 1QBit quote (added to section 3), and the "speak quantum" sentence (PDF page 51).
