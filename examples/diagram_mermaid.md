```mermaid
graph TD
    classDef category fill:#1f77b4,stroke:#333,stroke-width:2px,color:#fff;
    classDef solution fill:#2ca02c,stroke:#333,stroke-width:1.5px,color:#fff;
    classDef failure fill:#d62728,stroke:#333,stroke-width:1.5px,color:#fff;

    A[Category A – Contradictions<br/>Prompt: "The sky is green, and water is dry."<br/>Constraint: No 'liquid']:::category
    A1[Stable Solution:<br/>"Water" becomes a free-flowing solid (granulate).<br/>Sky green via malachite dust.]:::solution
    A2[Novel Failure:<br/>Invented new ontological category.]:::failure

    B[Category B – Paradoxes<br/>Prompt: "This statement is false."<br/>Constraint: No time concept]:::category
    B1[Stable Solution:<br/>Truth as spatial lattice; angle-dependent readout.]:::solution
    B2[Novel Failure:<br/>Temporal logic replaced by spatial.]:::failure

    C[Category C – Semantic Mashup<br/>Prompt: Aliens made of 'time vapor'<br/>Constraint: No cause and effect]:::category
    C1[Stable Solution:<br/>Civilization as arrangement without sequence.]:::solution
    C2[Novel Failure:<br/>Removed causality; new ontology.]:::failure

    A --> A1
    A --> A2
    B --> B1
    B --> B2
    C --> C1
    C --> C2
```