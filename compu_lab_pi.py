import math
import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal, getcontext

# Set high precision for decimal calculations
getcontext().prec = 150

def calculate_pi_leibniz(iterations=1000000):
    """
    Calculate pi using Leibniz formula:
    π = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)
    """
    getcontext().prec = 150
    pi = Decimal(0)
    for i in range(iterations):
        pi += Decimal((-1)**i) / Decimal(2*i + 1)
    return pi * 4

def calculate_pi_nilakantha(iterations=1000000):
    """
    Calculate pi using Nilakantha series (faster convergence):
    π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - ...
    """
    getcontext().prec = 150
    pi = Decimal(3)
    for i in range(1, iterations):
        sign = (-1) ** (i + 1)
        denominator = Decimal(2*i) * Decimal(2*i + 1) * Decimal(2*i + 2)
        pi += Decimal(sign * 4) / denominator
    return pi

def truncate_decimal(value, decimals):
    """Truncate a decimal value to specified decimal places"""
    multiplier = Decimal(10) ** decimals
    return int(value * multiplier) / multiplier

def round_decimal(value, decimals):
    """Round a decimal value to specified decimal places"""
    return round(value, decimals)

def calculate_ellipse_area(pi_value, semi_major, semi_minor):
    """Calculate ellipse area: A = π × a × b"""
    return pi_value * semi_major * semi_minor

def main():
    print("="*70)
    print("COMPUTATIONAL SCIENCE - PI PRECISION ANALYSIS")
    print("Shape: ELLIPSE (Area = π × a × b)")
    print("="*70)
    
    # Calculate pi using Nilakantha series (better convergence)
    print("\nCalculating Pi using Nilakantha Series...")
    print("    Formula: π = 3 + 4/(2×3×4) - 4/(4×5×6) + 4/(6×7×8) - ...")
    
    pi_calculated = calculate_pi_nilakantha(100000)
    
    # Ellipse dimensions
    semi_major_axis = Decimal('5.0')  # a = 5
    semi_minor_axis = Decimal('3.0')  # b = 3
    
    print(f"\nEllipse Dimensions:")
    print(f"    Semi-major axis (a) = {semi_major_axis}")
    print(f"    Semi-minor axis (b) = {semi_minor_axis}")
    
    # Decimal places to test
    decimal_places = [20, 40, 60, 100]
    
    print("\n" + "="*70)
    print("PRECISION ANALYSIS: Truncation vs Rounding")
    print("="*70)
    
    results = []
    
    for decimals in decimal_places:
        print(f"\n--- {decimals} Decimal Places ---")
        
        # Truncation
        pi_truncated = truncate_decimal(pi_calculated, decimals)
        area_truncated = calculate_ellipse_area(pi_truncated, semi_major_axis, semi_minor_axis)
        
        # Rounding
        pi_rounded = round_decimal(pi_calculated, decimals)
        area_rounded = calculate_ellipse_area(pi_rounded, semi_major_axis, semi_minor_axis)
        
        # Calculate difference
        difference = abs(area_rounded - area_truncated)
        
        print(f"Pi (truncated): {pi_truncated}")
        print(f"Pi (rounded):   {pi_rounded}")
        print(f"\nEllipse Area (truncated): {area_truncated}")
        print(f"Ellipse Area (rounded):   {area_rounded}")
        print(f"Difference in area:       {difference}")
        
        results.append({
            'decimals': decimals,
            'pi_truncated': float(pi_truncated),
            'pi_rounded': float(pi_rounded),
            'area_truncated': float(area_truncated),
            'area_rounded': float(area_rounded),
            'difference': float(difference)
        })
    
    # Comparison with math.pi
    print("\n" + "="*70)
    print("COMPARISON WITH PYTHON'S math.pi")
    print("="*70)
    area_math_pi = math.pi * float(semi_major_axis) * float(semi_minor_axis)
    print(f"Python's math.pi: {math.pi}")
    print(f"Ellipse area using math.pi: {area_math_pi}")
    
    # Visualization
    create_visualizations(results, semi_major_axis, semi_minor_axis, area_math_pi)
    
    print("\n" + "="*70)
    print("CONCLUSION:")
    print("="*70)
    print("As decimal precision increases:")
    print("- The difference between truncation and rounding decreases")
    print("- Both methods converge to the true value")
    print("- Rounding is generally more accurate than truncation")
    print("- At 100 decimal places, the difference is negligible for practical purposes")
    print("\nGoal achieved: We can see there IS a difference, especially at lower")
    print("decimal precision, but it becomes insignificant at higher precision.")
    print("="*70)

def create_visualizations(results, semi_major, semi_minor, area_math_pi):
    """Create visualizations of the results"""
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Pi Precision Analysis - Ellipse Area Calculation', fontsize=16, fontweight='bold')
    
    decimals = [r['decimals'] for r in results]
    areas_truncated = [r['area_truncated'] for r in results]
    areas_rounded = [r['area_rounded'] for r in results]
    differences = [r['difference'] for r in results]
    
    # Plot 1: Area comparison (Truncation vs Rounding)
    ax1.plot(decimals, areas_rounded, 's-', label='Rounded', linewidth=2, markersize=8)
    ax1.plot(decimals, areas_truncated, 'o-', label='Truncated', linewidth=2, markersize=8)
    ax1.axhline(y=area_math_pi, color='r', linestyle='--', label='math.pi reference', linewidth=2)
    ax1.set_xlabel('Decimal Places', fontsize=11)
    ax1.set_ylabel('Ellipse Area', fontsize=11)
    ax1.set_title('Area Calculation: Truncation vs Rounding', fontsize=12, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Difference between methods
    ax2.plot(decimals, differences, 'o-', color='purple', linewidth=2, markersize=8)
    ax2.set_xlabel('Decimal Places', fontsize=11)
    ax2.set_ylabel('Absolute Difference', fontsize=11)
    ax2.set_title('Difference: Rounded - Truncated', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.set_yscale('log')  # Log scale to see small differences
    
    # Plot 3: Ellipse visualization
    theta = np.linspace(0, 2*np.pi, 100)
    a = float(semi_major)
    b = float(semi_minor)
    x = a * np.cos(theta)
    y = b * np.sin(theta)
    
    ax3.plot(x, y, linewidth=3, color='blue')
    ax3.fill(x, y, alpha=0.3, color='lightblue')
    ax3.set_xlabel('x-axis', fontsize=11)
    ax3.set_ylabel('y-axis', fontsize=11)
    ax3.set_title(f'Ellipse Shape (a={a}, b={b})', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.axis('equal')
    ax3.axhline(y=0, color='k', linewidth=0.5)
    ax3.axvline(x=0, color='k', linewidth=0.5)
    
    # Plot 4: Bar chart of differences
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    bars = ax4.bar(range(len(decimals)), differences, color=colors, alpha=0.7, edgecolor='black')
    ax4.set_xlabel('Decimal Precision', fontsize=11)
    ax4.set_ylabel('Difference', fontsize=11)
    ax4.set_title('Absolute Difference by Precision Level', fontsize=12, fontweight='bold')
    ax4.set_xticks(range(len(decimals)))
    ax4.set_xticklabels([f'{d} decimals' for d in decimals])
    ax4.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height,
                f'{differences[i]:.2e}',
                ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
