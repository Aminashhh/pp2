import { Injectable } from '@angular/core';
import { CanActivate, Router, UrlTree } from '@angular/router';
import { Observable, of, switchMap, take, catchError } from 'rxjs';
import { AuthService } from '../services/auth.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  canActivate(): Observable<boolean | UrlTree> | boolean | UrlTree {
    // Быстрая проверка наличия токена
    if (!this.authService.isAuthenticated()) {
      return this.createLoginUrlTree();
    }

    // Проверка наличия данных пользователя
    const currentUser = this.authService.getCurrentUser();
    if (currentUser) {
      return true;
    }

    // Загрузка данных пользователя при наличии токена
    return this.authService.currentUser$.pipe(
      take(1),
      switchMap(user => {
        if (user) {
          return of(true);
        }
        return this.handleUserProfileFetch();
      }),
      catchError(() => of(this.createLoginUrlTree()))
    );
  }

  private handleUserProfileFetch(): Observable<boolean | UrlTree> {
    return this.authService.fetchUserProfile().pipe(
      switchMap(() => of(true)),
      catchError(() => {
        this.authService.logout();
        return of(this.createLoginUrlTree());
      })
    );
  }

  private createLoginUrlTree(): UrlTree {
    const currentUrl = this.router.url;
    const queryParams = this.shouldPreserveUrl(currentUrl) 
      ? { returnUrl: currentUrl }
      : undefined;

    return this.router.createUrlTree(['/login'], { queryParams });
  }

  private shouldPreserveUrl(url: string): boolean {
    const excludedUrls = ['/login', '/register', '/password-reset'];
    return !!url && !excludedUrls.some(excluded => url.startsWith(excluded));
  }
}