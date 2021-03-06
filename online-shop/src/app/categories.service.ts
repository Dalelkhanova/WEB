import { Injectable } from '@angular/core';
import { Category } from './category';
import {Observable} from 'rxjs';
import { HttpClient} from '@angular/common/http';
import {LoginResponse} from './login';
import { RegistrationResponse } from './registrate';

@Injectable({
  providedIn: 'root'
})
export class CategoriesService {


  constructor(
    private http: HttpClient) { }

  getCategories(): Observable<Category[]> {
    return this.http.get<Category[]>('http://localhost:8000/api/categories');
  }

  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>('http://localhost:8000/api/login/', {
      username,
      password
    });
  }

  registr(username, password): Observable<RegistrationResponse> {
    return this.http.post<RegistrationResponse>('http://localhost:8000/api/newusers/', {
      username,
      password
    });
  }
}