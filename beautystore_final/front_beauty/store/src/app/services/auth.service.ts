import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Router } from '@angular/router';
import { BehaviorSubject, Observable, throwError } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';

interface User {
  id: number;
  email: string;
  name?: string;
  // Добавьте другие поля пользователя по необходимости
}

interface AuthResponse {
  token: string;
  user: User;
}

interface RegisterResponse {
  message: string;
  user?: User;
  token?: string;
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private readonly API_URL = 'http://localhost:8000/api';
  private readonly TOKEN_KEY = 'cosmetic_store_token';
  private readonly USER_KEY = 'cosmetic_store_user';
  
  private currentUserSubject = new BehaviorSubject<User | null>(null);
  public currentUser$ = this.currentUserSubject.asObservable();

  constructor(private http: HttpClient, private router: Router) {
    this.initializeAuthState();
  }

  /**
   * Авторизация пользователя
   */
  login(credentials: {email: string, password: string}): Observable<AuthResponse> {
    return this.http.post<AuthResponse>(`${this.API_URL}/login`, credentials).pipe(
      tap(response => this.handleAuthSuccess(response)),
      catchError(error => this.handleAuthError(error))
    );
  }

  /**
   * Регистрация нового пользователя
   */
  register(userData: {name: string, email: string, password: string}): Observable<RegisterResponse> {
    return this.http.post<RegisterResponse>(`${this.API_URL}/register`, userData).pipe(
      tap(response => {
        if (response.token && response.user) {
          this.handleAuthSuccess({
            token: response.token,
            user: response.user
          });
        }
      }),
      catchError(error => this.handleAuthError(error))
    );
  }

  /**
   * Получение профиля пользователя
   */
  fetchUserProfile(): Observable<User> {
    return this.http.get<User>(`${this.API_URL}/profile`).pipe(
      tap(user => {
        this.saveUser(user);
        this.currentUserSubject.next(user);
      }),
      catchError(error => {
        this.clearAuth();
        return throwError(() => this.handleError(error));
      })
    );
  }

  /**
   * Выход из системы
   */
  logout(): void {
    this.clearAuth();
    this.router.navigate(['/login']);
  }

  /**
   * Обновление токена
   */
  refreshToken(): Observable<{ token: string }> {
    return this.http.post<{ token: string }>(`${this.API_URL}/refresh-token`, {}).pipe(
      tap(response => this.saveToken(response.token)),
      catchError(error => {
        this.clearAuth();
        return throwError(() => this.handleError(error));
      })
    );
  }

  // ======== Публичные методы доступа к состоянию ========
  getToken(): string | null {
    return localStorage.getItem(this.TOKEN_KEY);
  }

  isAuthenticated(): boolean {
    return !!this.getToken();
  }

  getCurrentUser(): User | null {
    return this.currentUserSubject.value;
  }

  // ======== Приватные методы ========
  private initializeAuthState(): void {
    const token = this.getToken();
    const user = this.getStoredUser();
    
    if (token && user) {
      this.currentUserSubject.next(user);
    } else if (token) {
      this.fetchUserProfile().subscribe({
        error: () => this.clearAuth()
      });
    }
  }

  private handleAuthSuccess(response: AuthResponse): void {
    this.saveToken(response.token);
    this.saveUser(response.user);
    this.currentUserSubject.next(response.user);
  }

  private handleAuthError(error: HttpErrorResponse): Observable<never> {
    this.clearAuth();
    return throwError(() => this.handleError(error));
  }

  private saveToken(token: string): void {
    localStorage.setItem(this.TOKEN_KEY, token);
  }

  private saveUser(user: User): void {
    localStorage.setItem(this.USER_KEY, JSON.stringify(user));
  }

  private getStoredUser(): User | null {
    const userData = localStorage.getItem(this.USER_KEY);
    return userData ? JSON.parse(userData) : null;
  }

  private clearAuth(): void {
    localStorage.removeItem(this.TOKEN_KEY);
    localStorage.removeItem(this.USER_KEY);
    this.currentUserSubject.next(null);
  }

  private handleError(error: HttpErrorResponse): string {
    console.error('AuthService error:', error);
    
    if (error.error?.message) {
      return error.error.message;
    }

    switch (error.status) {
      case 0: return 'Ошибка соединения с сервером';
      case 400: return 'Некорректные данные';
      case 401: return 'Неавторизованный доступ';
      case 403: return 'Доступ запрещен';
      case 404: return 'Ресурс не найден';
      case 409: return 'Пользователь уже существует';
      case 500: return 'Ошибка сервера';
      default: return 'Произошла неизвестная ошибка';
    }
  }
}