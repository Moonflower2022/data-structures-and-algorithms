/*
It's broken rn, idk how to fix it. Something with returning vectors or smth
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <vector>

using namespace std;

#define MAX_LINE_LENGTH 20
#define LINES 20

char lines[LINES][MAX_LINE_LENGTH];
vector<int> numbers;


std::vector<int> merge_sort(int length, std::vector<int> unsorted);
std::vector<int> combine (int len1, std::vector<int> arr1, int len2, std::vector<int> arr2);

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
    std::vector<int> sorted_numbers = merge_sort(LINES, numbers);

    for (int i = 0; i < LINES; i++)
    {
        printf("%i\n", sorted_numbers[i]);
    }
    return 0;
}

std::vector<int> merge_sort(int length, std::vector<int> unsorted)
{
    if (length == 1)
    {
        return unsorted;
    }
    int half_int = round(length/2);
    std::vector<int> arr1(half_int);
    std::vector<int> arr2(length - half_int);
    for (int i = 0; i < half_int; i++)
    {
        arr1[i] = unsorted[i];
    }
    for (int i = half_int; i < length - half_int; i++)
    {
        arr2[i] = unsorted[i];
    }
    return combine(half_int, merge_sort(half_int, arr1), length - half_int, merge_sort(length - half_int, arr2));
}

std::vector<int> combine (int len1, std::vector<int> arr1, int len2, std::vector<int> arr2)
{
    std::vector<int> arr3(len1 + len2);
    int i1 = 0;
    int i2 = 0;
    while (i1 + i2 != len1 + len2)
    {
        if (i1 == len1)
        {
            for (int i = 0; i < len2; i++)
            {
                if (i >= i2)
                {
                    arr3.push_back(arr2[i]);
                }
            }
            break;
        }
        else if (i2 == len2)
        {
            for (int i = 0; i < len1; i++)
            {
                if (i >= i1)
                {
                    arr3.push_back(arr1[i]);
                }
            }
            break;
        }
        else if (arr2[i2] < arr1[i1])
        {  
            //arr3[i1 + i2] = arr2[i2];
            arr3.push_back(arr2[i2]);
            i2++;
            continue;
        }
        if (arr1[i1] < arr2[i2])
        {
            //arr3[i1 + i2] = arr1[i1];
            arr3.push_back(arr1[i1]);
            i1++;
            continue;
        }
        if (arr1[i1] == arr2[i2])
        {
            //arr3[i1 + i2] = arr1[i1];
            //arr3[i1 + i2 + 1] = arr2[i2];
            arr3.push_back(arr1[i1]);
            arr3.push_back(arr2[i2]);
            i1++;
            i2++;
            continue;
        }
    }
    return arr3;
}