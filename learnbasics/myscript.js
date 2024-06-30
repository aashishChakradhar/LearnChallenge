var guessNum = prompt('Enter the number: ')
var num = 13
if(Math.abs(guessNum-num) >= 10){
    console.log("Very far")
}
else if(Math.abs(guessNum-num) >= 5 && Math.abs(guessNum-num) < 10){
    console.log("near")
}
else{ 
    console.log("tTrue num")
} 