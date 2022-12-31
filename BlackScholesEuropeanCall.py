import math

def black_scholes_call(S, K, T, r, sigma):
  """
  Calculates the Black-Scholes price of a European call option.
  
  Parameters:
  S (float): the current price of the underlying asset
  K (float): the strike price of the option
  T (float): the time until expiration of the option, in years
  r (float): the risk-free interest rate
  sigma (float): the implied volatility of the underlying asset
  
  Returns:
  float: the Black-Scholes price of the call option
  """
  # Calculate the d1 and d2 terms
  d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
  d2 = d1 - sigma * math.sqrt(T)
  
  # Calculate the Black-Scholes price using the cumulative standard normal distribution function
  call_price = S * math.erf(d1) - K * math.exp(-r * T) * math.erf(d2)
  
  return call_price

# Example usage
S = 100  # underlying asset price
K = 105  # strike price
T = 0.5  # time until expiration (in years)
r = 0.1  # risk-free interest rate
sigma = 0.2  # implied volatility
call_price = black_scholes_call(S, K, T, r, sigma)
print(f"The Black-Scholes price of the call option is {call_price:.2f}")
