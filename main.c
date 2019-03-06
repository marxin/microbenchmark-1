#define LOOP 200000000

int foo(int);

int
main ()
{
  for (int i = 0; i < LOOP; i++)
    foo (i);
}
