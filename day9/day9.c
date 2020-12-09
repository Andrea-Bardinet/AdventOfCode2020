#include <stdio.h>
#include <stdlib.h>

long fPart1(FILE *input){

	long last[25], current, control, save, tmp;

	for(int i=0;i<25;i++){
		fscanf(input,"%ld\n",&last[i]);
	}

	while(!feof(input)){
		control = 0;
		fscanf(input,"%ld\n",&current);
		for(int i=0;i<25&&!control;i++){
			for(int j=i+1;j<25&&!control;j++){
				if(last[i]+last[j]==current){
					control = 1;
				}
			}
		}
		if(!control){
			return current;
		}

		
		save = current;
		for(int i=24;i>=0;i--){
			tmp = last[i];
			last[i] = save;
			save = tmp;	
		}
		
	}
	
	return -1;
}

long fPart2(FILE *input, long part1){
	long tab[1000], current=0, nbTab, *result, add=0, find[2], tmp;

	for(nbTab=0;current!=part1;nbTab++){
		fscanf(input,"%ld\n",&current);
		tab[nbTab] = current;
	}


	for(int i = 2; i<nbTab; i++){

		result = (long*)malloc(sizeof(long)*i);

		for(int j = 0;j<nbTab-i;j++){
			add = 0;
			for(int k=0;k<i;k++){
				result[k] = tab[k+j];
			}
			for(int k=0;k<i;k++){
				add += result[k];
			}
			if(add == part1){
				find[0] = result[0];
				find[1] = result[0];
				for(int k=0;k<i;k++){
					if(result[k] < find[0]){
						find[0] = result[k];
					}
					if(result[k]>find[1]){
						find[1] = result[k];
					}
				}
				return find[0]+find[1];
			}
			
		}
	}

	return -1;
}


int main(void){

	FILE *input;
	input = fopen("input", "r");

	long  part1 = fPart1(input);
	

	fseek(input, 0, SEEK_SET);
	long part2 = fPart2(input,part1);
	
	printf("Part1: %ld\n",part1);
	printf("Part2: %lld",part2);


	return 0;
}