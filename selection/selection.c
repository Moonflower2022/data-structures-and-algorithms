#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_LINE_LENGTH 20
#define LINES 20

char lines[LINES][MAX_LINE_LENGTH];
int numbers[LINES];


int* selection_sort(int length, int* unsorted);
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

    int* sorted_numbers = selection_sort(LINES, numbers);

    for (int i = 0; i < LINES; i++)
    {
        printf("%i\n", sorted_numbers[i]);
    }
    return 0;
}

int* selection_sort(int length, int* unsorted)
{
    int biggest = -1;
    int biggest_index;
    int completed = 0;
    while (completed != length)
    {
        biggest = -1;
        biggest_index = -1;
        for (int i = 0; i < length; i++)
        {
            if (unsorted[i] > biggest)
            {
                biggest = unsorted[i];
                biggest_index = i;
            }
            if (i == length - completed - 1)
            {
                swap(biggest_index, length - completed - 1, unsorted);
                completed++;
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