#AND
# TRUTH table
# 0 0 0
# 0 1 0 
# 1 0 0
# 1 1 1
# OR
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 1

alpha=True
beta=False
print (alpha and beta) 
print(alpha or beta)

#Income
income=55000
credit_score=650
if income >65000 or credit_score >=650:
    print("Loan eligible")
else:
    print("Not Eligible")   

#Not Gate
login_in=False
if not login_in:
    print("Please log in")

