let canvas = document.getElementById("slate");
let ctx = canvas.getContext("2d");

let mode = "rect";
let size = 20

let drawRect = function(e) {
  let x = e.offsetX;
  let y = e.offsetY;
  ctx.fillStyle = "#ff0000";
  ctx.fillRect(x, y, size, size);
}

let drawCirc = function(e) {
  let x = e.offsetX;
  let y = e.offsetY;
  ctx.fillStyle = "#0000ff";
  ctx.beginPath();
  ctx.arc(x, y, size/2, 0, 2 * Math.PI);
  ctx.fill();
}

let draw = function(e) {
  if (mode == "rect") {
    drawRect(e);
  } else {
    drawCirc(e);
  }
}

let wipeCanvas = function(e) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

canvas.addEventListener("click", draw);
// On drag, draw
canvas.addEventListener("mousedown", function(e) {
  canvas.addEventListener("mousemove", draw);
  canvas.addEventListener("mouseup", function(e) {
    canvas.removeEventListener("mousemove", draw);
  });
});
let clear = document.getElementById("buttonClear");
clear.addEventListener("click", wipeCanvas);

let toggleMode = function(e) {
  if (mode == "rect") {
    mode = "circ";
    toggle.innerHTML = "Circle";
  } else { 
    mode = "rect";
    toggle.innerHTML = "Rectangle";
  }
  console.log("toggled to " + mode);
}

let toggle = document.getElementById("buttonToggle");
toggle.addEventListener("click", toggleMode);

let sizeSlider = document.getElementById("sizeSlider");
let sizeSpan = document.getElementById("sizeSpan");
sizeSlider.addEventListener("input", function(e) {
  size = sizeSlider.value;
  sizeSpan.innerHTML = size;
  console.log("size set to " + size);
});