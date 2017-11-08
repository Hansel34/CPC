// Union-Find

#define MAXN 200000
int p[MAXN];
int find(int x)
{
	return p[x] == x ? x: p[x] = find(p[x]);
}

void unite (int x, int y)
{
	p[find(x)] = find(y);
}

int main()
{
for (int i = 0; i < MAXN; i++) 
{
	p[i] = i;
}
}


//square root decomposition

