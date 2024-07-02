// var x = 0
// //understanding while loop 
// while (x < 5){
//     console.log("x is currently: "+x);
//     if(x ===3){
//         console.log("The value of x is Three");
//         break;
//     }
//     console.log("The value of x is still <5, adding 1 to x");
//     x += 1;
// }
// //print the even number from 1 to 10 using while loop
// x = 0;
// document.write("The even numbers from 1 to 10 are: ")
// while(x<10){
//     if(x % 2 === 0){
//         document.write(x+"<br>");
//     }
//     x += 1;
// }

// // starting for loop
// for (x = 0;x<10;x++){
//     document.write(`${x}<br>`)
// }

// project one for js
var firstName = prompt("Enter your First Name: ");
var lastName = prompt("Enter your Last Name: ");
var age = parseInt(prompt("Enter your age: "));
var height = parseFloat(prompt("Enter your height: "));
var petName = prompt("Enter your pet name: ");
if(firstName[0] === lastName[0]){
    if(age>=26){
        if(height>175){
            console.log(petName[petName.length-1])
            if(petName[petName.length-1] === "y"){
                document.write("There is a secret message in console");
                console.log("You are a spy");
            }
        }
    }
}
else{
    document.write("Thank you for your details");
}



