# OpenSCAD Syntax Validator

This is a quick reference for validating OpenSCAD code syntax.

## ✅ Common Syntax Errors and Fixes

### Error 1: Missing Semicolons
❌ **WRONG:**
```openscad
cylinder(h=100, d=30)
cube([50, 50, 50])
```

✅ **CORRECT:**
```openscad
cylinder(h=100, d=30);
cube([50, 50, 50]);
```

---

### Error 2: Missing $fn for Smooth Circles
❌ **WRONG:**
```openscad
cylinder(h=100, d=30);  // Will look faceted
```

✅ **CORRECT:**
```openscad
cylinder(h=100, d=30, $fn=50);  // Smooth circle
```

---

### Error 3: Incorrect Hole Syntax
❌ **WRONG:**
```openscad
difference() {
    cube([100, 50, 5]);
    cylinder(h=5, d=6);  // Hole won't go through
}
```

✅ **CORRECT:**
```openscad
difference() {
    cube([100, 50, 5]);
    translate([10, 10, -1])  // Position the hole
        cylinder(h=7, d=6, $fn=30);  // Extend beyond surface
}
```

---

### Error 4: Wrong Bracket Syntax
❌ **WRONG:**
```openscad
difference {  // Missing parentheses
    cube([50, 50, 50]);
}
```

✅ **CORRECT:**
```openscad
difference() {  // Needs parentheses
    cube([50, 50, 50]);
}
```

---

### Error 5: Incorrect Cube Dimensions
❌ **WRONG:**
```openscad
cube(50, 50, 50);  // Wrong syntax
```

✅ **CORRECT:**
```openscad
cube([50, 50, 50]);  // Use array notation
```

---

## 🔍 Quick Validation Checklist

Before accepting AI-generated code, check:

- [ ] Every statement ends with a semicolon `;`
- [ ] Cylinders and spheres have `$fn` parameter
- [ ] Cubes use array notation: `cube([x, y, z])`
- [ ] CSG operations have parentheses: `difference()`, `union()`, `intersection()`
- [ ] Holes extend beyond surfaces (use -1 and +2 in translate/height)
- [ ] All braces `{}` are properly matched
- [ ] Comments use `//` syntax

---

## 🛠️ Testing Generated Code

1. Copy the generated code
2. Open OpenSCAD
3. Paste and press F5 (preview)
4. Check for errors in the console
5. If errors appear, compare with examples in training_examples.md

---

## 📝 Improving the AI

If you get bad code:

1. **Identify the error pattern**
2. **Find or create a correct example**
3. **Add it to the system prompt** in the Streamlit app
4. **Try generating again** - it should improve!

The more correct examples you provide, the better the AI becomes at generating valid code.
