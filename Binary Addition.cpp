// Akhilesh.M
#include<stdio.h>
int main() {
	int a,b,carry=0,l,i=0;
	scanf("%d%d",&a,&b);
	int x=a,y=b,arr[8]={0};
	while(x!=0 && y!=0) {
		l=carry+(x%10)+(y%10);
		printf("l is %d\n",l);
		if (l==2) {
			carry=1;
			arr[i]=0;
		} else if (l==3) {
			carry=1;
			arr[i]=1;
		} else {
			arr[i]=l;
			carry=0;
		}
		i++;
		x=x/10;
		y=y/10;
	}
	arr[i]=carry;
	for(int i=7;i>=0;i--) {
		printf("%d",arr[i]);
	}
    return 0;
}

