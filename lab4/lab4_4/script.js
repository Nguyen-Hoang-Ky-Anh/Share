var inputTA = document.getElementById('textArea');
var inputTF = document.getElementById('textField');
var btnSubmit = document.getElementById('btn');

btnSubmit.addEventListener('click', function(){
    const textA = inputTA.value.trim().toLowerCase();
    const textB = inputTF.value.trim().toLowerCase();
    let count = 0;
    let pos = textA.indexOf(textB);
    if(textB === ""){
        alert("Vui long nhap tu tim kiem o text field");
        return;
    }
    while(pos !== -1){
        count++;
        pos = textA.indexOf(textB, pos + textB.length);
    }
    alert("Tu/cum tu " + textB + " xuat hien " + count + " lan")
});
