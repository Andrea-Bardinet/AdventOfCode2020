#include <stdio.h>

void part1(int *tab, int nbNombre){
	int x;
	long ans;

	

	for(int i = 0; i<nbNombre;i++){
		for(int j=i; j<nbNombre;j++){
			if(tab[i]+tab[j] == 2020){
				ans = tab[i]*tab[j];
				printf("Reponse part1: %ld\n",ans);
			}
		}
	}
}

void part2(int *tab, int nbNombre){
	int x;
	long ans;

	for(int i=0;i<nbNombre;i++){
		for(int j=i;j<nbNombre;j++){
			for(int k=j;k<nbNombre;k++){
				if(tab[i]+tab[j]+tab[k] == 2020){
					ans = tab[i]*tab[j]*tab[k];
					printf("Reponse part2: %ld\n",ans );
				}
			}
		}
	}
}

int main(void)
{
	FILE *input;
	input = fopen("input","r");

	int tab[500], nbNombre, x;

	do{
		fscanf(input,"%d",&x);
		tab[nbNombre] = x;
		nbNombre++;
	}while(!feof(input));

	part1(tab, nbNombre);
	part2(tab, nbNombre);


	return 0;
}