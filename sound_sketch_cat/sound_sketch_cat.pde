import ddf.minim.*;
import ddf.minim.analysis.*;


Minim minim;
AudioPlayer song;
FFT fft;

int rowmax = 800;
int colmax = 512;
int leftedge;
int col;

float[][] sgram = new float[rowmax][colmax];

float y = 0;
float x = 0;
float r;
float t = 0;

void setup()
{
  size(800, 800, P3D);

  minim = new Minim(this);
  song = minim.loadFile("cat.wav");
  song.loop();

  fft = new FFT(song.bufferSize(), song.sampleRate());
}

void draw()
{
  background(26, 79, 102);
 
 
  strokeWeight(1);
  noFill();

  // perform a forward FFT on the samples in the input buffer
  fft.forward(song.mix);
  
  translate(width/2, height/2);
  
  beginShape();
  for (int i = 0; i < 360; i++)
    {
      stroke(234, 190, 108, i);
      sgram[i][col] = fft.getBand(i);
      r = map(sgram[i][col], 0, 1, 80, 300);
      x = r*cos(i);
      y = r*sin(i);
      bezier(xx(y-t), xx(y+t), yy1(x-t), yy1(x+t), 
              xx(i+t), yy(i+t), xx1(i+t), yy1(i+t)); 
  }
  endShape();
  
  t = t+0.025;
}

void keyPressed()
{
  if ( song.isPlaying() )
  {
    song.pause();
    noLoop();
  } else
  {
    // simply call loop again to resume playing from where it was paused
    song.loop();
    loop();
  }
}

float xx(float t){
    return cos(t / 10) * 100;
}

float yy(float t){
    return sin(-t / 10) * 100;
}

float xx1(float t){
    return cos(-t /10) * 280;
}

float yy1(float t){
    return sin(t / 10) * 150;
}
