# Model Training

## Baseline

Start with a YOLO-family object detector after the source annotations have been normalized into `configs/dataset.yaml`.

## Recommended evaluation

- Keep a held-out test set from unseen survey/location data.
- Report precision, recall, mAP50, and mAP50-95.
- Track performance separately for ghost nets, fishing gear, and generic debris.
- Inspect false positives on rocks, seabed clutter, shadows, and other man-made objects.

## Important

Do not train/evaluate on adjacent frames from the same sonar sequence across different splits. This can inflate benchmark results.
