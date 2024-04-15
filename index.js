// Usig var
var name = 'Indtrustor Eddy.'; //string datatype
console.log(name)

// using let
let job = "A PLP Istrictor";
console.log(job);

// using comst
const PI = 3.14152; //number datatype - float
console.log(PI);

// camelCase
var firstName, FirstName, FIRSTNAME;

// snake_case
var last_name;

var age = 29; //numebr datatype - interger

//boolean datatypes true or false
var success = false;

// null datatype - empty or unknown value
var balance = null;

// undefined datatype
var LastName; 
console.log(LastName);

//------------------------------------------------

// arithmetic operators - mathematical
// = addition
// - subtraction
// * multiplication
// / division
// ** exponentiation
// ++ increment
// -- decrement
// % remainder
let x = 10;
let y = 5;

console.log(x + y);
console.log(x - y);
console.log(x * y);
console.log(x / y);
console.log(x ** y);
x++;
console.log(x);
y--;
console.log(y);
console.log(x%y);

// assignment operator
// equal =
// addition +=
// subtration -=
// multipilcation *=
// division /=
// remainder %=
let p = 10;
let v = 5;

p -= v;

console.log(p);

//------------------------------------------------+

//comparison operator
// equal ==
// not equal !=
// strict equal ===
// not strict equal !==
// greater than >
// lesser than <
// greater than or equal >=
// less than or equal <=
var u = 1;
var o = 3;

console.log(u == o);
console.log(u != o);
console.log(u === o);
console.log(u !== o);
console.log(u > o);
console.log(u < o);
console.log(u >= o);
console.log(u <= o);

//------------------------------------------------------------------------------------------------

// arrays - stores more than one value
var cars = ['Toyota', 'Mazda', 'Volvo', 'Nissan'];
console.log(cars);
// assigning the possition of the array
console.log(cars[1]);

cars[3] = 'Mercedes';

console.log(cars);

cars.push('Nissan');

cars.unshift('Mistubishi');

console.log(cars);

cars.pop();

console.log(cars);

//--------------------------------------------------------------------------------------------------

//conditional statements

var cash = 999;

if(cash > 1000){
   console.log("You can afford airtime."); 
} else {
    console.log("You have insufficient cash");
}