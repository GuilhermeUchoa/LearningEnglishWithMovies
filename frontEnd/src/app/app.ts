import { CommonModule } from '@angular/common';
import { Component, signal } from '@angular/core';


@Component({
  selector: 'app-root',
  imports: [CommonModule],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {

  numVideo = 1;
  linkVideo = `assets/cortes_curto_legenda/clip_${this.numVideo}.mp4`;

  nextVideo(){
    this.numVideo++;
    document.getElementById('videoPlayer')?.setAttribute('src', `assets/cortes_curto_legenda/clip_${this.numVideo}.mp4`);
  }

  lastVideo(){
    if(this.numVideo > 1){
      this.numVideo--;
      document.getElementById('videoPlayer')?.setAttribute('src', `assets/cortes_curto_legenda/clip_${this.numVideo}.mp4`);
    }
  }
  
}
