class attractor {
  constructor(m) {
    this.m = m;
    this.pos = createVector(0, 0);
    this.r = sqrt(this.m) * 2;
    this.G = 0.3;
  }
  attract(particle) {
    let dir = p5.Vector.sub(this.pos, particle.pos);

    let mag = constrain(dir.magSq(), 100, 1000);
    let force = (this.G * this.m * particle.m) / mag;
    dir.setMag(force);
    particle.applyforce(dir);
  }
  display() {
    stroke(255);
    ellipse(this.pos.x, this.pos.y, this.r * 2, this.r * 2);
  }
  applyforce(Force) {
    // let f = Force.copy();
    // f.div(this.m);
    this.acc.add(Force);
  }
}
