# The Tipping Point of Quantum Computing
## Draft Version 17

Brainstorm draft. No word limit yet. Built on draft 16. Written for readers who already know Weeks 1 to 3 (teammates and professors): concepts are named, not explained, and the article is referenced, not transcribed. "I" can be read as Qimono (TM). Drafts 12 to 16 are untouched.

## Prompt checklist (must be covered in every draft)

- [x] 1. Networks: how ambitions differ across countries and why; impact on global relations since 2017; my own conviction on the role networks should play
- [x] 2. Investment: four reasons "the time for investment, all agree, is now"; which are most convincing
- [x] 3. Gil: three ways quantum software addresses his quote; argue whether to believe him
- [x] 4. Speak quantum: how the article presents it (corporate and government examples); examples from my own experience

---

### 1. The three-year promise

In 2004, the Bank of Austria and Vienna's city hall made the first quantum-encrypted bank transfer. Anton Zeilinger hoped "all problems of implementation will be solved within three years." Palmer's verdict, thirteen years later: "They were not."[^1]

The physics worked; the engineering did not. The no-cloning theorem forbids amplifiers, so fibre links stop at about 200 km and every relay must be trusted. I call this **the three-year promise**: the gap between an experiment that works and a network that works.

Who pays for that gap explains why ambitions differ. China's network is state-funded, from Beijing to Shanghai plus the Micius satellite: sovereignty, with patience as policy. South Korea, Britain and Australia build national or government links. In Europe, companies and standards lead (ID Quantique, ETSI): a product, with patience on a quarterly deadline.

Since 2017 that split has become geopolitics. Micius carried the first intercontinental quantum-secured video call, Beijing to Vienna, in September 2017,[^8] and by 2021 China ran a 4,600 km integrated satellite-and-fibre network.[^9] Europe answered with EuroQCI. But the NSA, the UK's NCSC and France, Germany, the Netherlands and Sweden all declined to rely on QKD.[^10] China bets on physics; the West bets on mathematics.

My conviction: "global effort or national shield?" is the wrong question. The real dilemma is feasibility. Each country builds its own shield, growing organically wherever links are feasible. Some classmates imagine a WHO-style global quantum initiative. Countries will share what quantum computers discover; they will never share the network that protects their secrets.

And a safer internet does not wait for any quantum network. Shor's algorithm breaks RSA and elliptic-curve signatures in polynomial time, so the fix is post-quantum signatures, and they ship now. My repository Proxora signs its first quantum-ready Debian package with ML-DSA (FIPS 204).[^2] Ubuntu 26.10 ships post-quantum ready package signing.[^3] Algorand has signed its State Proofs with Falcon since 2022.[^4] Seth Lloyd's quantum internet promises "establishing trust while protecting privacy." The trust is arriving first, without new fibre.

### 2. A quantum computer for the price of a car

On October 20, 2026, SpinQ quoted me USD 12,000 for a 2-qubit Gemini Mini Pro and USD 17,000 for a 3-qubit Triangulum Mini.[^5] A real quantum computer for less than a new car.

Palmer gives four reasons why "the time for investment, all agree, is now": small machines earn early, simulation pays off, security cannot wait, and nations need years to build capability.[^1] I rank them in this order:

**1. Cybersecurity.** Harvest now, decrypt later: the only threat that works backwards in time. Once Shor runs at scale, every RSA-encrypted secret stored today opens. Its deadline has already passed, which is why it ranks first.

**2. Small machines.** They lower the entry barrier: USD 12,000 is the most feasible door for a local startup like Qimono (TM). They earn first in financial services, above all portfolio optimization, a smaller problem than simulating nature. At Qimono (TM) we are building Porketo, a portfolio management system; its new MCP server lets the automation call Proxora's predictions, with prediction and portfolio optimization in Qiskit.

**3. Simulation.** The biggest prize, but a harder problem, so it pays later. Robotics shows why it matters: Musk calls Tesla's cars "semi-sentient robots on wheels."[^12] A self-driving car is a robot living inside reality, only as good as its model of that reality. Quantum simulation is how that model becomes exact, down to the chemistry of the battery that moves it. What quantum computers are best at simulating is still the evolving idea.

**4. National capability.** UNAHUR installed the first quantum computer in Argentina's public university system; CNEA is building a fluxonium processor. Meanwhile 2025 was the lowest science budget since at least 1972, 0.167% of GDP, with 2026 projected at 0.164%.[^6] **Argentina-no-continuity**: capability takes years to build and one budget to break. QaaS and hybrid setups are the workaround: when the hardware budget disappears, the cloud does not. It ranks last only because a startup cannot fix it alone.

### 3. The race I rigged on purpose

In Proxora, a quantum regression races a classical linear regression, and the quantum one always wins. I rigged it: nonlinear beats linear. It proves nothing about advantage; the point is the habit.

Dario Gil: "The power of quantum computing is rediscovering all the problems that computers cannot solve, and having a path to solving them."[^1] Quantum software delivers that in three ways:

1. **Languages and cloud access.** IBM put a real processor online in 2016; today it is QaaS, with hybrid setups calling a QPU for one step.
2. **Algorithms that map real problems.** The Algorithm Zoo catalogues the families; the work is encoding chemistry, logistics or finance into circuits.
3. **Better classical thinking.** 1QBit's Landon Downs: "By taking the lens of how you would formulate an algorithm on a quantum computer you often find very good improvements on classical algorithms."

