gcc usage:
1. gcc main.c
2. gcc main.c -o a.out
3. gcc -c main.c
    Just compile. 
    In this case, gcc used C compiler(ccl) and assembler(as), and didn't use linker(ld)
4. gcc -Werror main.c -o a.out
    print more warning information as much as possible
5. -fPIC(optional, for dynamic linking)