import numpy_financial
import numpy as np

# Project proposals and cash flows projections
# Your project managers have projected the cash flows for each of the proposals.
#
# Project 1 provides higher short term cash flows, but Project 2 becomes more profitable over time.
#
# The cash flow projections for both projects are as follows:

# Create a numpy array of cash flows for Project 1
cf_project_1 = np.array([-1000, 200, 250, 300, 350, 400, 450, 500, 550, 600])

# Create a numpy array of cash flows for Project 2
cf_project_2 = np.array([-1000, 150, 225, 300, 375, 425, 500, 575, 600, 625])

# Scale the original objects by 1000x
cf_project1 = cf_project_1 * 1000
cf_project2 = cf_project_2 * 1000

# Internal Rate of Return
# Now that you have the cash flow projections ready to go for each project, you want to compare the internal rate of return (IRR) of each project to help you decide which project would be most beneficial for your company in terms of yield (rate of return). In this exercise, you will calculate the internal rate of return for each project using np.irr(values).
#
# The cash flows for projects 1 and 2 are available as cf_project1 and cf_project2.


# Calculate the internal rate of return for Project 1
irr_project1 = numpy_financial.irr(cf_project1)
print("Project 1 IRR: " + str(round(100*irr_project1, 2)) + "%")

# Calculate the internal rate of return for Project 2
irr_project2 = numpy_financial.irr(cf_project2)
print("Project 2 IRR: " + str(round(100*irr_project2, 2)) + "%")


# Debt and equity financing
# In the previous chapter, you were able to assume that your discount rate for the NPV calculation was solely based on a measure such as inflation.
#
# However, in this chapter, you are the CEO of a new company that has outstanding debt and financing costs, which you will have to adjust for.
#
# You will use the WACC as your discount rate in upcoming exercises.
#
# For this exercise, assume you take out a $1,000,000 loan to finance the project, which will be your company's only outstanding debt. This loan will represent 50% of your company's total financing of $2,000,000. The remaining funding comes from the market value of equity.

# Set the market value of debt
mval_debt = 1000000

# Set the market value of equity
mval_equity = 1000000

# Compute the total market value of your company's financing
mval_total = mval_debt + mval_equity

# Compute the proportion of your company's financing via debt
percent_debt = mval_debt / mval_total
print("Debt Financing: " + str(round(100*percent_debt, 2)) + "%")

# Compute the proportion of your company's financing via equity
percent_equity = mval_equity / mval_total
print("Equity Financing: " + str(round(100*percent_equity, 2)) + "%")


# Calculating WACC
# In addition to determining the proportion of both equity and debt financing, you will need to estimate the cost of financing via
# both debt and equity in order to estimate your WACC.
#
# The cost of debt financing can be estimated as the amount you will have to pay on a new loan.
# This can be estimated by looking at the interest rates of loans of similar sizes to similar companies, or could be
# based on previous loans your company may already have been issued.
#
# The cost of equity financing can be estimated as the return on equity of similar companies. Calculating the return
# on equity is a simple accounting exercise, but all you need to know is that essentially, investors will require a rate
# of return that is close to what could be earned by a similar investment.


# The proportion of debt vs equity financing is predefined
percent_debt = 0.50
percent_equity = 0.50

# Set the cost of equity
cost_equity = 0.18

# Set the cost of debt
cost_debt = 0.12

# Set the corporate tax rate
tax_rate = 0.35

# Calculate the WACC
wacc = (percent_equity*cost_equity) + (percent_debt*cost_debt) * (1 - tax_rate)
print("WACC: " + str(round(100*wacc, 2)) + "%")

# Two project with different lifespans
# The board of the company has decided to go a different direction, involving slightly shorter term projects and lower initial investments.
#
# Your project managers have come up with two new ideas, and projected the cash flows for each of the proposals.
#
# Project 1 has a lifespan of 8 years, but Project 2 only has a lifespan of 7 years. Project 1 requires an initial investment of $700,000, but Project 2 only requires $400,000.
#
# The cash flow projections for both projects are as follows:

# Create a numpy array of cash flows for Project 1
cf_project_1 = np.array([-700, 100, 150, 200, 250, 300, 350, 400])

# Create a numpy array of cash flows for Project 2
cf_project_2 = np.array([-400, 50, 100, 150, 200, 250, 300])

# Scale the original objects by 1000x
cf_project1 = cf_project_1 * 1000
cf_project2 = cf_project_2 * 1000

# Calculating IRR and NPV with different project lifespans
# Now that you calculated the WACC, you can calculate and compare the IRRs and NPVs of each project.
#
# While the IRR remains relatively comparable across projects, the NPV, on the other hand, will be much more difficult to compare given the additional year required for project 1.
#
# Luckily, in the next exercise, we will introduce another method to compare the NPVs of the projects, but we will first need to compute the NPVs as before.
#
# The cash flows for projects 1 and 2 are available as cf_project1 and cf_project2.

# Calculate the IRR for Project 1
irr_project1 = numpy_financial.irr(cf_project1)
print("Project 1 IRR: " + str(round(100*irr_project1, 2)) + "%")

# Calculate the IRR for Project 2
irr_project2 = numpy_financial.irr(cf_project2)
print("Project 2 IRR: " + str(round(100*irr_project2, 2)) + "%")

# Set the wacc equal to 12.9%
wacc = 0.129

# Calculate the NPV for Project 1
npv_project1 = numpy_financial.npv(wacc, cf_project1)
print("Project 1 NPV: " + str(round(npv_project1, 2)))

# Calculate the NPV for Project 2
npv_project2 = numpy_financial.npv(wacc, cf_project2)
print("Project 2 NPV: " + str(round(npv_project2, 2)))

# Using the equivalent annual annuity approach
# Since the net present values of each project are not directly comparable given the different
# lifespans of each project, you will have to consider a different approach.
#
# The equivalent annual annuity (EAA) approach allows us to compare two projects
# by essentially assuming that each project is an investment generating a flat interest
# rate each year (an annuity), and calculating the annual payment you would receive from
# each project, discounted to present value.
#
# You can compute the EAA of each project using the .pmt(rate, nper, pv, fv) function in numpy.
#
# The weighted average cost is available as wacc, and the net present values
# for projects 1 and 2 are available as npv_project1 and npv_project2.

# Calculate the EAA for Project 1
eaa_project1 = numpy_financial.pmt(rate=wacc, nper=8, pv=-npv_project1, fv=0)
print("Project 1 EAA: " + str(round(eaa_project1, 2)))

# Calculate the EAA for Project 2
eaa_project2 = numpy_financial.pmt(rate=wacc, nper=7, pv=-npv_project2, fv=0)
print("Project 2 EAA: " + str(round(eaa_project2, 2)))