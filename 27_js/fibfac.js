// Team SexyMFs:: Yusha A & Russel G
// SoftDev pd2
// K27 -- Basic functions in JavaScript
// 2023-04-04t
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn

//Fact Function

function fact(n){
    if (n<= 0) 
        return "Error";
    else if (n == 1)
        return 1;
    else {
        var output = 1;
        for (var i = 1; i <= n; i++) {
            output *=i;
        }
        return output;
    }
}

//Fib Function

function fib(n){
    if (n <= 0) 
        return "Error!";
    else if (n == 1)
        return 0;
    else if (n == 2)
        return 1;
    else {
        var first = 0;
        var second = 1;
        for (var i = 3; i <= n; i++) {
            subSum = first + second;
            first = second;
            second = subSum;
        }
        return subSum;
    }
}


//test:
var num = 10;
console.log("Factorial of " + num + " is " + fact(num));
console.log("Fibonacci  of " + num + " is " + fib(num));
//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
