# Side-Scan Sonar Sources

This file tracks side-scan sonar (SSS) datasets relevant to object detection, seabed clutter, targets, and acoustic-shadow learning.

## Priority

Real SSS data is particularly important for a ghost-net detector because net/gear appearance can depend strongly on acoustic shadows, seabed texture, incidence angle, range, and sensor characteristics.

## Candidate source

Use OpenSonarDatasets as the discovery index:
https://github.com/remaro-network/OpenSonarDatasets

## Before integration

- Verify official source
- Verify license and redistribution terms
- Record sonar frequency/sensor where available
- Record image dimensions and dynamic range
- Identify annotations and class definitions
- Inspect examples for acoustic shadows and seabed clutter
- Convert annotations to the common project schema
