critical = 2
high = 3
medium = 5

risk_score = (critical * 10) + (high * 7) + (medium * 3)

print("Risk Score:", risk_score)

if risk_score > 30:
    print("Deployment Blocked")
else:
    print("Deployment Allowed")
