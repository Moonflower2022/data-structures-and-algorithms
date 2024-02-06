#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_LINE_LENGTH 20
#define LINES 20

char lines[LINES][MAX_LINE_LENGTH];
int numbers[LINES];


int* bubble_sort(int length, int* unsorted);
int* swap(int i1, int i2, int* list);

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: ./{program name} {.txt with numbers' name}\n");
        return 1;
    }
    FILE* file = fopen(argv[1], "r");
    
    if (file == NULL)
    {
        printf("Invalid file. Please check for typos\n");
        return 1;
    }
    int i = 0;
    while(!feof(file) && !ferror(file))
    {
        if (fgets(lines[i], MAX_LINE_LENGTH, file) != NULL)
        {
            i++;
        }
    } 
    fclose(file);

    for (int i = 0; i < LINES; i++)
    {
        numbers[i] = atoi(lines[i]);
    }

    int* sorted_numbers = bubble_sort(LINES, numbers);

    for (int i = 0; i < LINES; i++)
    {
        printf("%i\n", sorted_numbers[i]);
    }
    return 0;
}

int* bubble_sort(int length, int* unsorted)
{
    bool made_switch = true;
    
    while (made_switch)
    {
        made_switch = false;
        for (int i = 0; i < length - 1; i++)
        {
            if (unsorted[i] > unsorted[i+1])
            {
                swap(i, i+1, unsorted);
                made_switch = true;
            }
        }
    }    
    return unsorted;
}

int* swap(int i1, int i2, int* list)
{
    int temp = list[i1];
    list[i1] = list[i2];
    list[i2] = temp;
    return list;
}