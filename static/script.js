let input_area;
let ctx;
let coord;

window.onload = function() {
    input_area = document.getElementById('canvas');
    ctx = input_area.getContext("2d");
    coord = { x: 0, y: 0 };
    input_area.addEventListener("mousedown", start);
    input_area.addEventListener("mouseup", stop);
}


function start(event) {
    console.log("start");
    document.addEventListener("mousemove", draw);
    reposition(event);
}

function reposition(event) {
    coord.x = event.clientX - input_area.offsetLeft;
    coord.y = event.clientY - input_area.offsetTop;
}

function stop() {
    console.log("stop");
    document.removeEventListener("mousemove", draw);
}

function draw(event) {
    ctx.beginPath();
    ctx.lineWidth = 15;
    ctx.lineCap = "round";
    ctx.strokeStyle = "#000000";
    ctx.moveTo(coord.x, coord.y);
    reposition(event);
    ctx.lineTo(coord.x, coord.y);
    ctx.stroke();
}

function clear_canvas() {
    console.log("clear");
    ctx.clearRect(0,0,280,280);
}
