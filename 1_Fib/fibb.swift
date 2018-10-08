//: Playground - noun: a place where people can play

import Swift
var x = -1 ,y = 1, sum = 0;

for _  in  0..<10 {
    
    sum = x+y;
    x   = y;
    y   = sum;
    
    print(sum);
    
}
