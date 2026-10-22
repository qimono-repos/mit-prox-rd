# The Tipping Point of Quantum Computing
## Draft Version 20

Same text as draft 19. Only change: footnote numbers replaced by inline links with full source names, for copy-paste into the forum's rich-text editor. "I" can be read as Qimono (TM). Drafts 12 to 19 are untouched.

## Prompt checklist (must be covered in every draft)

- [x] 1. Networks: how ambitions differ across countries and why; impact on global relations since 2017; my own conviction on the role networks should play
- [x] 2. Investment: four reasons "the time for investment, all agree, is now"; which are most convincing
- [x] 3. Gil: three ways quantum software addresses his quote; argue whether to believe him
- [x] 4. Speak quantum: how the article presents it (corporate and government examples); examples from my own experience

---

### The three-year promise

In 2004, the Bank of Austria and Vienna's city hall made the first quantum-encrypted bank transfer. Anton Zeilinger hoped "all problems of implementation will be solved within three years." Palmer's verdict, thirteen years later: "They were not." ([The Economist, "Here, there and everywhere" (2017)](https://quantuminstitute.yale.edu/publications/here-there-and-everywhere-quantum-technology-beginning-come-its-own))

The physics worked; the engineering did not. The no-cloning theorem forbids amplifiers, so fibre links stop at about 200 km and every relay must be trusted. I call this **the three-year promise**: the gap between an experiment that works and a network that works.

Who pays for that gap explains why ambitions differ. China's network is state-funded, from Beijing to Shanghai plus the Micius satellite: sovereignty, with patience as policy. South Korea, Britain and Australia build national or government links. In Europe, companies and standards lead (ID Quantique, ETSI): a product, with patience on a quarterly deadline.

Since 2017 that split has become geopolitics. Micius carried the first intercontinental quantum-secured video call, Beijing to Vienna, in September 2017, ([Chinese Academy of Sciences, first intercontinental quantum video call](https://english.cas.cn/newsroom/news/201709/t20170928_183577.shtml)) and by 2021 China ran a 4,600 km integrated satellite-and-fibre network. ([Optica, "Quantum keys sent along fiber and into space"](https://optica-opn.org/home/newsroom/2021/january/quantum_keys_sent_along_fiber_and_into_space)) Europe answered with EuroQCI. But the NSA, the UK's NCSC and France, Germany, the Netherlands and Sweden all declined to rely on QKD. ([PostQuantum, "How countries differ on QKD"](https://postquantum.com/post-quantum/qkd-countries-differ/)) China bets on physics; the West bets on mathematics.

My conviction: "global effort or national shield?" is the wrong question. The real dilemma is feasibility. Each country builds its own shield, growing organically wherever links are feasible. Some classmates imagine a WHO-style global quantum initiative. Countries will share what quantum computers discover; they will never share the network that protects their secrets.

And a safer internet does not wait for any quantum network. Shor's algorithm breaks RSA and elliptic-curve signatures in polynomial time, so the fix is post-quantum signatures, and they ship now. My repository [Proxora](https://github.com/qimono-repos/proxora) signs its first quantum-ready Debian package, the standard installable format in Linux operating systems like Ubuntu, with ML-DSA (FIPS 204). The timing couldn't be better: this October, during this course, the news arrived that some Linux distributions, starting with Ubuntu 26.10, are now quantum ready with post-quantum signatures. ([Canonical, "Canonical releases Ubuntu 26.10 Stonking Stingray"](https://canonical.com/blog/canonical-releases-ubuntu-26-10-stonking-stingray)) Algorand has signed its State Proofs with Falcon since 2022. ([Algorand, "Post-Quantum Technology"](https://algorand.co/technology/post-quantum)) Seth Lloyd's quantum internet promises "establishing trust while protecting privacy." The trust is arriving first, without new fibre.

### A quantum computer for the price of a car

Quantum computing was born in the cloud. Everyone rents it by the hour. But for local development I wanted one on my desk, so I wrote to SpinQ directly. On October 20, 2026, the answer arrived: USD 12,000 for a 2-qubit Gemini Mini Pro, USD 17,000 for a 3-qubit Triangulum Mini. (email from SpinQ's sales team, October 20, 2026; tax and duty not included) A real quantum computer for less than a new car.

Palmer gives four reasons why "the time for investment, all agree, is now": small machines earn early, simulation pays off, security cannot wait, and nations need years to build capability. ([The Economist, "Here, there and everywhere" (2017)](https://quantuminstitute.yale.edu/publications/here-there-and-everywhere-quantum-technology-beginning-come-its-own)) I rank them in this order:

**1. Cybersecurity.** Because the fear of RSA breaking down is the strongest reason, and enough on its own to motivate quantum-ready checks worldwide, across companies and countries, starting with a Quantum-Readiness Roadmap, as CISA, NSA and NIST recommend. ([CISA, NSA and NIST, "Quantum-Readiness: Migration to Post-Quantum Cryptography"](https://cisa.gov/resources-tools/resources/quantum-readiness-migration-post-quantum-cryptography)) Harvest now, decrypt later: the only threat that works backwards in time. Once Shor runs at scale, every RSA-encrypted secret stored today opens.

**2. Small machines.** Small machines, because the lower the entry barrier, the easier to implement: for entrepreneur developers like me at Qimono (TM), or for students in the Iniciativa Cuántica, the Argentine university network for quantum technologies led by UNAHUR (University National of the City Hurlingham, Buenos Aires) with UNICEN (University National of the Center of the Province of Buenos Aires), UNRN (University National of Río Negro), UNLP (University National of La Plata) and others. ([UNAHUR, Iniciativa Cuántica declaration](https://unahur.edu.ar/wp-content/uploads/2026/03/Declaracion-de-Intencion-para-la-promocion-y-desarrollo-de-una-iniciativa-cuantica.pdf)) UNAHUR already runs a 3-qubit NMR SpinQ, the first quantum computer in Argentina's public university system.

I am not the only one calling this a tipping point. Malcolm Gladwell's [*The Tipping Point*](https://www.amazon.com/dp/B000OT8GD0) describes the moment when small things accumulate into a snowball. McKinsey used the same words in April 2026: a commercial tipping point, with more than 300 companies working with quantum firms and USD 12.6 billion invested in 2025. ([McKinsey, "Quantum Technology Monitor 2026: A commercial tipping point"](https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/mckinsey-quantum-technology-monitor-2026-a-commercial-tipping-point)) Add post-quantum Linux and a quantum computer for the price of a car, and the momentum is real.

Small machines earn first in financial services, above all portfolio optimization, a smaller problem than simulating nature. At Qimono (TM) we are building [Porketo](https://github.com/qimono-repos/the-porketo), a portfolio management system; its new MCP server lets the automation call Proxora's predictions, with prediction and portfolio optimization in Qiskit.

**3. Simulation.** The biggest prize, but a harder problem than portfolio optimization, so it pays later. Elon Musk calls Tesla's cars "semi-sentient robots on wheels." ([TechCrunch, Tesla AI Day 2021](https://techcrunch.com/?p=2191983)) This applies to the whole self-driving industry. In the Humid Pampas, where I come from, people say the most advanced robot is the combine harvester. Since 1995, when INTA Manfredi drew Argentina's first yield map, ([INTA Argentina, CEPAL presentation on precision agriculture](https://d7.cepal.org/sites/default/files/presentations/presentacion.tecnica_1_fernando-scaramuzza_inta-argentina.pdf)) combines have carried GPS and yield monitors that map every field as they harvest it. Maybe this is why, since a young age, I learned to look at robotics with different eyes. A self-driving machine is a robot living inside reality, only as good as its model of that reality. Quantum simulation is how that model becomes exact, down to the chemistry of the battery that moves it. What quantum computers are best at simulating is still the evolving idea.

**4. National capability.** Britain (£270m), the EU (€1bn) and China invest so they won't fall behind. ([The Economist, "Here, there and everywhere" (2017)](https://quantuminstitute.yale.edu/publications/here-there-and-everywhere-quantum-technology-beginning-come-its-own)) Argentina shows the other side. CNEA is building a fluxonium processor, superconducting qubits made in Argentina. And all of this is happening in spite of the lowest science budget since 1972: 0.167% of GDP in 2025, and 0.164% projected for 2026. ([Grupo EPC–ANPRES and CIICTI–ANPRES, Argentina science budget chart](https://github.com/qimono-repos/mit-prox-rd/blob/trunk/essay/argentina-science-budget.svg)) It ranks last only because a startup cannot fix it alone.

### The race Qimono (TM) rigged on purpose

In Proxora, the Qimono (TM) software project for the command line and the Model Context Protocol, a quantum regression races a classical linear regression, and the quantum one always wins. Qimono (TM) rigged it: nonlinear beats linear. It proves nothing about advantage; the point is the habit.

Dario Gil: "The power of quantum computing is rediscovering all the problems that computers cannot solve, and having a path to solving them." ([The Economist, "Here, there and everywhere" (2017)](https://quantuminstitute.yale.edu/publications/here-there-and-everywhere-quantum-technology-beginning-come-its-own)) Quantum software delivers that in three ways:

1. **Cloud access.** IBM put a real processor online in 2016. That was the birth of QaaS (Quantum as a Service), a technology born in the cloud, with hybrid setups calling a QPU for one step.
2. **Languages.** Many quantum libraries, starting with Qiskit, then Google's Cirq, Xanadu's PennyLane and the Amazon Braket SDK, are built on Python, the most widespread language in artificial intelligence. And for developers with deep roots in C# and the .NET world, there is Microsoft's Q#.
3. **Better classical thinking.** 1QBit's Landon Downs: "By taking the lens of how you would formulate an algorithm on a quantum computer you often find very good improvements on classical algorithms." ([The Economist, "Here, there and everywhere" (2017)](https://quantuminstitute.yale.edu/publications/here-there-and-everywhere-quantum-technology-beginning-come-its-own))

Proxora keeps classical and quantum side by side: **the side-by-side habit**. Next comes SVM against QSVM, a fair fight between kernel methods, refereed by Big O, the new currency of the comparison.

Should we believe Gil? Yes, fully. Both halves are already happening. "Rediscovering the problems": you cannot write a problem for a quantum machine without rediscovering it, as 1QBit and my own race show. "A path to solving them": software is the path. Gil promised a path, not an arrival date, and we are already walking it.

### The car company that built a quantum sensor in 1964

The first SQUID was built in 1964 at Ford Research Laboratory. ([The Economist, "Here, there and everywhere" (2017)](https://quantuminstitute.yale.edu/publications/here-there-and-everywhere-quantum-technology-beginning-come-its-own)) A car company, more than sixty years ago. Palmer's point is that this kind of physics stops being a footnote: Intel with Urenco and Air Liquide on isotopically pure silicon, Element Six engineering diamonds for sensors, ID Quantique selling links to banks, governments funding national networks, ETSI writing the standards. "Engineers (and perhaps even consumers) will have to learn to speak quantum."

The car comes back. Bosch's Michael Bolle describes autonomous vehicles combining quantum sensing, cryptography and computing. Ford's sensor was a curiosity; Bosch's vehicle is a system. Tomorrow's robotics engineer speaks all three dialects.

As a person born in South America I can give this personal experience in Argentina. There will be more than one winning modality, and Argentina already touches three: NMR, fluxonium at CNEA, and the topological approach I study. As founder of Qimono (TM), I live the gap: the learning is open, the hardware is not.

My way of speaking quantum lives in my repository qu, which has a full Q# section, and through it I want to open the Majorana debate. Majorana 1 (February 2025) was heavily disputed. Majorana 2 (June 2026) reports a mean parity lifetime of about 20 seconds, over 1,000 times its predecessors, and a doubled topological gap. ([Microsoft, "Majorana 2"](https://news.microsoft.com/source/features/innovation/majorana-2-microsoft-discovery-agentic-ai/)) But parity lifetime is not coherence, and the paper is not peer-reviewed. The right measuring stick is Google's: Willow went below the error-correction threshold, ([Google, "Meet Willow"](https://blog.google/technology/research/google-willow-quantum-chip/)) so the race is gate depth at low logical error, not qubit count. One of my goals in this MIT xPRO course is to put Majorana 2 to that test, with classmates and teachers at MIT. Speaking quantum means learning enough to ask the company that wrote the language: are you sure?

Zeilinger gave himself three years. It took far longer, and it is still not finished. The tipping point never arrives on the date the physicists promise. It arrives when enough engineers, in enough countries, speak the language.

---

## Changes from v19

- Text unchanged. Every footnote marker replaced by an inline link with the full source name, so links survive copy-paste into the forum editor. The footnotes section is removed.
- Two links merged where the text already linked the same source: Proxora (section 1) and *The Tipping Point* (ranking #2), so the same URL does not appear twice in a row.
