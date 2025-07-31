from dataclasses import dataclass


@dataclass
class Cdi:
    """
    type (int): charging duration info (null=no charging in progress, type=0 counter going up, type=1 duration in ms
    value (int): type=0 counter going up, type=1 duration in ms
    """

    type: int
    value: int


@dataclass
class ErrorStatus:
    err: int


# energy_total, measured in Wh
@dataclass
class StatusPoll:
    """
    Represents the API response for polling
    Attributes:
        eto (int): Energy total (in Wh).
        err (int): Error code (0 means no error).
    """

    eto: int
    err: int
