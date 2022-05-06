weight = 4.8

# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
elif weight > 10:
  cost_ground = weight * 4.75 + 20

print("Ground shipping: ", cost_ground)

# Premium Ground Shipping
cost_premium_ground = 125

print("Premium ground shipping: ", cost_premium_ground)

# Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5 + 0
elif weight <= 6:
  cost_drone = weight * 9 + 0
elif weight <= 10:
  cost_drone = weight * 12 + 0
elif weight > 10:
  cost_drone = weight * 14.25 + 0

print("Drone shipping: ", cost_drone)
