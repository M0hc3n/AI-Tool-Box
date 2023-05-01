class Graph {
  constructor(states = []) {
    this.states = [];
  }

  addState(x, y, label, edges) {
    this.states.push(new State(x, y, label, edges));
  }

}
