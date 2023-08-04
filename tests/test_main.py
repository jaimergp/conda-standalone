import os
import subprocess
import sys

CONDA_EXE = os.environ.get(
    "CONDA_STANDALONE",
    os.path.join(sys.prefix, "standalone_conda", "conda.exe")
)


def run_conda(*args, **kwargs):
    return subprocess.run([CONDA_EXE, *args], **kwargs)


def test_new_environment(tmp_path):
    p = run_conda("create", "-p", tmp_path / "env", "-y", "-c", "conda-forge", "libzlib")
    p.check_returncode()
    assert list((tmp_path / "env" / "conda-meta").glob("libzlib-*.json"))
