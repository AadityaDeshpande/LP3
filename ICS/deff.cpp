#include<iostream>
using namespace std;
long long int power(int a, int b, int mod)
{
long long int t;
if(b==1)
return a;
t=power(a,b/2,mod);
if(b%2==0)
return (t*t)%mod;
else
return (((t*t)%mod)*a)%mod;
}
long int calculateKey(int a, int x, int n)
{
return power(a,x,n);
}
int main()
{
int p,g,x,a,y,b;

cout<<"Enter the value of p and g : ";
cin>>p>>g;
cout<<"Enter the value of x for the first person : ";
cin>>x;
a=power(g,x,p);
cout<<"Enter the value of y for the second person : ";
cin>>y;
b=power(g,y,p);
cout<<"key for the first person is"<<power(b,x,p);
cout<<"key for the second person is"<<power(a,y,p);
}
