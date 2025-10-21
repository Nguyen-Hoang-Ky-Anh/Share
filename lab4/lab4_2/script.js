function giaiPhuongTrinhBac2(a,b,c){
    var delta = b ** 2 - 4 * a * c;
    if (delta < 0) {
        console.log("Phuong trinh vo nghiem");
    }
    else if(delta == 0){
        console.log("Phuong trinh co nghiem kep x1 = x2 = " + (-b/(2*a)));
    }
    else{
        var x1 = (-b + Math.sqrt(delta)) / (2 * a);
        var x2 = (-b - Math.sqrt(delta)) / (2 * a);
        console.log("Phuong trinh co 2 nghiem phan biet: " + "x1: " + x1 + ", " + "x2: " + x2);
    }
}
giaiPhuongTrinhBac2(1,2,3);
