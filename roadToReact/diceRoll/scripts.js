function numberGenerator(){
    var number = Math.floor(Math.random()*6)+1;
    return number;
}

function diceRoll() {
    const numberOfDices = document.getElementById("players").value; // gets number of player
    const numberSet = new Set();

    while (numberSet.size < numberOfDices) {
        numberSet.add(numberGenerator()); // add number to set until set size is equal to number of player
    }

    const numberGenerated = [...numberSet]; // Convert Set to array
    const imageElements = document.getElementsByClassName('dice'); // Get image elements
    for (let index = 0; index < numberGenerated.length; index++) {
        imageElements[index].src = `images/dice${numberGenerated[index]}.png`; // Update image source
    }

    const maxValue = Math.max(...numberGenerated);
    const maxValueIndex = numberGenerated.indexOf(maxValue);

    const result = document.querySelector(".result");
    result.textContent = `Player ${maxValueIndex + 1} Wins`; // Update result
}

function numberOfPlayers(){
    const player = document.getElementById("players").value;    // gets number of player
    document.getElementById("playersValue").textContent = player;   // display number of player
    const parent = document.querySelector(".whole");    // Get the parent element
    parent.innerHTML = "";  // Clear previous content
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