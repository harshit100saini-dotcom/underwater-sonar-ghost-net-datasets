# Dataset acquisition status

## Current status

- Repository structure: READY
- Verified SSS source: READY
- Actual third-party images in GitHub: NOT UPLOADED
- Local download script: READY
- YOLO conversion: NEXT STEP

## First dataset to acquire

**Side-scan sonar imaging for Mine detection** (Figshare article 24574879)

- 1,170 real SSS images
- ~584.99 MB
- Teledyne Marine Gavia AUV
- Annotated
- CC BY 4.0

The dataset is intentionally downloaded from its official Figshare source rather than copied into GitHub. Run:

```bash
python datasets/DOWNLOAD_SSS_MINE_DATASET.py
```

This will place the downloaded files under `data/raw/sss-mine-detection/`.
