from py import path as path, process as process
from py._path import common as common, svnwc as svncommon
from py._path.cacheutil import AgingCache as AgingCache, BuildcostAccessCache as BuildcostAccessCache
from typing import Any, Optional

DEBUG: bool

class SvnCommandPath(svncommon.SvnPathBase):
    strpath: Any = ...
    rev: Any = ...
    auth: Any = ...
    def __new__(cls, path: Any, rev: Optional[Any] = ..., auth: Optional[Any] = ...): ...
    def open(self, mode: str = ...): ...
    def dirpath(self, *args: Any, **kwargs: Any): ...
    def mkdir(self, *args: Any, **kwargs: Any): ...
    def copy(self, target: Any, msg: str = ...) -> None: ...
    def rename(self, target: Any, msg: str = ...) -> None: ...
    def remove(self, rec: int = ..., msg: str = ...) -> None: ...
    def export(self, topath: Any): ...
    def ensure(self, *args: Any, **kwargs: Any): ...
    def info(self): ...
    def listdir(self, fil: Optional[Any] = ..., sort: Optional[Any] = ...): ...
    def log(self, rev_start: Optional[Any] = ..., rev_end: int = ..., verbose: bool = ...): ...

class InfoSvnCommand:
    lspattern: Any = ...
    kind: str = ...
    created_rev: Any = ...
    last_author: Any = ...
    size: Any = ...
    mtime: Any = ...
    time: Any = ...
    def __init__(self, line: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...

def parse_time_with_missing_year(timestr: Any): ...

class PathEntry:
    strpath: Any = ...
    action: Any = ...
    copyfrom_path: Any = ...
    copyfrom_rev: Any = ...
    def __init__(self, ppart: Any) -> None: ...
