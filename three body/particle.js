class Particle {
  constructor(x, y, m) {
    this.acc = createVector(0, 0);
    this.vel = p5.Vector.random2D();
    this.vel.mult(random(50, 100));
    // this.vel.limit(10);
    // this.vel.rotate(90);
    this.vel.limit(5);
    this.pos = createVector(random(-ww / 2, ww / 2), random(-wh / 2, wh / 2));
    this.dx = x;
    this.dy = y;
    this.m = m;
    this.G = 0.3;
  }
  update() {
    this.vel.add(this.acc);
    this.pos.add(this.vel);
    this.acc.set(0, 0);
  }
  display() {
    stroke(255);
    strokeWeight(10);
    ellipse(this.pos.x, this.pos.y, this.dx, this.dy);
  }
  applyforce(Force) {
    // let f = Force.copy();
    // f.div(this.m);
    this.acc.add(Force);
  }
  attract(particle) {
    let dir = p5.Vector.sub(this.pos, particle.pos);

    let mag = constrain(dir.magSq(), 100, 1000);
    let force = (this.G * this.m * particle.m) / mag;
    dir.setMag(force);
    particle.applyforce(dir);
  }
  bounce() {
    if (this.pos.x > ww / 2 || this.pos.x < -ww / 2) {
      this.vel.x = -1 * this.vel.x;
    }
    if (this.pos.y > wh / 2 || this.pos.y < -wh / 2) {
      this.vel.y = -1 * this.vel.y;
    }
  }
}
