import { Injectable } from '@angular/core';
import words_db from '../../../public/data/words_db.json';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class DataService {
  private dataSource = new BehaviorSubject<any[]>(words_db);
  data$ = this.dataSource.asObservable();

  constructor() {}

  onSearch(searchTerm: string = '') {
    try {
      const regex = new RegExp(searchTerm, 'i');
      const filtered = words_db.filter((video) => regex.test(video.TEXT) || regex.test(video.CLIP_NAME));
      this.dataSource.next(filtered);
    } catch {
      this.dataSource.next(words_db);
    }
  }
}
