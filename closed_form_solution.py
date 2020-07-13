import numpy as np
import pandas as pd

from scipy.stats import norm

from derivative_objects import *

class EuropeanOptionPricer(object):
    def __init__(self, market_info, euro_option_info):
        self.S0 = market_info.underlying_price
        self.sigma = market_info.volatility
        self.r = market_info.interest_rate
        self.q = market_info.dividend_rate
        self.option_type = euro_option_info.option_type
        self.K = euro_option_info.strike
        self.T = euro_option_info.time_to_maturity


    def __str__(self):
        info = """
        ------------------------
        Underlying Price: {}
        Strike: {}
        Volatility: {}
        Interest Rate: {}
        Dividend Rate: {}
        Time-to-Maturity: {}
        ------------------------
        """.format(self.S0, self.K, self.sigma, self.r, self.q, self.T)
        return info

    def get_d(self):
        sigma_sqrtT = self.sigma * np.sqrt(self.T)
        d1 = (np.log(self.S0/self.K) + (self.r - self.q) * self.T) / sigma_sqrtT + 0.5 * sigma_sqrtT
        d2 = d1 - sigma_sqrtT
        return d1, d2

    def NPV(self):
        d1, d2 = self.get_d()
        if self.option_type == "C":
            lhs = self.S0 * np.exp(-self.q * self.T) * norm.cdf(d1)
            rhs = self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
        else:
            lhs = self.K * np.exp(-self.r * self.T) * norm.cdf(-d2)
            rhs = self.S0 * np.exp(-self.q * self.T) * norm.cdf(-d1)
        value = lhs - rhs
        return value

    def delta(self):
        d1, _ = self.get_d()
        if self.option_type == "C":
            return np.exp(-self.q * self.T) * norm.cdf(d1)
        else:
            return -np.exp(-self.q * self.T) * norm.cdf(-d1)

    def vega(self):
        
        pass

    def gamma(self):
        d1, _ = self.get_d()
        sigma_sqrtT = self.sigma * np.sqrt(self.T)
        return np.exp(-self.q * self.T) * norm.cdf(d1) / self.S0 / sigma_sqrtT

    def theta(self):
        pass

    def rho(self):
        pass


if __name__ == "__main__":
    market_info = MarketInfo(100, 0.3, 0.05, 0.01)
    option_info = EuropeanOptionInfo("C", 100, 1)
    call_option = EuropeanOptionPricer(market_info, option_info)
    print(call_option)
    print(call_option.NPV())



