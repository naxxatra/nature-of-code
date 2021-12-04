function setup() {
  createCanvas(640, 360);
  w = new Walker();
  b = new Walker();
}

function draw() {
  background(51);

  w.show();
  w.display();
  w.walk();
  w.bounce();

  b.show();
  b.display();
  b.walk();
  b.bounce();
}

class Walker {
  constructor() {
    this.trail = [];
    this.pos = createVector(width / 2, height / 2);
    this.vel = createVector(0, 0);
    
  }

  walk() {
    this.acc = createVector(random(-0.4, 0.4), random(-0.4, 0.4));
    this.pos.add(this.vel);
    this.vel.add(this.acc);
    this.trail.push([this.pos.x, this.pos.y]);
  }

  display() {
    fill(255, 255, 0);
    ellipse(this.pos.x, this.pos.y, 15, 15);
  }

  bounce() {
    if (this.pos.y >= 360 || this.pos.y <= 0) {
      this.vel.y = -this.vel.y;
    }

    if (this.pos.x >= 640 || this.pos.x <= 0) {
      this.vel.x = -this.vel.x;
    }
  }

  show() {
    stroke(255, 0, 0);
    strokeWeight(1);
    let l = this.trail.length;

    for (let i = 0; i < l; i++) {
      point(this.trail[i][0], this.trail[i][1]);
    }
  }
}