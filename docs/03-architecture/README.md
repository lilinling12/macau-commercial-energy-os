# Architecture Authority

This directory stores the system architecture decisions derived from research authority.

Core architecture principles:

- Energy OS is an enterprise energy intelligence platform.
- Physical topology and settlement topology are separated.
- Energy Graph is the domain foundation.
- Tariff logic is versioned and traceable.
- Safety boundaries are explicit.

Architecture flow:

Research -> Decision -> Product -> Architecture -> Engineering -> Implementation -> Validation

PRD and research-Gate traceability, current design gaps, and implementation audit: `detailed-design/PRD-ARCHITECTURE-TRACEABILITY-v0.1.md`.

Stack-neutral STRIDE threat model and verification scenarios (draft; no G6 closure): `detailed-design/SECURITY-THREAT-MODEL-v0.1.md`.

Stack-neutral localization / internationalization design proposal (language set and implementation remain open): `detailed-design/LOCALIZATION-AND-I18N-DESIGN-v0.1.md`.

Stack-neutral data persistence and schema evolution design proposal (owner/data/security review pending; no physical database or migration selected): detailed-design/DATA-PERSISTENCE-AND-SCHEMA-EVOLUTION-DETAILED-DESIGN-v0.1.md.

Logical MVP application and event contract catalog (review draft; no endpoint or wire format selected): detailed-design/MVP-APPLICATION-AND-EVENT-CONTRACT-CATALOG-v0.1.md.
