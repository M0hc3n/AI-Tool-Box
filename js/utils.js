function checkClicked(x, y, targetX, targetY, radius) {
  return Math.abs(x - targetX) <= radius && Math.abs(y - targetY) <= radius;
}

function getClicked(event, graph = new Graph(), radius = 50) {
  let x = event.targetX + event.clientX;
  let y = event.targetY + event.clientY;

  graph.states.forEach((state) => {
    if (checkClicked(x, y, state.x, state.y, radius)) return state;
  });

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
