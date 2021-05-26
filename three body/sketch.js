let ww = window.innerWidth;
let wh = window.innerHeight;
// let m = 0;
// let n = 1;

function setup() {
  createCanvas(ww, wh);
  p1 = new Particle(10, 10, 50);
  p2 = new Particle(10, 10, 50);
  q = new attractor(10);
}

function draw() {
  translate(ww / 2, wh / 2);
  p1.display();
  p2.display();
  // let gravity = createVector(0, 0.5);
  // let gravityForce = p5.Vector.mult(gravity, p.m);
  // let wind = createVector(
  //   random(-noise(m), noise(m)) / 3,
  //   random(-noise(n), noise(n)) / 3
  // );
  background(0);
  // p.applyforce(gravityForce);
  // p.applyforce(wind);
  p1.update();
  p2.update();
  // p1.bounce();
  // p2.bounce();
  p1.display();
  p2.display();
  p1.attract(p2);
  // p1.attract(q);
  p2.attract(p1);
  // p2.attract(q);
  q.attract(p1);
  q.attract(p2);
  // q.display();

  // n += 0.001;
  // m += 0.001;
  if (mouseIsPressed) {
    q.pos.x = mouseX - ww / 2;
    q.pos.y = mouseY - wh / 2;
  }
  q.display();
}
