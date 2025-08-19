# 📘 CSE4221: Computer Graphics — Lab Manual

## 🔥 Warm-Up Tasks

1. Draw the **National Flag of Bangladesh**  
2. Write **your name with animation**  
3. Simulate a **scene of traveling through space**  

---

## 🧪 Experiments

<!-- -. **Simulate Hidden Surface Elimination** (Visual Surface Detection)   -->
1. **Implement the Cohen–Sutherland Line Clipping Algorithm**  
2. **Implement the Sutherland–Hodgman Polygon Clipping Algorithm**  
3. **Create a Bézier Curve**  
4. Simulate **2D Geometric Transformations**:
   - Translation  
   - Rotation  
   - Scaling  
5. Draw a line using **Bresenham’s Line Drawing Algorithm**  
6. Draw a circle using **Bresenham’s Circle Drawing Algorithm**  
7. Draw a **Snowflake Pattern using Fractal Geometry**  



# 🐢 Computer Graphics with Python Turtle

---

## ✅ Requirements

- **Python 3.x**
- **Tkinter** (used internally by turtle for the graphics window)  
  → Usually comes pre-installed with the standard Python distribution.  
  → On Linux, if you get errors like *“No module named Tkinter”*, install it using:  
  ```bash
  sudo apt-get install python3-tk
  ```
---

## ⚙️ How to Run

1. **Install Python** (if not already installed):  
   https://www.python.org/downloads/

2. **Download or clone** this repository.

3. Open your terminal / command prompt and navigate to the folder containing the `.py` file.

4. Run any program using:

```bash
python filename.py
```




# 🟢 OpenGL Setup on Ubuntu 22.04+ using VS Code

This guide helps you set up and run **OpenGL** graphics programs on **Ubuntu 24.04** using **G++** and **Visual Studio Code** with `tasks.json`.

---

## 📦 Requirements

Make sure the following tools are installed:

- GCC/G++ compiler
- OpenGL development libraries
- VS Code (Visual Studio Code)

---

## 🧰 Step 1: Install Dependencies

Open your terminal and run:

```bash
sudo apt update
sudo apt install build-essential libgl1-mesa-dev libglu1-mesa-dev freeglut3-dev mesa-utils
```

## 🧪 Step 2: Test OpenGL
Run:

```bash
glxgears
```

If a spinning gear window appears, OpenGL is correctly set up on your system.

## 💻 Step 3: Create a Sample OpenGL Program
Create a file called main.cpp:

```c
#include <GL/glut.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glBegin(GL_TRIANGLES);
        glColor3f(1.0, 0.0, 0.0);
        glVertex2f(-0.5, -0.5);
        glColor3f(0.0, 1.0, 0.0);
        glVertex2f(0.5, -0.5);
        glColor3f(0.0, 0.0, 1.0);
        glVertex2f(0.0, 0.5);
    glEnd();
    glFlush();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutCreateWindow("OpenGL Triangle");
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
```

## 🧠 Step 4: VS Code Configuration
📁 Folder Structure

```css
your-project/
├── main.cpp
└── .vscode/
    └── tasks.json
```

## 📄 Create .vscode/tasks.json

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "build OpenGL",
      "type": "shell",
      "command": "g++",
      "args": [
        "main.cpp",
        "-o",
        "main",
        "-lglut",
        "-lGLU",
        "-lGL"
      ],
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "problemMatcher": []
    }
  ]
}
```

## ▶️ Step 5: Build and Run
🛠️ Build the Code
Press ```Ctrl + Shift + B``` to build the project using the ```tasks.json``` file.

## 🏃 Run the Output
Run this in the VS Code terminal:

```bash
./main
```


## ▶️ Step 5-B: Compile & run in terminal

```bash
  Compile: gcc main.c -o main -lglut -lGLU -lGL -lm
  Run    : ./main
```
