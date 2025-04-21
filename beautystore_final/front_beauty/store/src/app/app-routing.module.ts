import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from './guards/auth.guard';
import { LoginComponent } from './pages/login/login.component';
import { RegisterComponent } from './pages/register/register.component';
import { ProfileComponent } from './pages/profile/profile.component';
import { FavoritesComponent } from './pages/favorites/favorites.component';
import { OrdersComponent } from './pages/orders/orders.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  // Основные маршруты
  { 
    path: '',
    redirectTo: 'login',
    pathMatch: 'full'
  },
  {
    path: 'login',
    component: LoginComponent,
    data: { 
      title: 'Вход в систему',
      animation: 'loginPage'
    }
  },
  {
    path: 'register',
    component: RegisterComponent,
    data: { 
      title: 'Регистрация',
      animation: 'registerPage' 
    }
  },
  // Защищенные маршруты (только для авторизованных пользователей)
  {
    path: 'home',
    component: HomeComponent,
    canActivate: [AuthGuard],
    data: { 
      title: 'Главная',
      requiresAuth: true 
    }
  },
  {
    path: 'profile',
    component: ProfileComponent,
    canActivate: [AuthGuard],
    data: { 
      title: 'Профиль',
      requiresAuth: true 
    }
  },
  {
    path: 'favorites',
    component: FavoritesComponent,
    canActivate: [AuthGuard],
    data: { 
      title: 'Избранное',
      requiresAuth: true 
    }
  },
  {
    path: 'orders',
    component: OrdersComponent,
    canActivate: [AuthGuard],
    data: { 
      title: 'Заказы',
      requiresAuth: true 
    }
  },
  
  { 
    path: '**',
    redirectTo: 'login'
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, {
      scrollPositionRestoration: 'enabled',
      anchorScrolling: 'enabled',
      enableTracing: false // Включите для отладки маршрутизации
    })
  ],
  exports: [RouterModule],
  providers: [AuthGuard]
})
export class AppRoutingModule { }