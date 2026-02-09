📊 **EXPLANATION OF THE 4 VISUALIZATIONS:**

### **Top-Left: Area Calculation - Truncation vs Rounding**
- **What it shows:** How the calculated ellipse area changes with different decimal precisions
- **The lines:**
  - **Blue circles (Truncated)**: Area calculated using truncated pi values
  - **Orange squares (Rounded)**: Area calculated using rounded pi values  
  - **Red dashed line (math.pi reference)**: The "true" area using Python's built-in pi
-  Both blue and orange lines overlap almost perfectly and converge to the red reference line. This shows that at high precision, truncation and rounding give nearly identical results

### **Top-Right: Difference - Rounded - Truncated**
- **What it shows:** The absolute difference between rounding and truncating
- **Y-axis note:** It's a **logarithmic scale** (notice 10⁻⁵⁸, 10⁻⁵⁹) - this means even tiny differences can be seen
- **The spike at 60 decimals:** This is where you finally see a difference! At 60 decimal places, there's a tiny difference of 1.5 × 10⁻⁵⁹ (that's 0.0000...59 zeros...00015)
- **Key insight:** At 20, 40, and 100 decimals, the difference is essentially zero. Only at 60 decimals does a measurable (but still incredibly tiny) difference appear.

### **Bottom-Left: Ellipse Shape (a=5.0, b=3.0)**
- **What it shows:** A visual representation of your ellipse
- **Dimensions:** Semi-major axis = 5 (horizontal stretch), Semi-minor axis = 3 (vertical stretch)
- **Purpose:** Helps visualize the actual shape whose area you're calculating
- **Key insight:** This is your "shape that uses pi" - not a circle, but an ellipse!

### **Bottom-Right: Absolute Difference by Precision Level**
- **What it shows:** Bar chart comparing the differences at each precision level
- **The bars:** 
  - 20 decimals: 0.00e+00 (no difference)
  - 40 decimals: 0.00e+00 (no difference)
  - 60 decimals: **1.50e-59** (tiny difference - this is why there's a visible bar!)
  - 100 decimals: 0.00e+00 (no difference)
- **Key insight:** The 60-decimal case is special - it's the only one where rounding and truncation actually produced different results in your calculation.

---

## 📝 **EXPLANATION OF THE TEXT OUTPUT:**

### **The Nilakantha Series**
```
π = 3 + 4/(2×3×4) - 4/(4×5×6) + 4/(6×7×8) - ...
```
- This is your "another formula for pi" (requirement #1)
- It converges to pi faster than the simpler Leibniz formula
- Each term adds more precision

### **Why Only 60 Decimals Shows a Difference?**

Look closely at the **60 decimal output**:
```
Pi (truncated): ...575908635
Pi (rounded):   ...575908636  ← Last digit is different!
```

At 60 decimals, the **61st digit** was exactly 5 or higher, causing rounding to bump up the last kept digit from 5→6. This is **truncation vs rounding** in action:
- **Truncation**: Just chops off after 60 digits (keeps ...635)
- **Rounding**: Looks at the next digit and rounds up (makes it ...636)

### **Why Not at Other Precisions?**

- **20 & 40 decimals**: The digit after the cutoff wasn't high enough to cause rounding up
- **100 decimals**: So much precision that the difference becomes immeasurably small in the calculation

---

## 🎯 **ANSWERING YOUR LAB GOAL:**

**"Goal: see whether or not there's really a difference"**

**Answer: YES, there IS a difference!**

✅ **At 60 decimal places**: Clear difference of 1.5 × 10⁻⁵⁹ in the area
✅ **Truncation vs Rounding behave differently** when the next digit matters
✅ **But** for practical purposes (20-40 decimals), the difference is negligible
✅ **At very high precision (100+ decimals)**, both methods converge to the same value

---

## 💡 **KEY POINTS FOR YOUR PRESENTATION:**

1. **Shape choice**: Ellipse uses pi just like circles (A = πab instead of A = πr²)
2. **Different pi formula**: Nilakantha series (not just circumference/diameter)
3. **Precision matters**: The difference only shows up at certain decimal places
4. **Rounding is more accurate**: It considers the next digit; truncation just cuts
5. **Practical takeaway**: For most calculations, even 20 decimals is more than enough!


At which precision level does truncation vs rounding actually matter?"

Do you have any questions about specific parts you'd like me to clarify further? Maayo na ang imong lab! (Your lab is good!) 🎉
