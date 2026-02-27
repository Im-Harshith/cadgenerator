# OpenSCAD Training Examples

This file contains correct OpenSCAD code examples that you can add to the system prompt to improve AI output quality.

## How to Use These Examples

1. Copy examples from this file
2. Add them to the system prompt in the Streamlit sidebar
3. The AI will learn from these patterns and generate better code

---

## Basic Shapes

### Cylinder
```
Input: "Create a cylinder 30mm diameter and 100mm height"
Output:
```openscad
// Cylinder: 30mm diameter, 100mm height
cylinder(h=100, d=30, $fn=50);
```
```

### Cube
```
Input: "Make a cube with 50mm sides"
Output:
```openscad
// Cube: 50mm sides
cube([50, 50, 50]);
```
```

### Sphere
```
Input: "Create a sphere with 25mm radius"
Output:
```openscad
// Sphere: 25mm radius
sphere(r=25, $fn=50);
```
```

---

## Mechanical Components

### Shaft with Keyway
```
Input: "Create a 120mm shaft, 20mm diameter with 4mm keyway"
Output:
```openscad
// Shaft with keyway
difference() {
    // Main shaft
    cylinder(h=120, d=20, $fn=50);
    
    // Keyway slot (4mm wide, 2mm deep)
    translate([8, -2, 0])
        cube([4, 4, 120]);
}
```
```

### Plate with Corner Holes
```
Input: "Rectangular plate 100x50x5mm with four 6mm corner holes"
Output:
```openscad
// Plate with corner holes
difference() {
    // Base plate
    cube([100, 50, 5]);
    
    // Corner holes (10mm from edges)
    translate([10, 10, -1]) cylinder(h=7, d=6, $fn=30);
    translate([90, 10, -1]) cylinder(h=7, d=6, $fn=30);
    translate([10, 40, -1]) cylinder(h=7, d=6, $fn=30);
    translate([90, 40, -1]) cylinder(h=7, d=6, $fn=30);
}
```
```

### Hollow Cylinder (Tube)
```
Input: "Create a hollow cylinder, outer diameter 40mm, inner diameter 30mm, height 60mm"
Output:
```openscad
// Hollow cylinder (tube)
difference() {
    // Outer cylinder
    cylinder(h=60, d=40, $fn=50);
    
    // Inner cylinder (hollow part)
    translate([0, 0, -1])
        cylinder(h=62, d=30, $fn=50);
}
```
```

### Bracket with 90-degree Bend
```
Input: "Make a bracket with a 90-degree bend, 50mm on each side, 3mm thick"
Output:
```openscad
// L-bracket
union() {
    // Horizontal part
    cube([50, 50, 3]);
    
    // Vertical part
    cube([50, 3, 50]);
}
```
```

---

## Complex Shapes

### Box with Rounded Corners (Fillet)
```
Input: "Create a box 80x60x40mm with 5mm radius rounded corners"
Output:
```openscad
// Box with rounded corners
minkowski() {
    cube([70, 50, 35]);
    cylinder(r=5, h=5, $fn=30);
}
```
```

### Hexagonal Nut
```
Input: "Create a hexagonal nut, 20mm across flats, 10mm thick, 8mm hole"
Output:
```openscad
// Hexagonal nut
difference() {
    // Hexagon body
    cylinder(h=10, d=20/cos(30), $fn=6);
    
    // Center hole
    translate([0, 0, -1])
        cylinder(h=12, d=8, $fn=30);
}
```
```

### Cone
```
Input: "Create a cone, base diameter 40mm, top diameter 20mm, height 50mm"
Output:
```openscad
// Cone
cylinder(h=50, d1=40, d2=20, $fn=50);
```
```

---

## Common Syntax Rules

1. **Always use semicolons** after statements
2. **Use $fn parameter** for smooth circles (e.g., $fn=50)
3. **Use translate()** before objects to position them
4. **Use difference()** to subtract shapes (for holes)
5. **Use union()** to combine shapes
6. **Extend holes slightly** (use -1 and +2 in height) to avoid rendering issues

---

## Adding Your Own Examples

When you find code that works well:

1. Note the input prompt
2. Save the working OpenSCAD code
3. Add it to this file
4. Copy it to the system prompt in the app

This creates a "training dataset" that improves the AI's output quality!
