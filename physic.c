#include<stdlib.h>
#include<math.h>
#include<stdio.h>
void simple_equation();
void motion();
void liner_motion();
void free_fall();
void gravity();
void temperature();
void light();
void convert();
int main(){
    int options;
    printf("1:Simple motion");
    printf("\n2:Motion");
    printf("\n3:Liner motion");
    printf("\n4:Gravity");
    printf("\n5:Free fall equation");
    printf("\nChoose an option:");
    sscanf("%d",&options);
    switch (options){
        case 1: simple_equation(); break;
        case 2: motion(); break;
        case 3: liner_motion(); break;
        case 4: gravity(); break;
        case 5: free_fall(); break;
        default: printf("Choose a vild"); exit(0); break;
    }
    return 0;
}
void simple_equation(){

}
void motion(){

}
void liner_motion(){

}
void free_fall(){

}
void gravity(){

}
