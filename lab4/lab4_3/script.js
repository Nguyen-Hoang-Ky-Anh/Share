var currGreet = document.getElementById('greet');
var listGreets = [];
listGreets.push("Lời chào ngẫu nhiên này");
listGreets.push("Cette salutation aléatoire");
listGreets.push("Este saludo aleatorio");
listGreets.push("Dieser zufällige Gruß");
listGreets.push("Questo saluto casuale");

function randomGreet(){
    var randomIndex = Math.floor(Math.random() * listGreets.length);
    currGreet.textContent = listGreets[randomIndex];
}
randomGreet();