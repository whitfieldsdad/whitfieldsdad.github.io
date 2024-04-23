+++
title = 'Translating STIX 2 content into directed acyclic graphs (DAGs)'
date = 2023-01-15T09:00:00-07:00
draft = false
tags = ['data']
+++


STIX 2 models relationships between STIX Domain Objects (SDOs) and STIX Cyber-observable Objects (SCOs) in two different ways:

1. Using STIX Relationship Objects (SROs) (i.e. within `relationship` or `sighting` objects); and
2. Using embedded relationships (e.g. `attack-pattern` objects contain embedded references to `x-mitre-tactic` objects using the `kill_chain_phases` property).

In this post, we'll cover:

- The set of SDOs, SROs, SCOs, and predicates outlined within the [STIX 2.1 specification](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html);
- The set of SDOs, SROs, and predicates used by MITRE when expressing [ATT&CK](https://github.com/mitre-attack/attack-stix-data/tree/master) ([Enterprise](https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack.json), [Mobile](https://github.com/mitre-attack/attack-stix-data/raw/master/mobile-attack/mobile-attack.json), [ICS](https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/ics-attack/ics-attack.json)), [CAPEC](https://github.com/mitre/cti/raw/master/capec/2.1/stix-capec.json), [NIST SP 800-53](https://github.com/center-for-threat-informed-defense/attack-control-framework-mappings/blob/main/frameworks/attack_12_1/nist800_53_r5/stix/nist800-53-r5-controls.json), and the [relationships between ATT&CK techniques and NIST SP-800-53 controls](https://github.com/center-for-threat-informed-defense/attack-control-framework-mappings/blob/main/frameworks/attack_12_1/nist800_53_r5/stix/nist800-53-r5-mappings.json) in STIX 2.1 format;
- A set of objects which can be used to model STIX 2 content relationally (e.g. in [third normal form (3NF)](https://en.wikipedia.org/wiki/Third_normal_form) or as a [snowflake](https://en.wikipedia.org/wiki/Snowflake_schema))
- A set of predicates which can be used to characterize embedded relationships (e.g. relationships between `attack-pattern` and `x-mitre-tactic` objects).

The following datasets will be used:

|Name|Format|URL|
|----|------|---|
|ATT&CK Enterprise|STIX 2.1|https://github.com/mitre-attack/attack-stix-data/raw/master/enterprise-attack/enterprise-attack.json|
|ATT&CK Mobile|STIX 2.1|https://github.com/mitre-attack/attack-stix-data/raw/master/mobile-attack/mobile-attack.json|
|ATT&CK ICS|STIX 2.1|https://github.com/mitre-attack/attack-stix-data/blob/master/ics-attack/ics-attack.json|
|CAPEC|STIX 2.1|https://github.com/mitre/cti/raw/master/capec/2.1/stix-capec.json|
|NIST SP-800-53|STIX 2.1|https://github.com/center-for-threat-informed-defense/attack-control-framework-mappings/raw/main/frameworks/attack_12_1/nist800_53_r5/stix/nist800-53-r5-controls.json|
|MITRE ATT&CK Enterprise to NIST SP-800-53|STIX 2.1|https://github.com/center-for-threat-informed-defense/attack-control-framework-mappings/raw/main/frameworks/attack_12_1/nist800_53_r5/stix/nist800-53-r5-mappings.json|

If you'd like to follow along, you can use the following Python 3 script to explore all STIX 2.1 objects from the following datasets:

- MITRE ATT&CK (Enterprise)
- MITRE ATT&CK (Mobile)
- MITRE ATT&CK (ICS)
- MITRE CAPEC
- NIST SP 800-53

```bash
python3 -m pip install stix2
```

```python3

```
