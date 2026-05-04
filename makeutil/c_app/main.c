#include <stdio.h>
#include <time.h>

int main() {
    time_t now = time(NULL);
    printf("This is C app");
    printf("Run time: %ld\n", now);
    return 0;
}