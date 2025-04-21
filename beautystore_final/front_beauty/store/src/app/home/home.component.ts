import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  showCookies = true;

  acceptCookies() {
    this.showCookies = false;
    // Здесь можно добавить логику сохранения согласия
  }
}