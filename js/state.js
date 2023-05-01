class State {
  constructor(x, y, label = "A", neighbors = []) {
    this.x = x;
    this.y = y;
    this.label = label !== null ? label : "";
    this.neighbors = neighbors;
  }

  addEdge(state) {
    this.neighbors.push(state);
  }

  draw(context, radius = 50) {
    drawCircle(context, this.x, this.y, radius);
    putText(context, this.label, this.x, this.y);
  }

  drawLineTo(context, state) {
    context.moveTo(this.x, this.y);
    context.lineTo(state.x, state.y);
    context.stroke();
  }
}
