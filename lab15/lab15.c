#include <math.h>
#include <stdio.h>
#include <stdlib.h>


void fill(int m, int n, double *(array[n]))
{
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            array[i][j] = cos(sqrt(i)) - i + cos(j)/sqrt(1+j);
            // printf("%lf " , array[j][i]);
        }
        // printf("\n");
    }
}

void adT(int m, int n, double *(array[n]))
{
    int a;
    for(int j=0;j<m;j++)
    {
        for(int i=0;i<n;i++)
        {
            a=array[j][i];
            array[j][i]=array[i][j];
            array[i][j]=a;

            // printf("%lf " , array[j][i]);
        }
        // printf("\n");
    }

}

double find_min(int m, int n, double *(array[n]))
{
  double res = 100;
  for (int i = 0; i < m; i++)
      for (int j = 0; j < n; j++)
          if (fabs(array[i][j]) < sqrt(res))
              res = fabs(array[i][j]);
  return sqrt(res);

}

int main()
{
  int n, m;
  printf("Enter count of rows: ");
  scanf("%d", &m);
  printf("Enter count of columns: ");
  scanf("%d", &n);
  double **array = (double **)malloc(sizeof(double *) * m);
  if (!array)
  {
    printf("Memory allocation error!\n");
    exit(EXIT_FAILURE);
  }
  for (int i = 0; i < m; i++)
    array[i] = (double *)malloc(n * sizeof(double));

  fill(m, n, array);
  adT(m, n, array);
  double res = find_min(m, n, array);
  printf("%lf", res);
  return 0;
}
