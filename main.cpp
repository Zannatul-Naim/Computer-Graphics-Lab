// #include <GL/glut.h>

// void display() {
//     glClear(GL_COLOR_BUFFER_BIT);
//     glBegin(GL_TRIANGLES);
//         glColor3f(1.0, 0.0, 0.0);
//         glVertex2f(-0.5, -0.5);
//         glColor3f(0.0, 1.0, 0.0);
//         glVertex2f(0.5, -0.5);
//         glColor3f(0.0, 0.0, 1.0);
//         glVertex2f(0.0, 0.5);
//     glEnd();
//     glFlush();
// }

// int main(int argc, char** argv) {
//     glutInit(&argc, argv);
//     glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
//     glutInitWindowSize(500, 500);
//     glutCreateWindow("OpenGL Triangle");
//     glutDisplayFunc(display);
//     glutMainLoop();
//     return 0;
// }


#include <GL/glut.h>
#include <iostream>

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutCreateWindow("OpenGL Version");

    const GLubyte* version = glGetString(GL_VERSION);
    std::cout << "OpenGL version: " << version << std::endl;

    return 0;
}
