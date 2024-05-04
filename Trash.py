import numpy as np
import matplotlib.pyplot as plt

# Generator parameters
E = 100  # Generated voltage (constant)
R_a = 0.5  # Armature resistance (constant)
X_s = 1.0  # Synchronous reactance (constant)

# Power factors
lagging_pf = [0.2, 0.4, 0.6, 0.8]
leading_pf = [0.2, 0.4, 0.6, 0.8]

# Armature currents (from no-load to full-load)
I_L_values = np.linspace(0, 10, 100)

# Plot terminal characteristics for lagging power factors
plt.figure(figsize=(10, 6))
for pf in lagging_pf:
    V_t_values = E - X_s * np.sqrt(1 - pf**2) * I_L_values - R_a * pf
    plt.plot(I_L_values, V_t_values, label=f'Lagging PF={pf}')

plt.title('Terminal Characteristics (Lagging Power Factor)')
plt.xlabel('Line Current (I_L)')
plt.ylabel('Terminal Voltage (V_t)')
plt.legend()
plt.grid(True)
plt.show()

# Plot terminal characteristics for leading power factors
plt.figure(figsize=(10, 6))
for pf in leading_pf:
    V_t_values = E - X_s * np.sqrt(1 - pf**2) * I_L_values - R_a * pf
    plt.plot(I_L_values, V_t_values, label=f'Leading PF={pf}')

plt.title('Terminal Characteristics (Leading Power Factor)')
plt.xlabel('Line Current (I_L)')
plt.ylabel('Terminal Voltage (V_t)')
plt.legend()
plt.grid(True)
plt.show()
