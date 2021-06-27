import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ExampleService {
  params = {};
  headers = new HttpHeaders({
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
  });
  private baseUrl = 'https://hack-the-mountain.herokuapp.com';
  constructor(private http: HttpClient) {}

  // GET -> Get all the links for a project specified by the id_project.
  getLinks(): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/links`);
  }

  // POST -> Upload a new link for a project specified by the id_project.
  addLink(id_project: number, queryParams: any): Observable<any> {
    return this.http.post<any>(
      `${this.baseUrl}/projects/${id_project}/links`,
      queryParams
    );
  }

  // DELETE -> Delete link specified by id_project_link
  deleteLink(id_project: number, id_link: number): Observable<any> {
    return this.http.delete<any>(`${this.baseUrl}/links/${id_link}`);
  }

  // PUT -> Edit link for a project specified by the id_project.
  editLink(id_link: number, queryParams: any): Observable<any> {
    return this.http.put<any>(`${this.baseUrl}/links/${id_link}`, queryParams);
  }

  // EXAMPLE I call it in sign in page and console log it
  checkHealth(): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/health`, {
      headers: this.headers,
    });
  }
}
