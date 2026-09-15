"""Security audit PoC plugin (canary).

If this module is ever imported by the hermes gateway plugin loader,
it drops a single canary marker file to evidence in-process execution.
It performs no other action, reads no secrets, and makes no network calls.
Installed with --no-enable during the audit, so it is never loaded.
"""

from pathlib import Path

_CANARY = Path("/tmp/hermes_audit_poc_plugin_loaded")

try:
    _CANARY.write_text("audit-poc-plugin was imported in-process\n")
except Exception:
    pass
