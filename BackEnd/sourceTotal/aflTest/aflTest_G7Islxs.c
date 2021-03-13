#include<stdio.h>
#include<stdlib.h>

int main(int argc, char **argv){
    char ptr[20];
    if (argc > 1){
        FILE *fp = fopen(argv[1], "r");
        fgets(ptr,sizeof(ptr),stdin);

    }
    else{
        fgets(ptr,sizeof(ptr),stdin);
    }
    printf("%s", ptr);
    if(ptr[0] == 'd'){
        if(ptr[1] == 'e'){
            if(ptr[2]=='a'){
                if(ptr[3]=='d'){
                    if(ptr[4] == 'b'){
                        if(ptr[5]=='e'){
                            if(ptr[6]=='e'){
                                if(ptr[7]=='f')
                                {
                                    abort();
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}