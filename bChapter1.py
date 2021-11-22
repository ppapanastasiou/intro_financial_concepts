import numpy_financial
import numpy as np

# added one line

# Growth and rate of return
# Growth and Rate of Return are two concepts that are ubiquitous throughout the financial world.
# Recall that the cumulative returns from investing $100 in an asset that grows at 5% per year, over a 2 year period can be calculated as:

# Calculate the future value for the first investment
future_value = 100*(1 + 0.06)**(30)
print("Future Value of Investment: " + str(round(future_value, 2)))

# Compound interest
# As you saw in the previous exercise, both time and the rate of return are very important variables when forecasting the future value of an investment.
#
# Another important variable is the number of compounding periods, which can greatly affect compounded returns over time.

# Predefined variables
initial_investment = 100
growth_periods = 30
growth_rate = 0.06

# Calculate the value for the investment compounded once per year
compound_periods_1 = 1
investment_1 = initial_investment*(1 + growth_rate / compound_periods_1)**(compound_periods_1*growth_periods)
print("Investment 1: " + str(round(investment_1, 2)))

# Calculate the value for the investment compounded quarterly
compound_periods_2 = 4
investment_2 = initial_investment*(1 + growth_rate / compound_periods_2)**(compound_periods_2*growth_periods)
print("Investment 2: " + str(round(investment_2, 2)))

# Calculate the value for the investment compounded monthly
compound_periods_3 = 12
investment_3 = initial_investment*(1 + growth_rate / compound_periods_3)**(compound_periods_3*growth_periods)
print("Investment 3: " + str(round(investment_3, 2)))

# Discount factors and depreciation
# Unfortunately, not everything grows in value over time.
#
# In fact, many assets depreciate, or lose value over time.
# To simulate this, you can simply assume a negative expected rate of return.
#
# Example:
#
# Calculate the final depreciated value of an initially $10,000 car which
# declines in value by 3% per year for 10 years:

# Calculate the future value
initial_investment = 100
growth_rate = -0.05
growth_periods = 10
future_value = initial_investment*(1 + growth_rate)**(growth_periods)
print("Future value: " + str(round(future_value, 2)))


# Present value
# Luckily for you, there is a module called numpy which contains many functions which will make your life much easier when working with financial values.
#
# The .pv(rate, nper, pmt, fv) function, for example, allows you to calculate the present value of an investment as before with a few simple parameters:
#
# rate: The rate of return of the investment
# nper: The lifespan of the investment
# pmt: The (fixed) payment at the beginning or end of each period (which is 0 in our example)
# fv: The future value of the investment
# You can use this formula in many ways. For example, you can calculate the present value of future investments in today's dollars.

# Import numpy as np


# Calculate investment_1
investment_1 = numpy_financial.pv(rate=0.03, nper=15, pmt=0, fv=10000)

