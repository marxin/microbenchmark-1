int global;

#define C(n, v) case n: return v;

int
foo (int x)
{
  switch (x & 20) {
    case 0:
      return 11;
    case 1:
      return 123;
    case 2:
      global += 1;
      return 3;
    case 3:
      return 44;
    case 4:
      return 444;
    C(5, 333)
    C(6, 555)
    C(7, 888)
    C(8, 1888)
    C(9, 2888)
    C(10, 3888)
    C(11, 4888)
    C(12, 5888)
    C(13, 6888)
    C(14, 7888)
    C(15, 8888)
    C(16, 9888)
    C(17, 33888)
    C(18, 88)
    C(19, 188)
    C(20, 388)
    default:
      return 0;
  }
}
