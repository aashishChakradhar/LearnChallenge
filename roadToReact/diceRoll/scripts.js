function numberGenerator(){
    var number = Math.floor(Math.random()*6)+1;
    return number;
}

function diceRoll(numberOfDices){
    const numberGenerated = new Set([]);
    const imageElements = document.getElementsByClassName('dice');
    let index = 0;
    while(index<numberOfDices) {
        numberGenerated.add(numberGenerator());
        imageElements[index].src = "images/dice"+numberGenerated[index]+".png";
        index = numberGenerated.length;
    }
    const maxValue = Math.max.apply(this,[...numberGenerated]);
    const maxValueIndex = numberGenerated.indexOf(maxValue);

    const result = document.querySelector(".result");
    result.textContent = `Player${maxValueIndex+1} Wins`;
    console.log(result);
}

function numberOfPlayers(){
    const player = document.getElementById("players").value;
    document.getElementById("playersValue").textContent = player;
    console.log(player)
    const parent = document.querySelector(".whole");
    parent.innerHTML = "";
    for (let index = 0; index < player; index++) {
        const div = document.createElement("div");
        const h4 = document.createElement("h4");
        const img = document.createElement("img");
    
        h4.textContent = "Player " + (index + 1);
        img.src = "images/dice" + (index + 1) + ".png"; // Ensure correct image path
        img.alt = "Dice Image";
        img.classList.add("dice"); // Add class properly
        img.style.width = "3rem";
        img.style.height = "3rem"; // Optional: Set image size
    
        div.appendChild(h4);
        div.appendChild(img);
        parent.appendChild(div); // Append div to parent
    }
    
}