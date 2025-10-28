import { Component } from '@angular/core';
import { Video } from '../../componnets/video/video';
import { Search } from "../../componnets/search/search";
import { SideBar } from "../../componnets/side-bar/side-bar";



@Component({
  selector: 'app-home',
  imports: [Video, Search, SideBar],
  templateUrl: './home.html',
  styleUrl: './home.scss',
})
export class Home {


  
  

}
