import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ApiService {


  private REST_API_SERVER = "http://localhost:8000/";
  constructor(private httpClient: HttpClient) { }
  //função base de teste do backend
  getTypeRequest(url: string) {
    return this.httpClient.get(this.REST_API_SERVER+url).pipe(map(res => {
      return res;
    }));
  }
  //função do login
  postTypeRequest(url: string, login: any, senha: any) {
    return this.httpClient.post(this.REST_API_SERVER+url+login+"/"+senha, login).pipe(map(res => {
      return res;
    }));
  }
  //função que retona os dados do usuario
  getDados(id: any) {
    return this.httpClient.get(this.REST_API_SERVER+id).pipe(map(res => {
      return res;
    }));
  }
  //função que chama a atualização ou cadastro de novo usuário
  updateDados(data: any, logado: boolean){
    let NomeCompleto = data.value.NomeCompleto;
    let Senha = data.value.Senha;
    let Email = data.value.Email;
    let Pais = data.value.Pais;
    let Estado = data.value.Estado;
    let Municipio = data.value.Municipio;
    let CEP = data.value.CEP;
    let Rua = data.value.Rua;
    let Numero = data.value.Numero;
    let Complemento = data.value.Complemento;
    let CPF = data.value.CPF;
    let PIS = data.value.PIS;
    let dados = NomeCompleto+"/"+Senha+"/"+Email+"/"+Pais+"/"+Estado+"/"+Municipio+"/"+CEP+"/"+Rua+"/"+Numero+"/"+Complemento+"/"+CPF+"/"+PIS+"/"+logado
    return this.httpClient.get(this.REST_API_SERVER+"update/"+dados).pipe(map(res => {
      return res;
    }));
  }
  //função de deletar usuario
  deleteUsuario(data: any, logado: boolean){
    return this.httpClient.get(this.REST_API_SERVER+"delete/" + data + "/" + logado).pipe(map(res => {
      return res;
    }));
  }
  //função que retorna o nome do usuario na pagina home
  getNome(id:any){
    return this.httpClient.get(this.REST_API_SERVER+"nome/"+id).pipe(map(res => {
      return res;
    }));
  }
}