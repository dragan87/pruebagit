#include <stdio.h>

// Función para intercambiar dos elementos del array
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

// Función para ordenar un array utilizando el algoritmo de ordenamiento de burbuja
void ordenarBurbuja(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }
}

int main() {
    int n;
    printf("Ingresa la cantidad de números: ");
    scanf("%d", &n);

    int numeros[n];

    printf("Ingresa %d números uno por uno:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &numeros[i]);
    }

    // Llama a la función para ordenar el array
    ordenarBurbuja(numeros, n);

    printf("Números ordenados: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", numeros[i]);
    }
    printf("\n");

    return 0;
}
