function checkClicked(x, y, targetX, targetY, radius) {
  if(Math.sqrt(Math.pow(x - targetX, 2) + Math.pow(y - targetY, 2)) <= 2 * radius){
    return true;
  } else {
    return false;
  }
}

function getClicked(event, graph , radius = 50) {

  let x =  event.clientX - canva.offsetLeft;
  let y = event.clientY - canva.offsetTop; 

  for(let i=0 ; i < graph.states.length ; i++){
    if(checkClicked(x, y, graph.states[i].x , graph.states[i].y ,radius )) {
      return graph.states[i] ;
    }
  }

  return null;
}

function drawCircle(context, x, y, radius) {
  context.beginPath();
  context.arc(x, y, radius, 0, Math.PI * 2);
  context.save();
  context.globalAlpha = 0.5;
  context.fill();
  context.restore();
  context.stroke();
}

function putText(
  context,
  text,
  x,
  y,
  size = "2rem",
  font = "sans-serif",
  align = "center",
  color = "white"
) {
  context.font = `bold ${size} ${font}`;
  context.textAlign = align;
  context.save();
  context.fillStyle = color;
  context.fillText(text, x, y);
  context.restore();
}
