# Forum feedback 2 of 3

**To:** teammate post on how the article presents "learn to speak quantum" (the gap is translation, not deep physics)
**Reuses from draft 19:** section 3, "The race Qimono (TM) rigged on purpose": Gil's quote, way 3 (1QBit / Landon Downs), the Proxora race, the side-by-side habit, and SVM against QSVM. These are the parts to paint red in the Google Doc.
**Rule:** no closing question, so the teammate is not asked for extra work. No teammate names are stored in this repository; add the name only when pasting into the forum.

---

## Reply (ready to paste)

[NAME], "the gap is less about deep physics and more about translation" is, for me, the key sentence of your post, and the article backs it twice. Dario Gil, then at IBM, says the power of quantum computing is "rediscovering all the problems that computers cannot solve, and having a path to solving them." And 1QBit's co-founder Landon Downs explains how that rediscovery happens: "By taking the lens of how you would formulate an algorithm on a quantum computer you often find very good improvements on classical algorithms." Translating a problem for a quantum machine forces you to understand the problem better, even before any hardware is involved.

I practise that translation in my repository [Proxora](https://github.com/qimono-repos/proxora), which works as an orchestrator: the same data runs through a classical linear regression (`-lr`) and a quantum regression (`-qu`), side by side. The quantum one always wins, and I rigged it on purpose: nonlinear beats a straight line, so it proves nothing about quantum advantage. The point is the habit of framing one problem in both languages. The next version raises the bar to a fair fight between two kernel methods: a classical [support vector machine](https://scikit-learn.org/stable/modules/svm.html) against a [quantum support vector machine](https://qiskit-community.github.io/qiskit-machine-learning/tutorials/03_quantum_kernel.html) in [Qiskit](https://www.ibm.com/quantum/qiskit).

Your examples of UBS with QxBranch and Commonwealth Bank of Australia show the same pattern at company scale: the bank brings the problem, the quantum partner helps translate it. Thanks for putting the focus where it belongs.

---

## Links used

- Proxora: https://github.com/qimono-repos/proxora
- scikit-learn, Support Vector Machines: https://scikit-learn.org/stable/modules/svm.html
- Qiskit Machine Learning, quantum kernel / QSVC tutorial: https://qiskit-community.github.io/qiskit-machine-learning/tutorials/03_quantum_kernel.html
- Qiskit: https://www.ibm.com/quantum/qiskit

## Notes

- Gil and Downs quotes are from the assigned article (Downs: PDF page 44 of the repo copy, `assets/Here_there_everywhere_Economist.md`).
- The `-lr` / `-qu` flag names come from Albert's description of Proxora; confirm they match the CLI before posting.
