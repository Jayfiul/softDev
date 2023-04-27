/*
Team AYO :: Yusha A, Aaron G, Sebastian
SoftDev pd2
K31 -- canvas based JS animation
2023-04-25t
*/

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");
var movieButton = document.getElementById("buttonMovie");

var ctx = c.getContext("2d");

ctx.fillStyle = "#0000FF";

var requestID;

var clear = (e) => {
    e.preventDefault();
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
}

var dvdLogoSetup = function(){
    window.cancelAnimationFrame(requestID);
    var rectWidth = movieButton.height;
    var rectHeight = movieButton.width;

    var rectX = Math.random(c.width) - rectWidth;
    var rectY = Math.random(c.height) - rectHeight;

    var rand = Math.random();

    var xVel = 5*Math.cos(rand*2*Math.PI);
    var yVel = 5*Math.sin(rand*2*Math.PI);


    var velocity = 5;

}

var logo = new Image();
logo.src = "logo_dvd.jpg";

var dvdLogo = function(){
    ctx.clearRect(0,0,c.width, c.height);
    ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
    if (y < 0 || y > c.height-rectHeight){
        yVel = YVel * -1
    }
    if (x < 0 || x > c.width-rectWidth){
        xVel = xVel * -1
    }
    rectX += xVel;
    rectY += yVel;
    requestID = window.requestAnimationFrame(buttonMovie);
}

var stopIt = () => {
    console.log("stopIt invoked...")
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener("click",drawDot);
stopButton.addEventListener("click", stopIt);
dvdButton.addEventListener("click", dvdLogoSetup);
