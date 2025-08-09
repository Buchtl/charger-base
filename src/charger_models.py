from dataclasses import dataclass

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
    tma: list[float]
    fhz: float
