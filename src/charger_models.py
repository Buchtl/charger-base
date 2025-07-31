from dataclasses import dataclass


@dataclass
class error_status:
    err: int


# energy_total, measured in Wh
@dataclass
class status_poll:
    """
    Represents the API response for polling
    Attributes:
        eto (int): Energy total (in Wh).
        err (int): Error code (0 means no error).
    """
    eto: int
    err: int
