years_of_exp = c(7,5,1,3)
salary_in_lakhs = c(21,13,6,8)
#employee.data = data.frame(satisfaction_score, years_of_exp, salary_in_lakhs)
employee.data = data.frame(years_of_exp, salary_in_lakhs)
employee.data
# Estimation of the salary of an employee, based on his year of experience and satisfaction score in his company.
model <- lm(salary_in_lakhs ~ years_of_exp, data = employee.data)
summary(model)
# The formula of Regression becomes
# Y = 2 + 2.5*year_of_Exp
# Visualization of Regression
plot(salary_in_lakhs ~ years_of_exp, data = employee.data)
abline(model)