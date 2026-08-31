# Madagascar Health Enterprise Architecture (HEA)
### Context, methodology, approach, and content — one-page overview

## 1. Context

Madagascar's digital health landscape is growing quickly, but like in many countries it faces fragmentation: multiple systems, duplicated data collection, weak interoperability, and investments that do not always connect to measurable health outcomes. The Ministry of Health needs a common architectural reference so that every initiative — government-led or partner-funded — fits into one coherent national ecosystem.

The **Health Enterprise Architecture (HEA)** answers that need. It is the documented enterprise architecture of Madagascar's digital health sector: a single, structured body of knowledge that describes where the country is going, why, and how each system contributes.

## 2. Methodology: value-driven architecture, documented as code

Two methodological choices define the HEA:

- **Value-Driven Enterprise Architecture.** Instead of starting from technology, we start from expected results for beneficiaries (patients, health workers, managers) expressed as national **value streams**, then trace downward to the **capabilities** required to deliver them, and only then to principles, standards, decisions, and technical patterns. Every technical artifact can be traced back to a strategic outcome.
- **Architecture as code.** The entire framework is written in structured Markdown with YAML metadata, versioned in Git, and validated by automated scripts (link integrity across 3,000+ cross-references, generated documents from a machine-readable referential). This keeps the documentation always coherent, auditable, and maintainable as a living asset rather than a static PDF.

## 3. Approach: a four-tier document hierarchy

The HEA organizes its content into four families, each addressing a distinct audience, plus a machine-readable source of truth:

| Tier | Document | Answers | Audience |
|------|----------|---------|----------|
| 1 | **CAESN** — Enterprise Architecture Framework | Why? Value streams, capabilities, principles, data, governance | Decision-makers, business owners |
| 2 | **CNISN** — National Interoperability Framework | How do systems interoperate? Standards, decisions (ADRs), compliance | DEPSI, architects, integrators |
| 3 | **ARTSN** — Reference Technical Architecture | What patterns and constraints? Technical chapters, data dictionary, roadmap | Architects, technical teams |
| 4 | **PTISN** — Implementation Profiles | How do I implement my initiative? Ready-to-use profiles per project | Developers, vendors |
| — | **Referentiel** (source of truth) | Machine-readable foundations from which published documents are generated | Tooling, governance scripts |

Each document opens with a "who should read this" guide, and reading matrices route every stakeholder profile to the right entry point.

## 4. Content at a glance

- **4 national value streams** (VS-01–VS-04) covering priority health flows
- **18 enterprise capabilities** (CAP-01–18) with maturity assessment and runway
- **14 interoperability capabilities** organized in 7 families
- **12+ technical architecture chapters** (ART-0 to ART-11): patterns, contracts, constraints
- **Shared data dictionary**: 31 sourced data objects across 7 domains, mapped to business objects and architecture chapters
- **10 Architecture Decision Records** (ADRs) with a decision registry and change process
- **Mandatory standards** (STD series) including international norms, plus 10 RBAC policies
- **Governance toolkit**: validation/homologation process, compliance program, architectural watch, deprecation process, legal foundation for an e-health bill
- **15 implementation profiles** (PT-01–PT-15), templates, and a national target topology
- **Roadmaps**: interoperability trajectory (Q4 2026 – Q2 2030) and a 6-phase technical roadmap aligned with national budgeting

## 5. Why it matters

The HEA gives Madagascar a durable governance instrument: any new digital health investment can be checked against a common reference before money is spent, and any existing system can be positioned on a shared roadmap. It reduces duplication, accelerates procurement and implementation, and keeps the sector's digital trajectory anchored in health outcomes rather than in individual projects.
