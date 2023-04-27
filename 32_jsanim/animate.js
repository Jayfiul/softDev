/*
Team Monkeys :: Yusha A & Shafiul H
SoftDev pd2
K32 -- canvas based JS animation
2023-04-26t
*/

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");
var dvdButton = document.getElementById("buttonMovie");

var ctx = c.getContext("2d");

ctx.fillStyle = "#0000FF";

var requestID;

var clear = (e) => {
    ctx.clearRect(0, 0, c.width, c.height);
};

var radius = 0;
var growing  = true;

let drawCirc = function() {
    ctx.beginPath();
    ctx.arc(c.width/2, c.height/2, radius, 0, Math.PI*2);
    ctx.fill();
    ctx.closePath();
  }

var drawDot = () => {
    clear();
    if(radius==c.width/2){
        growing = false;
    }
    else if(radius==0){
        growing = true;
    }

    if (growing){
        radius++;
    }else{
        radius--;
     }
     
    drawCirc();

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
};


var stopIt = () => {
    console.log("stopIt invoked...")
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
};

var dvdLogoSetup = function(){
    window.cancelAnimationFrame(requestID);

    var rectWidth = 60;
    var rectHeight = 40;

    var rectX = Math.floor(Math.random() * 440);
   // console.log(rectX);
    var rectY = Math.floor(Math.random() * 460);
    // console.log(rectY);

    var xVel = 2;
    var yVel = 2;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function(){
        ctx.clearRect(0,0,c.width, c.height);
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);

        if (rectY <= 0 || rectY >= c.height-rectHeight){
            yVel = yVel * -1;
        }
        if (rectX <= 0 || rectX >= c.width-rectWidth){
            xVel = xVel * -1;
        }
        rectX += xVel;
        rectY += yVel;
        requestID = window.requestAnimationFrame(dvdLogo);
    };
    
    dvdLogo();

};


dotButton.addEventListener("click",drawDot);
stopButton.addEventListener("click", stopIt);
dvdButton.addEventListener("click", dvdLogoSetup);
