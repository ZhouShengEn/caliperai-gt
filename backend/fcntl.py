"""Windows compatibility shim for the Unix-only `fcntl` module.

CaliperGT's segmentation endpoint uses fcntl.flock() as a cross-process file
lock, which does not exist on Windows. This shim provides no-op equivalents so
the backend can run natively on Windows for local/demo deployments.

Scope: single-process demo usage. The lock degrades to a no-op (same behaviour
as the Docker single-worker case for this code path).
"""

LOCK_SH = 1
LOCK_EX = 2
LOCK_NB = 4
LOCK_UN = 8


def flock(fd, operation):
    return None


def lockf(fd, operation, length=0, start=0, whence=0):
    return None
