# Underwater Sonar Ghost-Net Dataset & AI Training

A structured repository for collecting, documenting, preparing, and training AI models on underwater sonar imagery for **ghost-net and marine-debris detection**.

## Project goal

Build a reproducible sonar-data pipeline that combines real underwater sonar datasets with carefully documented augmentation and training workflows. The primary target is ghost fishing nets, with related marine-debris/object classes used to improve robustness.

## Dataset sources

| Dataset / Source | Sonar type | Primary use | Status |
|---|---|---|---|
| [OpenSonarDatasets](https://github.com/remaro-network/OpenSonarDatasets) | SSS / FLS / Multibeam | Dataset discovery and benchmarking | Source directory |
| [Marine Debris FLS](https://github.com/mvaldenegro/marine-debris-fls-datasets) | Forward-looking sonar | Marine debris detection | Source repository |
| [Forward-Looking Underwater Mines & Debris](https://github.com/riku-1825/Forward_Looking_Under_Water_Mines_And_Debris_Sonar_dataset) | Forward-looking sonar | YOLO/object-detection baseline | Source repository |
| Side-scan sonar object/mine datasets | Side-scan sonar | Seabed clutter, targets, acoustic shadows | To verify |
| SWDD / sonar wall-anomaly data | Side-scan sonar | Man-made structure/anomaly detection | To verify |

> **Licensing:** Follow each original dataset's license and redistribution rules. This repository stores metadata, links, and preprocessing code unless redistribution of the underlying data is explicitly permitted.

## Recommended pipeline

1. Download datasets from their official source.
2. Record source, license, sonar type, image format, and annotation format.
3. Normalize labels into a common taxonomy.
4. Convert supported annotations to YOLO format.
5. Create train/validation/test splits without leakage between sequences or deployments.
6. Train a baseline object detector.
7. Add ghost-net-specific data as it becomes available.
8. Evaluate on held-out real sonar data from unseen locations/surveys.

## Initial target classes

- ghost_net
- fishing_gear
- tire
- pipe
- bottle
- can
- chain
- hook
- debris
- other_object

The taxonomy should be revised after inspecting the actual source annotations.

## Repository layout

```text
.
├── README.md
├── datasets/
│   ├── OpenSonarDatasets.md
│   ├── Marine-Debris-FLS.md
│   ├── Forward-Looking-Mines-Debris.md
│   ├── Side-Scan-Sonar.md
│   └── SWDD.md
├── data/
│   ├── raw/              # locally downloaded data; normally gitignored
│   ├── annotations/      # normalized annotations
│   ├── train/
│   ├── val/
│   └── test/
├── scripts/
│   ├── prepare_dataset.py
│   ├── convert_to_yolo.py
│   └── split_dataset.py
├── configs/
│   └── dataset.yaml
├── training/
│   └── README.md
├── requirements.txt
└── .gitignore
```

## Training

The first baseline is intended to support a YOLO-style detector. Training code will be added after the source datasets and annotation formats are verified.

## Important research note

Optical underwater images should not be treated as real sonar data. Synthetic sonar generation can be useful for augmentation, but real sonar data should remain the primary validation source because sonar appearance depends on acoustic geometry, material response, range, incidence angle, seabed characteristics, and sensor-specific effects.

## Roadmap

- [x] Create repository
- [x] Document initial public sonar sources
- [ ] Verify dataset licenses and availability
- [ ] Add download/verification scripts
- [ ] Normalize annotation schemas
- [ ] Build YOLO conversion pipeline
- [ ] Establish baseline model
- [ ] Add ghost-net-specific training data
- [ ] Evaluate cross-domain generalization
