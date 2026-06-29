"""CLI entry point for grg."""

import subprocess
import sys
import signal

from .translator import translate_grep_args

try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except AttributeError:
    pass


def main():
    """Main entry point - translate grep args and run rg."""
    grep_args = sys.argv[1:]
    rg_args = translate_grep_args(grep_args)
    
    result = subprocess.run(["rg"] + rg_args)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
