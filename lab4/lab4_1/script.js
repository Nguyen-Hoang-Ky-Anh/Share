var redBtn = document.getElementById('red')
var orangeBtn = document.getElementById('orange')
var yellowBtn = document.getElementById('yellow')
var cyanBtn = document.getElementById('cyan')
var greenBtn = document.getElementById('green')
var whiteBtn = document.getElementById('white')

redBtn.addEventListener("click", function(){
    document.body.style.backgroundColor = "red"
});
orangeBtn.addEventListener("click", function(){
    document.body.style.backgroundColor = "orange"
});
yellowBtn.addEventListener("click", function(){
    document.body.style.backgroundColor = "yellow"
});
cyanBtn.addEventListener("click", function(){
    document.body.style.backgroundColor = "cyan"
});
greenBtn.addEventListener("click", function(){
    document.body.style.backgroundColor = "green"
});
whiteBtn.addEventListener("click", function(){
    document.body.style.backgroundColor = "white"
});