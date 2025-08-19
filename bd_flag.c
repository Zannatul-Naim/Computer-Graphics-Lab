/*
  
  To compile this code: > gcc bd_flag.c -o bd_flag -lglut -lGLU -lGL -lm
                  run:  > ./bd_flag

*/

#include <GL/glut.h>
#include <math.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    // Draw flag pole (white rectangle)
    glColor3f(1.0f, 1.0f, 1.0f); // White
    glBegin(GL_QUADS);
        glVertex2f(-0.85f, -0.7f);
        glVertex2f(-0.83f, -0.7f);
        glVertex2f(-0.83f,  0.7f);
        glVertex2f(-0.85f,  0.7f);
    glEnd();

    // Draw green background (flag)
    glColor3f(0.0f, 0.42f, 0.0f); // Deep green
    glBegin(GL_QUADS);
        glVertex2f(-0.8f, -0.5f);
        glVertex2f( 0.8f, -0.5f);
        glVertex2f( 0.8f,  0.5f);
        glVertex2f(-0.8f,  0.5f);
    glEnd();

    // Draw red circle (centered)
    glColor3f(0.83f, 0.0f, 0.0f); // Red
    float cx = 0.0f;
    float cy = 0.0f;
    float r = 0.25f;
    int i;
    glBegin(GL_TRIANGLE_FAN);
        glVertex2f(cx, cy); // center
        for (i = 0; i <= 100; ++i) {
            float angle = 2.0f * M_PI * i / 100;
            float x = cx + r * cos(angle);
            float y = cy + r * sin(angle);
            glVertex2f(x, y);
        }
    glEnd();

    glFlush();
}

void reshape(int w, int h) {
    float aspect = (float)w / (float)h;

    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    if (aspect >= 1.0f)
        gluOrtho2D(-aspect, aspect, -1.0f, 1.0f);
    else
        gluOrtho2D(-1.0f, 1.0f, -1.0f / aspect, 1.0f / aspect);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(600, 400);
    glutCreateWindow("Flag of Bangladesh - C with OpenGL");
    glClearColor(1.0, 1.0, 1.0, 1.0); // White background
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutMainLoop();
    return 0;
}
