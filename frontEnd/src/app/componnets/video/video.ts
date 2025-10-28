import { Component } from '@angular/core';

import { ButtonModule } from 'primeng/button';
import { DataService } from '../../service/data-service';

@Component({
  selector: 'app-video',
  standalone: true,
  imports: [ButtonModule],
  templateUrl: './video.html',
  styleUrl: './video.scss',
})
export class Video {
  numberVideo: number = 0; // Numero do video
  videoData: any; // Dado geral
  objectVideo: any; // Video Atual

  constructor(private DataService_: DataService) {}

  ngOnInit() {
    this.DataService_.data$.subscribe((res) => {
      this.videoData = res
      this.objectVideo = this.videoData[0];
      this.numberVideo = 0;
      console.log("Video atualizado");
      
    });
  }

  nextButton() {
    this.numberVideo++;
    if (this.numberVideo >= this.videoData.length) {
      this.numberVideo = 0;
    }
    this.objectVideo = this.videoData[this.numberVideo];
  }

  previousButton() {
    this.numberVideo--;
    if (this.numberVideo < 0) {
      this.numberVideo = this.videoData.length - 1;
    }
    this.objectVideo = this.videoData[this.numberVideo];
  }
}
