var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

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
}


var stopIt = () => {
    console.log("stopIt invoked...")
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener("click",drawDot);
stopButton.addEventListener("click", stopIt);