#include <math.h>
#include <stdio.h>
#include <stdlib.h>


double fill(int m, int n, double *(array[n]))
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

double adT(int m, int n, double *(array[n]))
{
    int a;
    for(int j=0;j<m;j++)
    {
        for(int i=0;i<n;i++)
        {
            a=array[j][i];
            array[j][i]=array[i][j];
            array[i][j]=a;

            printf("%lf " , array[j][i]);
        }
        printf("\n");
    }

}

double res(int m, int n, double array[n][m], double trans_arr[m][n])
{
  double res_arr[m][n];
  for(int i = 0; i < m; i++)
      for(int j = 0; j < n; j++)
      {
          res_arr[i][j] = 0;
          for(int k = 0; k < n; k++)
              res_arr[i][j] += array[i][k] * trans_arr[k][j];
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

  double original_array[m][n];
  fill(m, n, original_array);

  double trans_arr[n][m];
  adT(m, n, trans_arr);
  
  res(m, n, original_array, trans_arr);
  double res = find_min(m, n, array);
  printf("%lf", res);
  return 0;
}
