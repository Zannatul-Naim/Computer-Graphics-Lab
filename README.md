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
