import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { finalize } from 'rxjs/operators';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  loginForm: FormGroup;
  isLoading = false;
  errorMessage: string | null = null;
  showPassword = false; // Добавлено для переключения видимости пароля

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
      rememberMe: [false] // Добавлена опция "Запомнить меня"
    });
  }

  // Геттеры для удобного доступа к полям формы
  get email() { return this.loginForm.get('email'); }
  get password() { return this.loginForm.get('password'); }
  get rememberMe() { return this.loginForm.get('rememberMe'); }

  onSubmit(): void {
    if (this.loginForm.invalid) {
      this.markFormGroupTouched(this.loginForm);
      return;
    }

    this.isLoading = true;
    this.errorMessage = null;

    const credentials = {
      email: this.loginForm.value.email.trim(),
      password: this.loginForm.value.password,
      rememberMe: this.loginForm.value.rememberMe
    };

    this.authService.login(credentials)
      .pipe(
        finalize(() => this.isLoading = false)
      )
      .subscribe({
        next: () => this.handleLoginSuccess(),
        error: (err) => this.handleLoginError(err)
      });
  }

  private handleLoginSuccess(): void {
    const returnUrl = this.router.parseUrl(this.router.url).queryParams['returnUrl'] || '/';
    this.router.navigateByUrl(returnUrl);
  }

  private handleLoginError(err: HttpErrorResponse): void {
    console.error('Login error:', err);
    this.errorMessage = this.getErrorMessage(err);
    
    // Автоматическая очистка ошибки через 5 секунд
    setTimeout(() => {
      this.errorMessage = null;
    }, 5000);
  }

  navigateToRegister(event?: Event): void {
    event?.preventDefault();
    this.router.navigate(['/register'], {
      queryParams: { from: 'login' }
    });
  }

  navigateToPasswordReset(event?: Event): void {
    event?.preventDefault();
    this.router.navigate(['/password-reset']);
  }

  togglePasswordVisibility(): void {
    this.showPassword = !this.showPassword;
  }

  private markFormGroupTouched(formGroup: FormGroup): void {
    Object.values(formGroup.controls).forEach(control => {
      control.markAsTouched();
      if (control instanceof FormGroup) {
        this.markFormGroupTouched(control);
      }
    });
  }

  private getErrorMessage(error: HttpErrorResponse): string {
    if (error.error?.message) {
      return error.error.message;
    }

    switch (error.status) {
      case 0: return 'Ошибка соединения с сервером';
      case 400: return 'Неверный запрос. Проверьте введенные данные';
      case 401: return 'Неверный email или пароль';
      case 403: return 'Доступ запрещен. Обратитесь к администратору';
      case 404: return 'Сервис авторизации недоступен';
      case 429: return 'Слишком много попыток. Попробуйте позже';
      case 500: return 'Ошибка сервера. Пожалуйста, попробуйте позже';
      case 503: return 'Сервис временно недоступен';
      default: return 'Произошла неизвестная ошибка';
    }
  }
}