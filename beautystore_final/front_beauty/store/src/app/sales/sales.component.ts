import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-sales',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './sales.component.html',
  styleUrls: ['./sales.component.css']
})
export class SalesComponent {
  promotions = [
    {
      imageUrl: 'assets/sale1.jpg',
      title: 'День Влюбленных с Beautystore!'
    },
    {
      imageUrl: 'assets/sale2.jpg',
      title: 'Дополнительная скидка -10% по промокоду LOVE_SAA'
    },
    {
      imageUrl: 'assets/sale3.jpg',
      title: 'Super предложение для него и для нее!'
    }
  ];
}
