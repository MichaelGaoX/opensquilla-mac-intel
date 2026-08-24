import ssl
import sys

_DESKTOP_CA_PROBE_ARG = "--_desktop-ca-probe"
_DESKTOP_CA_PROBE_OK = "opensquilla-desktop-ca-store-ok"
_SANDBOX_FILESYSTEM_WORKER_ARG = "--_sandbox-filesystem-worker"
_INTERNAL_CHILD_ARG = "--internal-child"


def _run_desktop_ca_probe() -> int:
    try:
        context = ssl.create_default_context()
        ca_certificate_count = len(context.get_ca_certs(binary_form=True))
    except Exception:
        ca_certificate_count = 0

    if ca_certificate_count <= 0:
        print(
            "OpenSquilla Desktop TLS trust probe found no trusted CA certificates.",
            file=sys.stderr,
        )
        return 1

    print(f"{_DESKTOP_CA_PROBE_OK} x509_ca={ca_certificate_count}")
    return 0

if __name__ == "__main__":
    if sys.argv[1:] == [_DESKTOP_CA_PROBE_ARG]:
        raise SystemExit(_run_desktop_ca_probe())

    if sys.argv[1:] == [_SANDBOX_FILESYSTEM_WORKER_ARG]:
        from opensquilla.sandbox.runtime_launcher import dispatch_internal_child

        raise SystemExit(dispatch_internal_child(["filesystem-worker", "-"]))

    if len(sys.argv) >= 3 and sys.argv[1] == _INTERNAL_CHILD_ARG:
        from opensquilla.sandbox.runtime_launcher import dispatch_internal_child

        raise SystemExit(dispatch_internal_child(sys.argv[2:]))

    # Frozen (PyInstaller) environment: process-tree helpers are spawned with
    # arguments directly on sys.executable (the bootloader).  Dispatch to
    # process_tree._main() which understands --posix-group-anchor and
    # --posix-owned-launch.
    _PROCESS_TREE_ARGS = ("--posix-group-anchor", "--posix-owned-launch")
    if sys.argv[1:2] and sys.argv[1] in _PROCESS_TREE_ARGS:
        from opensquilla.process_tree import _main as _process_tree_main

        raise SystemExit(_process_tree_main())

    if len(sys.argv) == 3 and sys.argv[1] == "--elevated-helper":
        from opensquilla.sandbox.backend.windows_default_setup import (
            elevated_setup_helper_main,
        )

        raise SystemExit(elevated_setup_helper_main(sys.argv[1:]))

    from opensquilla.cli.main import app

    app()
