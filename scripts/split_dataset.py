"""Create train/validation/test splits.

For sonar sequences, split by survey/sequence/location rather than randomly
splitting adjacent frames, which can cause severe data leakage.
"""


def main() -> None:
    print("Split scaffold: implement sequence/location-aware splitting for each source.")


if __name__ == "__main__":
    main()
