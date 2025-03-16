let keys = document.querySelectorAll(".drum-button");
var sounds = ["crash.mp3","kick-bass.mp3","snare.mp3","tom-1.mp3","tom-2.mp3","tom-3.mp3","tom-4.mp3"];
for (let index = 0; index < keys.length; index++) {
    keys[index].addEventListener("click",function(){
        new Audio(`sounds\\${sounds[index]}`).play(); 
    });    
}
