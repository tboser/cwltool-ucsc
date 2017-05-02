# Stubs for io

# Based on https://docs.python.org/2/library/io.html

# Only a subset of functionality is included.

DEFAULT_BUFFER_SIZE = 0

from typing import (AnyStr, List, BinaryIO, TextIO, IO, overload, Iterator,
	Iterable, Any, Union)

def open(file: Union[str, unicode, int],
         mode: unicode = ..., buffering: int = ..., encoding: unicode = ...,
         errors: unicode = ..., newline: unicode = ...,
         closefd: bool = ...) -> IO[Any]: ...

class IOBase:
    # TODO
    ...

class BytesIO(BinaryIO):
    def __init__(self, initial_bytes: str = ...) -> None: ...
    # TODO getbuffer
    # TODO see comments in BinaryIO for missing functionality
    def close(self) -> None: ...
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def read(self, n: int = ...) -> str: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = ...) -> str: ...
    def readlines(self, hint: int = ...) -> List[str]: ...
    def seek(self, offset: int, whence: int = ...) -> None: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int = ...) -> int: ...
    def writable(self) -> bool: ...
    def write(self, s: AnyStr) -> None: ...
    def writelines(self, lines: Iterable[str]) -> None: ...
    def getvalue(self) -> str: ...
    def read1(self) -> str: ...

    def __iter__(self) -> Iterator[str]: ...
    def __enter__(self) -> 'BytesIO': ...
    def __exit__(self, type, value, traceback) -> bool: ...

class StringIO(TextIO):
    def __init__(self, initial_value: unicode = ...,
                 newline: unicode = ...) -> None: ...
    # TODO see comments in BinaryIO for missing functionality
    def close(self) -> None: ...
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def read(self, n: int = ...) -> unicode: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = ...) -> unicode: ...
    def readlines(self, hint: int = ...) -> List[unicode]: ...
    def seek(self, offset: int, whence: int = ...) -> None: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int = ...) -> int: ...
    def writable(self) -> bool: ...
    def write(self, s: unicode) -> None: ...
    def writelines(self, lines: Iterable[unicode]) -> None: ...
    def getvalue(self) -> unicode: ...

    def __iter__(self) -> Iterator[unicode]: ...
    def __enter__(self) -> 'StringIO': ...
    def __exit__(self, type, value, traceback) -> bool: ...

class TextIOWrapper(TextIO):
    # write_through is undocumented but used by subprocess
    def __init__(self, buffer: IO[str], encoding: unicode = ...,
                 errors: unicode = ..., newline: unicode = ...,
                 line_buffering: bool = ...,
                 write_through: bool = ...) -> None: ...
    # TODO see comments in BinaryIO for missing functionality
    def close(self) -> None: ...
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def read(self, n: int = ...) -> unicode: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = ...) -> unicode: ...
    def readlines(self, hint: int = ...) -> List[unicode]: ...
    def seek(self, offset: int, whence: int = ...) -> None: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int = ...) -> int: ...
    def writable(self) -> bool: ...
    def write(self, s: unicode) -> None: ...
    def writelines(self, lines: Iterable[unicode]) -> None: ...

    def __iter__(self) -> Iterator[unicode]: ...
    def __enter__(self) -> StringIO: ...
    def __exit__(self, type, value, traceback) -> bool: ...

class BufferedIOBase(IOBase): ...
