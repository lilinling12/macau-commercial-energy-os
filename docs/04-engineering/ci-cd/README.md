# CI/CD Governance

CI is an engineering gate, not only a build runner.

## Initial required checks

- repository / documentation structure validation;
- contract and schema validation;
- formatting and lint;
- unit tests;
- build checks;
- security / dependency checks where available.

## Later Energy OS-specific checks

- tariff Golden Bill fixtures;
- historical settlement replay;
- simulator regression;
- optimization feasibility checks;
- Safety Kernel / command arbitration tests;
- tenant isolation tests;
- edge protocol compatibility tests.

## Rule

A green build does not override Authority or evidence requirements. CI proves selected properties; it does not redefine architecture or convert assumptions into verified facts.
