#include <iostream>
#include <string>

using namespace std;

int gcd (int a, int b){
    return b == 0 ? a : gcd(b, a%b);
}

int main(){
  char a[200];
  char charA[8];
  char charB[8];
  int x = 0;
  cin >> a;
   for (x; x<strlen(a);x++)
   {
     if (a[x]== '/')
     break;
   }
   for (int y = 0; y<x; y++)
   {
     charA[y] = a[y];
   }
   int b = 0;
   for (int y = x+1; y<strlen(a); y++)
   {
     charB[b] = a[y];
     b++;
   }
   int a1 = atoi(charA);
   int b1 = atoi(charB);

  int num = 5 * ( a1 - 32 * b1 );
  int den = b1 * 9;

  int originalNum = num;
  num = abs(num);

  int gcd1 = gcd(num, den);

  cout <<originalNum/gcd1 << "/" << den/gcd1 << endl;
}