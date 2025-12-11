"""
FintorAI Python Trading Bot Starter
----------------------------------
Minimal entrypoint for running a config-driven trading bot.

This is intentionally simple:
- loads a YAML settings file
- prints the parsed config
- placeholder where exchange + strategy engines will plug in later
"""

import argparse
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    yaml = None


def load_settings(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Settings file not found: {path}")

    if yaml is None:
        raise ImportError(
            "PyYAML is not installed. Run 'pip install -r requirements.txt' first."
        )

    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="FintorAI Python Trading Bot Starter"
    )
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        default="config/settings_example.yaml",
        help="Path to YAML settings file (default: config/settings_example.yaml)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config_path = Path(args.config)

    try:
        settings = load_settings(config_path)
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)

    # For now we just print a short summary.
    # Later this is where we will:
    #  - init exchanges
    #  - load strategy module
    #  - start the execution loop
    print("✅ Settings file loaded successfully.")
    print(f"   Path : {config_path}")
    print(f"   Bot  : {settings.get('bot', {}).get('name', 'Unknown bot')}")
    print(f"   Mode : {settings.get('bot', {}).get('mode', 'N/A')}")

    # Placeholder hook for future expansion
    print("\n[TODO] Plug in execution engine, exchanges, and strategy here.")


if __name__ == "__main__":
    main()
