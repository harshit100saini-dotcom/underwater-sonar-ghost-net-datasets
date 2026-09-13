# Verified Sonar Dataset Sources

_Last checked: 2026-09-13_

This file records what has been verified about candidate datasets. A dataset being publicly downloadable does **not** automatically mean its contents can be redistributed in this repository.

## 1. OpenSonarDatasets

Source: https://github.com/remaro-network/OpenSonarDatasets

- Type: directory/index of sonar datasets, not the dataset files themselves.
- Covers SSS, FLS, MBES and other sonar datasets.
- Purpose: discover and compare open sonar datasets.
- License of each underlying dataset must be checked separately.
- **Status for our project:** discovery source; do not treat it as permission to redistribute data.

## 2. Marine Debris FLS Datasets

Source: https://github.com/mvaldenegro/marine-debris-fls-datasets

- Sonar: ARIS Explorer 3000 forward-looking sonar.
- Includes water-tank and turntable marine-debris data.
- Water-tank release includes full sonar PNG images and JSON bounding-box annotations.
- Reported classes include bottle, can, chain, drink carton, hook, propeller, shampoo bottle, standing bottle, tire and valve.
- The repository is public and provides releases containing downloadable data.
- **License status: NOT YET CONFIRMED.** The repository has an open issue specifically asking about data permission/license, so we should not mirror the raw dataset into our GitHub repo until the authors' reuse terms are confirmed.
- **Status for our project:** high priority; download from the original source for local/cloud training after checking permission.

## 3. Forward-Looking Underwater Mines & Debris Sonar Dataset

Source: https://github.com/riku-1825/Forward_Looking_Under_Water_Mines_And_Debris_Sonar_dataset

- Sonar: forward-looking sonar.
- Format: YOLO.
- Contains 11 underwater object classes with train/validation/test splits and YOLO annotations.
- Repository license: MIT.
- The dataset repository references Marine Debris FLS and Mine Sonar Images as source material, so the MIT license of the repository should **not automatically be assumed to relicense every underlying image**.
- **Status for our project:** useful for a baseline, but verify the underlying data rights before redistributing images.

## 4. Side-scan sonar imaging for Mine detection

Source: https://figshare.com/articles/dataset/_i_Side-scan_sonar_imaging_for_Mine_detection_i_/24574879

- Sonar: side-scan sonar.
- 1,170 real sonar images collected using a Teledyne Marine Gavia AUV.
- Images are annotated for NOMBO (non-mine-like bottom objects) and MILCO (mine-like contacts).
- License: **CC BY 4.0**.
- Size listed by Figshare: about 585 MB.
- **Status for our project:** strong candidate for real SSS training/robustness experiments; attribution required.

## 5. SWDD — Sonar Wall Detection Dataset

Source: https://zenodo.org/records/13692547

- Sonar: Klein 3500 side-scan sonar on a LAUV.
- Version 2 includes SWDD, SWDD-Validation and SWDD-Adversarial material.
- Original SWDD contains wall/noWall annotations; the v2 record also provides validation and adversarial variants.
- COCO annotations are used.
- v2 archive is listed as about 5.3 GB.
- The record is public on Zenodo, but the accessible metadata does not clearly expose a specific reuse license in the page result we verified.
- **Status for our project:** useful for SSS robustness/domain research, but confirm rights before redistribution.

## Recommended first training set

1. **Side-scan sonar mine dataset (CC BY 4.0)** — safest verified reusable SSS source.
2. **Forward-looking mines/debris YOLO dataset** — useful for quickly establishing an object-detection baseline, with underlying-data rights checked separately.
3. **Marine Debris FLS** — especially valuable because it contains real sonar marine-debris imagery and bounding boxes, but its data license needs confirmation.
4. **SWDD** — useful as a domain/robustness dataset, not as a ghost-net dataset.

## Important ghost-net limitation

None of the verified sources above is a dedicated, large-scale ghost-net sonar dataset. They are useful for transfer learning, marine-debris detection, sonar-domain pretraining and robustness, but we will still need genuine ghost-net sonar examples for a reliable ghost-net detector.
