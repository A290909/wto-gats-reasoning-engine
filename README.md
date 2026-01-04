**WTO–GATS Reasoning Engine**

**A research-oriented tool for structuring legal analysis under the GATS**

1. **Research Context and Purpose**
Legal analysis under the General Agreement on Trade in Services (GATS) commonly follows a structured reasoning sequence developed in WTO jurisprudence. This sequence typically begins with the identification of a prima facie inconsistency with market access (Article XVI) or national treatment (Article XVII), and, where relevant, proceeds to the examination of justifications under Article XIV, including necessity and proportionality considerations and compliance with chapeau-type conditions.
The purpose of this repository is to provide a conceptual and research-oriented tool that mirrors this reasoning structure in a transparent and systematic manner. Rather than offering automated legal conclusions, the tool is designed to support doctrinal clarity, facilitate comparative reasoning, and assist in the organization of complex legal arguments in research on services trade and digital regulation.

2. **Relation to the PhD Research Project**
This project accompanies a doctoral research project examining the compatibility of selected provisions of the EU Data Act (Articles 4, 5, and 35) with WTO obligations under the GATS. The repository operationalizes the core analytical pathway employed in the dissertation—namely:
identification of potential GATS market access or national treatment concerns;

assessment of regulatory objectives under Article XIV;
structured consideration of necessity and proportionality; and
examination of non-arbitrary or non-discriminatory application as reflected in chapeau-type reasoning.
By translating this analytical sequence into a structured logic model, the tool serves as a methodological aid for developing and testing hypothetical scenarios involving cross-border data flows and digital services.

3. **Methodological Approach**
The tool adopts a rule-based and explainable approach, reflecting the logic of WTO legal reasoning rather than technical automation. Each step corresponds to a well-established doctrinal stage in WTO case law, including landmark decisions such as US–Gambling, Korea–Beef, and China–Publications.
The variables used in the model are deliberately simplified proxies. They are intended to prompt legally relevant questions such as the existence of less trade-restrictive alternatives or the clarity of a measure’s contribution to a legitimate objective rather than to replace detailed factual or legal assessment. The output highlights analytical steps taken, risk indicators, and information gaps, thereby reinforcing the interpretive nature of WTO analysis.

4. **Scope and Limitations**
This repository does not aim to:
provide legal advice;
automate legal decision-making; or
determine WTO-consistency in a definitive manner.
Instead, it should be understood as a conceptual research instrument. Its value lies in clarifying analytical pathways, improving internal coherence in legal argumentation, and enhancing transparency in the assessment of regulatory measures affecting trade in services.

5. **How to Use the Tool (Research Demonstration)**

The repository contains illustrative scenarios inspired by regulatory measures affecting digital services. These scenarios are hypothetical and serve solely for analytical demonstration.
To run the examples:
Copy code
Bash
python -m src.examples

The output presents:
a qualitative risk indication (Low / Medium / High);

a step-by-step reasoning trace aligned with GATS analysis; and
a list of missing information required for a complete legal assessment.

6. **Academic Relevance**
By bridging doctrinal analysis and structured logic, this project contributes to ongoing discussions on regulatory autonomy, legal certainty, and institutional coherence in international economic law. It demonstrates how complex legal tests developed in WTO jurisprudence may be systematically articulated without compromising their interpretive and context-sensitive character.

7. **Disclaimer**
This repository is provided exclusively for academic and research purposes.
It does not constitute legal advice and should not be used as a substitute for doctrinal legal analysis or case-specific evaluation.
