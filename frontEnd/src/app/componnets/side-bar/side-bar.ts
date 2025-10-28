import { Component } from '@angular/core';
import { DataService } from '../../service/data-service';


@Component({
  selector: 'app-side-bar',
  imports: [],
  templateUrl: './side-bar.html',
  styleUrl: './side-bar.scss',
})
export class SideBar {

  constructor(private _DataService:DataService){}

  termos :any = [
    "you","future",'look','time'
  ]

  searchTermOnClick(event:any){

    this._DataService.onSearch(event.target.textContent)
    console.log(event.target.textContent)
  }
}
