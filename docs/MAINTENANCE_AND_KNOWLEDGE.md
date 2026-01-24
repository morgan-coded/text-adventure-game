# Maintenance Strategy (SDLC Maintenance Phase)

Maintenance is the longest lifecycle phase and directly impacts reliability, security, and ROI.

## Corrective maintenance
Fix defects that prevent correct operation.
Example: concurrency issue where two customers book the last asset; requires transaction/locking analysis and fix.

## Adaptive maintenance
Modify system to remain compatible with external changes:
- new offerings (paddleboards, eco-tours, bundles)
- payment processor updates
- security/compliance changes

## Perfective maintenance
Enhancements based on real use:
- streamline admin workflows
- improve mobile booking usability
- performance improvements for reporting or availability queries

## Preventive maintenance
Proactive tasks to reduce failure likelihood:
- database optimization
- automated backups
- monitoring/alerts
- patch management
- vulnerability scanning, SSL renewals, security hardening

## Maintenance workflow
1) identify & log issue/request
2) analyze root cause
3) design fix
4) implement in dev environment
5) test
6) deploy (prefer off-peak)
7) post-implementation review + documentation update

# Knowledge Retention Policy

Small businesses are vulnerable when system knowledge lives in one person.

Policy:
- documentation-first: no change is "done" until documented
- centralized repository: architecture diagrams, schemas, config, troubleshooting guides
- living user manuals updated when workflows change
- training materials maintained for seasonal staff onboarding
