### tuple usage
1. 使用std::make_tuple(...)创建tuple  
e.g.: tuple<int, string> tp = make_tuple(12, "ming");
2. 使用std::get<n>(tuple)访问tuple  
e.g.: get<1>(tp)    // 访问第2个元素
3. 使用std::tie(...)绑定已存在变量
3.1 绑定到变量  
e.g.: int a; string b;   
tie(a, b) = tp;  
tie(std::ignore, b) = tp;  
3.2 绑定到tuple  
e.g.: a = 12, b = "ming"; tp = tie(a, b);  