Proxora keeps classical and quantum side by side: **the side-by-side habit**. Next comes SVM against QSVM, a fair fight between kernel methods, refereed by Big O, the new currency of the comparison.

Should we believe Gil? Yes, fully. Both halves are already happening. "Rediscovering the problems": you cannot write a problem for a quantum machine without rediscovering it, as 1QBit and my own race show. "A path to solving them": software is the path. Gil promised a path, not an arrival date, and we are already walking it.

### 4. The car company that built a quantum sensor in 1964

The first SQUID was built in 1964 at Ford Research Laboratory.[^1] A car company, more than sixty years ago. Palmer's point is that this kind of physics stops being a footnote: Intel with Urenco and Air Liquide on isotopically pure silicon, Element Six engineering diamonds for sensors, ID Quantique selling links to banks, governments funding national networks, ETSI writing the standards. "Engineers (and perhaps even consumers) will have to learn to speak quantum."

The car comes back. Bosch's Michael Bolle describes autonomous vehicles combining quantum sensing, cryptography and computing. Ford's sensor was a curiosity; Bosch's vehicle is a system. Tomorrow's robotics engineer speaks all three dialects.

As a person born in South America I can give this personal experience in Argentina. UNAHUR's machine is a 3-qubit NMR SpinQ, shared and combined with cloud access. [PLACEHOLDER: interview with Dr. Federico Holik, if it happens.] There will be more than one winning modality, and Argentina already touches three: NMR at UNAHUR, fluxonium at CNEA, and the topological approach I study. As founder of Qimono (TM), I live the gap: the learning is open, the hardware is not.

My way of speaking quantum lives in my repository qu, which has a full Q# section, and through it I want to open the Majorana debate. Majorana 1 (February 2025) was heavily disputed. Majorana 2 (June 2026) reports a mean parity lifetime of about 20 seconds, over 1,000 times its predecessors, and a doubled topological gap.[^11] But parity lifetime is not coherence, and the paper is not peer-reviewed. The right measuring stick is Google's: Willow went below the error-correction threshold,[^13] so the race is gate depth at low logical error, not qubit count. One of my goals in this MIT xPRO course is to put Majorana 2 to that test, with classmates and teachers at MIT. Speaking quantum means learning enough to ask the company that wrote the language: are you sure?

Zeilinger gave himself three years. It took far longer, and it is still not finished. The tipping point never arrives on the date the physicists promise. It arrives when enough engineers, in enough countries, speak the language.

---

## Footnotes

[^1]: Jason Palmer, "Here, there and everywhere," *The Economist*, Technology Quarterly, March 2017, Sections 3 to 6. Repo copy: `assets/Here_there_everywhere_Economist.md`.

[^2]: qimono-repos/proxora, `packaging/`. https://github.com/qimono-repos/proxora

[^3]: Canonical, "Canonical releases Ubuntu 26.10 Stonking Stingray," October 2026, https://canonical.com/blog/canonical-releases-ubuntu-26-10-stonking-stingray ; https://canonical.com/blog/ubuntu-26-10-security

[^4]: Algorand, "Post-Quantum Technology," https://algorand.co/technology/post-quantum

[^5]: Email from Rachel Lin, Overseas Sales Manager, Shenzhen SpinQ Technology, October 20, 2026. Shipping included; tax and duty not included. Informal price, not a formal quotation.

[^6]: Grupo EPC–ANPRES; CIICTI–ANPRES No. 32 (2026 projection). Charts: https://github.com/qimono-repos/mit-prox-rd/blob/trunk/essay/argentina-science-budget.svg

[^8]: Chinese Academy of Sciences, September 2017, https://english.cas.cn/newsroom/news/201709/t20170928_183577.shtml

[^9]: Optica, January 2021, https://optica-opn.org/home/newsroom/2021/january/quantum_keys_sent_along_fiber_and_into_space

[^10]: Marin Ivezic, "How countries differ on QKD," PostQuantum, December 2025, https://postquantum.com/post-quantum/qkd-countries-differ/

[^11]: Microsoft, "Majorana 2," June 2, 2026, https://news.microsoft.com/source/features/innovation/majorana-2-microsoft-discovery-agentic-ai/ ; The Quantum Insider, June 2, 2026.

[^12]: Elon Musk, Tesla AI Day, August 2021. [TO VERIFY: exact wording and link.]

[^13]: Google, "Meet Willow," December 2024, https://blog.google/technology/research/google-willow-quantum-chip/

---

## Changes from v16

- Trimmed for Week 1-3 readers: no explanation of QKD, post-quantum signatures, SQUID, parity lifetime, Big O or linear vs nonlinear beyond one clause. Article lists shortened.
- Section 1: no-cloning theorem named in one line inside the three-year promise. Shor's algorithm (polynomial-time break of RSA and elliptic curves) as the motivation for post-quantum signatures.
- Section 2: Shor added to cybersecurity at number 1. "The evolving idea" restored in simulation.
- Section 4: Willow framed as gate depth at low logical error.
- About 1,700 words in the body, down from about 2,700.
- Still open: Musk quote wording; Holik placeholder; primary agency links for QKD positions.
