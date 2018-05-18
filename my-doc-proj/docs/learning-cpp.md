### tuple usage
* use `std::make_tuple(...)` create `tuple`
```
e.g.: tuple<int, string> tp = make_tuple(12, "ming");
```
* use `std::get<n>(tuple)` access `tuple`
```
e.g.: get<1>(tp);    // access the second element
```
* use `std::tie(...)` bind the existed variables

bind varibles
```
    e.g.: int a; string b;   
    tie(a, b) = tp;  
    tie(std::ignore, b) = tp;  
```
bind tuple
```
    e.g.: a = 12, b = "ming"; tp = tie(a, b);  
```