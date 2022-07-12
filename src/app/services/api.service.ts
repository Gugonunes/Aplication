import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ApiService {


  private REST_API_SERVER = "http://localhost:8000/";
  constructor(private httpClient: HttpClient) { }

  getTypeRequest(url: string) {
    return this.httpClient.get(this.REST_API_SERVER+url).pipe(map(res => {
      return res;
    }));
  }

  postTypeRequest(url: string, login: any, senha: any) {
    return this.httpClient.post(this.REST_API_SERVER+url+login+"/"+senha, login).pipe(map(res => {
      return res;
    }));
  }
  getDados(id: any) {
    return this.httpClient.get(this.REST_API_SERVER+id).pipe(map(res => {
      return res;
    }));
  }

}