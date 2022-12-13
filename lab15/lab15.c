#include <math.h>
#include <stdio.h>
void main()
{
int i,n,j;
float a,b,mas[10][10];
    printf("Введите n= ");
    scanf("%d",&n);
        for(i=0;i<n;i++) 
{
        for(j=0;j<n;j++) 
{
    printf("mas(%d %d)=",i,j);
    scanf("%f",&mas[i][j]);
}
}
        for(j=0;j<n;j++)
        for(i=0;i<j;i++)
{
a=mas[j][i];
mas[j][i]=mas[i][j];
mas[i][j]=a;
}
        for(i=0;i<n;i++) 
{
        for(j=0;j<n;j++)
    printf("%f\t",mas[i][j]);
    printf("\n");
}
    scanf("%f",&mas[i][j]);
    scanf("%f",&n);
}