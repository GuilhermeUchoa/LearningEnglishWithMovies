import { Component, Output } from '@angular/core';
import videoData from '../../../../public/data/words_db.json';
import { FormsModule } from '@angular/forms';
import { DataService } from '../../service/data-service';

@Component({
  selector: 'app-search',
  imports: [FormsModule],
  templateUrl: './search.html',
  styleUrl: './search.scss',
})
export class Search {
  searchTerm = '';

  constructor(private dataService: DataService) {}

  onInput() {
    this.dataService.onSearch(this.searchTerm);
  }
}
