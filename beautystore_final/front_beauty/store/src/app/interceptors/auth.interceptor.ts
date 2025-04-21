import { Injectable } from '@angular/core';
import {
  HttpInterceptor,
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpErrorResponse,
  HttpResponse
} from '@angular/common/http';
import { Observable, throwError, from } from 'rxjs';
import { catchError, switchMap, tap } from 'rxjs/operators';
import { AuthService } from '../services/auth.service';
import { Router } from '@angular/router';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  private isRefreshing = false;
  private refreshTokenUrl = '/auth/refresh-token';

  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  intercept(
    req: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    if (this.isAuthRequest(req)) {
      return next.handle(req);
    }

    const authReq = this.addTokenToRequest(req);

    return next.handle(authReq).pipe(
      tap(event => {
        if (event instanceof HttpResponse && event.body?.token) {
          this.authService.saveToken(event.body.token);
        }
      }),
      catchError(error => {
        if (error instanceof HttpErrorResponse) {
          return this.handleAuthError(error, req, next);
        }
        return throwError(() => error);
      })
    );
  }

  private addTokenToRequest(req: HttpRequest<any>): HttpRequest<any> {
    const token = this.authService.getToken();
    return token ? req.clone({
      setHeaders: { Authorization: `Bearer ${token}` }
    }) : req;
  }

  private isAuthRequest(req: HttpRequest<any>): boolean {
    const authUrls = ['/auth/login', '/auth/register', this.refreshTokenUrl];
    return authUrls.some(url => req.url.includes(url));
  }

  private handleAuthError(
    error: HttpErrorResponse,
    originalRequest: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    if (error.status === 401) {
      if (originalRequest.url.includes(this.refreshTokenUrl)) {
        this.authService.logout();
        return this.redirectToLogin();
      }

      return from(this.handleTokenRefresh()).pipe(
        switchMap(() => next.handle(this.addTokenToRequest(originalRequest))),
        catchError(() => {
          this.authService.logout();
          return this.redirectToLogin();
        })
      );
    }

    if (error.status === 403) {
      this.router.navigate(['/forbidden']);
    }

    return throwError(() => error);
  }

  private async handleTokenRefresh(): Promise<boolean> {
    if (this.isRefreshing) {
      return this.waitForRefreshCompletion();
    }

    this.isRefreshing = true;
    
    try {
      const response = await this.authService.refreshToken().toPromise();
      
      if (!response?.token) {
        throw new Error('Invalid refresh token response');
      }

      this.authService.saveToken(response.token);
      return true;
    } catch (error) {
      console.error('Token refresh failed:', error);
      this.authService.logout();
      throw error;
    } finally {
      this.isRefreshing = false;
    }
  }

  private waitForRefreshCompletion(): Promise<boolean> {
    return new Promise(resolve => {
      const interval = setInterval(() => {
        if (!this.isRefreshing) {
          clearInterval(interval);
          resolve(true);
        }
      }, 100);
    });
  }

  private redirectToLogin(): Observable<never> {
    const returnUrl = this.router.routerState.snapshot.url;
    this.router.navigate(['/login'], {
      queryParams: { 
        returnUrl: returnUrl !== '/' ? returnUrl : undefined,
        sessionExpired: true
      }
    });
    return throwError(() => new Error('Session expired'));
  }
}