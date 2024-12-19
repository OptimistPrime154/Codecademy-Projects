weight = 41.5
print ("Package weight is", weight)



if weight <=2:
  cost_ground =  weight * 1.50 + 20
elif weight <=6:
  cost_ground =  weight * 3.00 + 20
elif weight <=10:
  cost_ground =  weight * 4.00 + 20
elif weight >=11:
  cost_ground =  weight * 4.75 + 20

print("Ground Shipping $",cost_ground)

cost_premium_shipping = 125

print("Ground Shipping Premium $",cost_premium_shipping)

if weight <=2:
  drone_shipping =  weight * 4.50
elif weight <=6:
  drone_shipping =  weight * 9.00
elif weight <=10:
  drone_shipping =  weight * 12.00
elif weight >=11:
  drone_shipping =  weight * 14.25

print ("Drone Shipping $",drone_shipping)
