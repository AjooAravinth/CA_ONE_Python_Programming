import unittest


class Employee:

    def __init__(self, id, Lname, Fname, RH, HR, OTm, TC, SB):
        self.StaffID = id
        self.LastName = Lname
        self.FirstName = Fname
        self.RegHours = RH
        self.HourlyRate = HR
        self.OTMultiple = OTm
        self.TaxCredit = TC
        self.StandardBand = SB

    def computePayment(self, HoursWorked, date):

        # Regular worktime payment
        regular_pay = (self.RegHours * self.HourlyRate)

        # Overtime payment
        overtime_hr = HoursWorked - self.RegHours # overtime worked
        over_rate = self.HourlyRate * self.OTMultiple   # overtime rate
        over_pay = (overtime_hr * over_rate)    # overtime payment

        # Gross pay
        gross_pay = (regular_pay + over_pay)

        higher_rate_pay = 0
        if gross_pay > self.StandardBand:
            higher_rate_pay = (gross_pay - self.StandardBand)

        standard_tax = self.StandardBand * (20/100)
        higher_tax = higher_rate_pay * (40/100)
        total_tax = standard_tax + higher_tax
        net_tax = total_tax - self.TaxCredit
        psri = gross_pay * (4/100)
        net_deduct = psri + net_tax
        net_pay = gross_pay - net_deduct

        worked = {'name': self.FirstName + " " + self.LastName, 'Date': date, 'Hours Worked': HoursWorked,
                  'Overtime Hours Worked': overtime_hr, 'Regular Hours Worked': self.RegHours,
                  'Regular Rate': self.HourlyRate, 'Overtime Rate': over_rate, 'Regular Pay': regular_pay,
                  'Overtime Pay': over_pay, 'Gross Pay': gross_pay, 'Standard Rate Pay': self.StandardBand,
                  'Higher Rate Pay': higher_rate_pay, 'Standard Tax': standard_tax, 'Higher Tax': higher_tax,
                  'Total Tax': total_tax, 'Tax Credit': self.TaxCredit, 'Net Tax': net_tax, 'PRSI': psri,
                  'Net Deductions': net_deduct, 'Net Pay': net_pay}

        return worked


class test_func(unittest.TestCase):

    def testNetLessEqualGross(self):
        jg = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = jg.computePayment(42, '31/10/2021')
        self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])

    def testOvertimeNegative(self):
        jg = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = jg.computePayment(42, '31/10/2021')
        self.assertGreaterEqual(pi['Overtime Hours Worked'], 0)

    def testRegHr_not_exceed_HrWrked(self):
        jg = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = jg.computePayment(42, '31/10/2021')
        self.assertGreaterEqual(pi['Hours Worked'], pi['Regular Hours Worked'])

    def testHigherTaxNegative(self):
        jg = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = jg.computePayment(42, '31/10/2021')
        self.assertGreaterEqual(pi['Higher Tax'], 0)

    def testNetPayNegative(self):
        jg = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 72, 710)
        pi = jg.computePayment(42, '31/10/2021')
        self.assertGreaterEqual(pi['Net Pay'], 0)


unittest.main(argv=['ignored'], exit=False)
