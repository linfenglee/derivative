from dataclasses import dataclass

@dataclass
class MarketInfo(object):
    """
    Record Market Information
    """

    underlying_price: float
    volatility: float
    interest_rate: float
    dividend_rate: float


@dataclass
class EuropeanOptionInfo(object):
    """
    Record European Option Information
    """

    option_type: str
    strike: float
    time_to_maturity: float



if __name__ == "__main__":
    pass