# Note that the present value returned is negative, so we multiply the result by -1
print("Investment 1 is worth " + str(round(-investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = numpy_financial.pv(rate=0.05, nper=10, pmt=0, fv=10000)
print("Investment 2 is worth " + str(round(-investment_2, 2)) + " in today's dollars")


# Future value
# The numpy module also contains a similar function, .fv(rate, nper, pmt, pv), which allows you to calculate the future value of
# an investment as before with a few simple parameters:
#
# rate: The rate of return of the investment
# nper: The lifespan of the investment
# pmt: The (fixed) payment at the beginning or end of each period (which is 0 in our example)
# pv: The present value of the investment
# It is important to note that in this function call, you must pass a negative value into the pv parameter if it
# represents a negative cash flow (cash going out). In other words, if you were to compute the future value of an investment,
# requiring an up-front cash payment, you would need to pass a negative value to the pv parameter in the .fv() function.

# Calculate investment_1
investment_1 = numpy_financial.fv(rate=0.05, nper=15, pmt=0, pv=-10000)
print("Investment 1 will yield a total of $" + str(round(investment_1, 2)) + " in 15 years")

# Calculate investment_2
investment_2 = numpy_financial.fv(rate=0.08, nper=15, pmt=0, pv=-10000)
print("Investment 2 will yield a total of $" + str(round(investment_2, 2)) + " in 15 years")

# Adjusting future values for inflation
# You can now put together what you learned in the previous exercises by following a simple methodology:
#
# First, forecast the future value of an investment given a rate of return
# Second, discount the future value of the investment by a projected inflation rate
# The methodology above will use both the .fv() and .pv() functions to arrive at the projected value of a
# given investment in today's dollars, adjusted for inflation.

# Calculate investment_1
investment_1 = numpy_financial.fv(rate=0.08, nper=10, pmt=0, pv=-10000)
print("Investment 1 will yield a total of $" + str(round(investment_1, 2)) + " in 10 years")

# Calculate investment_2
investment_1_discounted = numpy_financial.pv(rate=0.03, nper=10, pmt=0, fv=investment_1)
print("After adjusting for inflation, investment 1 is worth $" + str(round(-investment_1_discounted, 2)) + " in today's dollars")


# Discounting cash flows
# You can use numpy's net present value function numpy.npv(rate, values) to calculate the net present value of
# a series of cash flows. You can create these cash flows by using a numpy.array([...]) of values.
#
# Compute the NPV of the same cash flows from the following project, but assuming different discount rates:

# Predefined array of cash flows
cash_flows = numpy_financial.array([100, 100, 100, 100, 100])

# Calculate investment_1
investment_1 = numpy_financial.npv(rate=0.03, values=cash_flows)
print("Investment 1's net present value is $"+str(round(investment_1,2))+" in today's dollars")

# Calculate investment_2
investment_2 = numpy_financial.npv(rate=0.05, values=cash_flows)
print("Investment 2's net present value is $"+str(round(investment_2,2))+" in today's dollars")

# Calculate investment_3
investment_3 = numpy_financial.npv(rate=0.07, values=cash_flows)
print("Investment 3's net present value is $"+str(round(investment_3,2))+" in today's dollars")

# Initial project costs
# The numpy.npv(rate, values) function is very powerful because it allows you to pass in both positive and negative values.
#
# For this exercise, you will calculate the net present value of two potential projects with different cash flows:


# Create an array of cash flows for project 1
cash_flows_1 = np.array([-250, 100, 200, 300, 400])

# Create an array of cash flows for project 2
cash_flows_2 = np.array([-250, 300, -250, 300, 300])

# Calculate the net present value of project 1
investment_1 = numpy_financial.npv(rate=0.03, values=cash_flows_1)
print("The net present value of Investment 1 is worth $" + str(round(investment_1, 2)) + " in today's dollars")

# Calculate the net present value of project 2
investment_2 = numpy_financial.npv(rate=0.03, values=cash_flows_2)
print("The net present value of Investment 2 is worth $" + str(round(investment_2, 2)) + " in today's dollars")

# Diminishing cash flows
# Remember how compounded returns grow rapidly over time? Well, it works in the reverse, too. Compounded discount factors over time will quickly shrink a number towards zero.
# For example, $100 at a 3% annual discount for 1 year is still worth roughly $97.08:
# But this number shrinks quite rapidly as the number of discounting periods increases:
# This means that the longer in the future your cash flows will be received (or paid), the close to 0 that number will be.

# Calculate investment_1
investment_1 = numpy_financial.pv(rate=0.03, nper=30, pmt=0, fv=100)
print("Investment 1 is worth $" + str(round(-investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = numpy_financial.pv(rate=0.03, nper=50, pmt=0, fv=100)
print("Investment 2 is worth $" + str(round(-investment_2, 2)) + " in today's dollars")

# Calculate investment_3
investment_3 = numpy_financial.pv(rate=0.03, nper=100, pmt=0, fv=100)
print("Investment 3 is worth $" + str(round(-investment_3, 2)) + " in today's dollars")