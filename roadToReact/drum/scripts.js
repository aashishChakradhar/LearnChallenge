let keys = document.querySelectorAll(".drum-button");
for (let index = 0; index < keys.length; index++) {
    keys[index].addEventListener("click",function(){
        console.log(`${keys[index].textContent} got clicked`);
        keys[index].textContent = "pressed"; 
    });    
}
