import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

// Временные интерфейсы User и Order
interface User {
  name: string;
  email: string;
  loyaltyPoints?: number;
  favoriteProducts?: string[];
}

interface Order {
  id: number;
  date: string;
  status: string;
}

// Временный AuthService
class AuthService {
  getCurrentUser(): User | null {
    return {
      name: 'Иван Иванов',
      email: 'ivan@example.com',
      loyaltyPoints: 120,
      favoriteProducts: ['product1', 'product2']
    };
  }

  logout(): void {
    console.log('Logged out');
  }
}

// Временный OrderService
import { of } from 'rxjs';

class OrderService {
  getUserOrders() {
    const orders: Order[] = [
      { id: 1, date: '2025-04-20', status: 'completed' },
      { id: 2, date: '2025-04-18', status: 'pending' },
      { id: 3, date: '2025-04-15', status: 'delivered' },
      { id: 4, date: '2025-04-10', status: 'cancelled' },
    ];
    return of(orders);
  }
}

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [
    CommonModule,
    // убраны компоненты NavigationComponent, FooterComponent и LoadingComponent
  ],
  template: `
    <div *ngIf="isLoading">Загрузка...</div>
    <div *ngIf="!isLoading">
      <h2>Профиль: {{ user?.name }}</h2>
      <p>Email: {{ user?.email }}</p>
      <p>Бонусные баллы: {{ loyaltyPoints }}</p>
      <p>Избранные товары: {{ favoriteProductsCount }}</p>
      <p>Количество заказов: {{ orderCount }}</p>

      <h3>Последние заказы:</h3>
      <ul>
        <li *ngFor="let order of recentOrders">
          Заказ #{{ order.id }} – {{ getStatusText(order.status) }}
        </li>
      </ul>

      <button (click)="logout()">Выйти</button>
    </div>
  `,
  styles: []
})
export class ProfileComponent implements OnInit {
  user: User | null = null;
  isLoading = true;
  orderCount = 0;
  loyaltyPoints = 0;
  favoriteProductsCount = 0;
  recentOrders: Order[] = [];

  private authService = new AuthService();
  private orderService = new OrderService();

  ngOnInit(): void {
    this.loadUserData();
    this.loadOrderData();
  }

  private loadUserData(): void {
    this.user = this.authService.getCurrentUser();

    if (this.user) {
      this.loyaltyPoints = this.user.loyaltyPoints || 0;
      this.favoriteProductsCount = this.user.favoriteProducts?.length || 0;
    }

    this.isLoading = false;
  }

  private loadOrderData(): void {
    this.orderService.getUserOrders().subscribe({
      next: (orders: Order[]) => {
        this.orderCount = orders.length;
        this.recentOrders = orders.slice(0, 3);
      },
      error: (err: Error) => {
        console.error('Ошибка при загрузке заказов:', err);
      }
    });
  }

  getStatusText(status: string): string {
    const statusMap: Record<string, string> = {
      'completed': 'Завершен',
      'pending': 'В обработке',
      'cancelled': 'Отменен',
      'delivered': 'Доставлен'
    };
    return statusMap[status] || status;
  }

  logout(): void {
    this.authService.logout();
  }
}
