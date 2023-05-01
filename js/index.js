const canva = document.getElementById("graph-area");
const context = canva.getContext("2d");

const graph = new Graph();
const radius = 50;

let previous_state = null;
let current_state = null;

context.fillStyle = "black";
context.strokeStyle = "white";

context.canvas.width = window.innerWidth;
context.canvas.height = window.innerHeight;

function drawState(event) {
  let x = event.clientX - canva.getBoundingClientRect().left ;
  let y =  event.clientY - canva.getBoundingClientRect().top ;

  let label = prompt("Set State Label");
  let state = new State(x, y, label);

  graph.states.push(state);

  state.draw(context, radius);
}


function on_click(event) {

  event.stopPropagation();

  current_state = getClicked(event, graph, radius);

  if (current_state === null) {
    drawState(event);
    return;
  } else if (previous_state === null) {
    previous_state = current_state;
    return;
  } else {
    previous_state.drawLineTo(context, current_state);
  }
}

canva.addEventListener("click", on_click);
