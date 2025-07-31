from dataclasses import dataclass


@dataclass
class error_status:
    err: int


@dataclass
class status_poll:
    eto: int
    err: int
