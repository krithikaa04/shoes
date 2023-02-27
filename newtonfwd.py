# newton forward interpolation

def calc(u,n):
	temp=u;
	for i in range(1,n):
		temp=temp*(u-i);
	return temp;

def fact(n):
	f=1;
	for i in range(2,n+1):
		f=f*i;
	return f;


# Number of values given
n=7
x=[100,150,200,250,300,350,400];

y = [[0 for i in range(n)]for j in range(n)];
y[0][0]=10.63
y[1][0]=13.03
y[2][0]=15.04
y[3][0]=16.81
y[4][0]=18.42
y[5][0] = 19.90
y[6][0] = 21.27

for i in range(1,n):
	for j in range(n-i):
		y[j][i]=y[j+1][i-1]-y[j][i-1];

for i in range(n):
	print(x[i],end="\t");
	for j in range(n-i):
		print(round(y[i][j],4),end="\t");
	print("");

value = 160;

sum=y[0][0];
u=(value-x[0])/(x[1]-x[0]);
for i in range(1,n):
	sum=sum+(calc(u,i)*y[0][i])/fact(i);

print("\nValue at", value, "is", round(sum, 4));

