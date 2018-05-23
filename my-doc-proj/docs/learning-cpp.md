# tuple
---
**usage**  
1. use `std::make_tuple(...)` create `tuple`  
2. use `std::get<n>(tuple)` access `tuple`  
3. use `std::tie(...)` bind the existed variables  
```
e.g.: tuple<int, string> tp = make_tuple(12, "ming");  
e.g.: get<1>(tp);    // access the second element
<1>. bind varibles
e.g.: int a; string b;   
tie(a, b) = tp;  
tie(std::ignore, b) = tp;  
<2>.  bind tuple
e.g.: a = 12, b = "ming"; tp = tie(a, b);
```

# dynamic link
---
Invoke `.so` in runtime. The main function is 
`dlopen()`, `dlsym()`, `dlerror()`, `dlclose()` 
in dlfcn.h head file.  
Usage:
```
void *handler = dlopen(file, MODE);	// MODE: RTLD_LAZY/RTLD_NOW
func_ptr = dlsym(handler, "invoked_func");
err = dlerror();
if (err != NULL) {
	// ...
}
__return = (*func_ptr)(args);	// invoke this function
dlclose(handler);
```

# compiler
---
**compilation process**  
ST-1. preprocessing(process `macro definition`)  
ST-2. compile(generate `assembly code`)  
ST-3. assembly(generate `object file`)  
ST-4. link(generate `executable file`)  
```
compilation command:
1. gcc -E hello.c -o hello.i
2. gcc -S hello.i -o hello.s
3. gcc -c hello.s -o hello.o
4. gcc hello.o -o hello
```
**gcc & g++**  
1. 后缀为.c的，gcc把它当作是C程序，而g++当作是c++程序；后缀为.cpp的，两者都会认为是c++程序.  
2. 编译阶段，g++会调用gcc；编译可以用gcc/g++，而链接可以用g++或者gcc -lstdc++。
因为gcc命令不能自动和C＋＋程序使用的库链接，所以通常使用g++来完成链接。但在编译阶段，g++会自动调用gcc，二者等价。  
3. __cplusplus宏只是标志着编译器将会把代码按C还是C++语法来解释。  
4. 无论是gcc还是g++，用extern "c"时，都是以C的命名方式来为symbol命名，否则，都以c++方式命名。
```
function: CppPrint()
1. with `extern "C"`:
    function name: CppPrint
2. without `extern "C"`
    function name: _Z9CppPrint
```

# gcc features 
---
**GCC inner macro definition**  
use `gcc -E -dM - </dev/null ` command look over the inner macro  

**GCC attribute mechanism**  
`__attribute__` mechanism is used to set function attribute, 
variable attribute and type attribute.  
```
Usage:
    __attribute__((attribute-list))
e.g.:
    __attribute__ ((visibility("default")))
During the compilation, you can use -fvisibility parameter set symbol visibility.
```
**GCC -D**  
It's easy to debug.
```
#include <stdio.h>  
#include <stdlib.h>  
  
int main(int argc, char* argv[])  
{   
#ifdef DEBUG  
    printf("gcc 的-D 选项测试\n");  
#endif
    return 0;  
}

yu@ubuntu:~/cplusplus/gcc$ gcc debugtest.c -o debugtest.exe  
yu@ubuntu:~/cplusplus/gcc$ ./debugtest.exe 

yu@ubuntu:~/cplusplus/gcc$ gcc debugtest.c -o debugtest.exe -D DEBUG  
yu@ubuntu:~/cplusplus/gcc$ ./debugtest.exe   
gcc 的-D 选项测试  
```

# C++11 features
---
[C++11](https://blog.csdn.net/zdy0_2004/article/details/69934828)  
[C++14](https://blog.csdn.net/u012234115/article/details/47209679)  
[C++17]()

# template
---
purpose:

# std algorithm
**1. std::nth_element**  
Description:  
将第n_thn_th 元素放到它该放的位置上，左边元素都小于它，右边元素都大于它.  
Usage:  
```
    vector<int> vec = {...};
    nth_element(vec.begin(), vec.begin() + 6, vec.end());
```