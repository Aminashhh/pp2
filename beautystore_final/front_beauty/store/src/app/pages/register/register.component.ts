import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, AbstractControlOptions } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { finalize } from 'rxjs/operators';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  registerForm: FormGroup;
  isLoading = false;
  errorMessage: string | null = null;
  successMessage: string | null = null;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {
    this.registerForm = this.fb.group({
      name: ['', [Validators.required, Validators.minLength(2), Validators.maxLength(50)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [
        Validators.required,
        Validators.minLength(6),
        Validators.pattern(/^(?=.*[A-Za-z])(?=.*\d).+$/) // Хотя бы одна буква и цифра
      ]],
      confirmPassword: ['', Validators.required]
    }, {
      validator: this.passwordMatchValidator
    } as AbstractControlOptions);
  }

  // Геттеры для удобного доступа к полям формы
  get name() { return this.registerForm.get('name'); }
  get email() { return this.registerForm.get('email'); }
  get password() { return this.registerForm.get('password'); }
  get confirmPassword() { return this.registerForm.get('confirmPassword'); }

  // Валидатор совпадения паролей
  private passwordMatchValidator(form: FormGroup) {
    const password = form.get('password');
    const confirmPassword = form.get('confirmPassword');
    return password && confirmPassword && password.value === confirmPassword.value 
      ? null 
      : { mismatch: true };
  }

  onSubmit() {
    if (this.registerForm.invalid) {
      this.markFormGroupTouched(this.registerForm);
      this.errorMessage = 'Пожалуйста, заполните все поля правильно';
      return;
    }

    this.isLoading = true;
    this.errorMessage = null;
    this.successMessage = null;

    const userData = {
      name: this.registerForm.value.name.trim(),
      email: this.registerForm.value.email.trim().toLowerCase(),
      password: this.registerForm.value.password
    };

    this.authService.register(userData)
      .pipe(
        finalize(() => this.isLoading = false)
      )
      .subscribe({
        next: (res) => this.handleRegistrationSuccess(res),
        error: (err) => this.handleRegistrationError(err)
      });
  }

  private handleRegistrationSuccess(res: any): void {
    this.successMessage = 'Регистрация прошла успешно! Вы будете перенаправлены на страницу входа...';
    setTimeout(() => {
      this.router.navigate(['/login'], {
        queryParams: { registered: true, email: this.registerForm.value.email }
      });
    }, 2000);
  }

  private handleRegistrationError(err: HttpErrorResponse): void {
    console.error('Registration error:', err);
    this.errorMessage = this.getErrorMessage(err);
  }

  navigateToLogin(event?: Event): void {
    event?.preventDefault();
    this.router.navigate(['/login'], {
      queryParams: { from: 'register' }
    });
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
      case 400: return 'Некорректные данные';
      case 409: return 'Пользователь с таким email уже существует';
      case 500: return 'Ошибка сервера. Пожалуйста, попробуйте позже';
      default: return 'Произошла ошибка при регистрации';
    }
  }
}