/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team AYO: Yusha Aziz & Aaron Gershkovich
// SoftDev pd2
// K29 -- Getting more comfortable with the dev console and the DOM
// 2023-04-20
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO"); //prints AYO in the console

//stores one string var i as hello and an int var j as 20
var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x; //adds 30 to the argument
};


//instantiate an object
var o = { 'name' : 'Thluffy', //it looks as if this var is a composition of many things, it also looks like a dictionary of sorts
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem); //adds the item to the very end
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove(); //removes the index that is the argument
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){ //if even
      items[i].classList.add('red'); //make it red
    } else {
      items[i].classList.add('blue'); //make it blue
    }
  }
};

//insert your implementations here for...
// FIB
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

// FAC
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

// GCD
function gcd(a, b) {
  if (b == 0) {
    return a;
  } else {
    while (b != 0) {
      var temp = b;
      b = a % b;
      a = temp;
    }
    return a;
  }
}

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};

document.getElementById("fib").innerHTML = fib(10);
document.getElementById("fact").innerHTML = fact(10);
document.getElementById("gcd").innerHTML = gcd(10,100);

/*
function doIt(){
  var dasbut = document.getElementById("b"); 
  dasbut.addEventListener('click', ()=>{
    console.log(fib(6))
    document.getElementById("a").innerHTML = fib(6);
  });
}
*/



function logFibonacci() {
  var result = fib(10);
  console.log("Fibonacci of 20:", result);
  document.getElementById("one").innerHTML = result;
}

function logFactorial() {
  var result = fact(10);
  console.log("Factorial of 10:", result);
  document.getElementById("two").innerHTML = result;
}

function logGcd() {
  var result = gcd(100, 10);
  console.log("GCD of 100 and 10:", result);
  document.getElementById("three").innerHTML = result;
}

function bindFibonacci() {
  var button = document.getElementById("FIB"); 
  console.log("Fibonacci button bound");
  button.addEventListener('click', logFibonacci);
}

function bindFactorial() {
  var button = document.getElementById("FACT"); 
  console.log("Factorial button bound");
  button.addEventListener('click', logFactorial);
}

function bindGCD() {
  var button = document.getElementById("GCD"); 
  console.log("GCD button bound");
  button.addEventListener('click', logGcd);
}

//I call the functions here or else you have to press the button twice!
bindFibonacci();
bindFactorial();
bindGCD();
