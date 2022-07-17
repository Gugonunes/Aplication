import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {ApiService} from '../services/api.service'
import swal from 'sweetalert';

export let logado = false; 
export let id = '';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})


export class LoginComponent implements OnInit {

  public login: String;
  public senha: String;
  constructor(
    private router: Router,
    private _api : ApiService,
  ) { }

  //ao entrar na pagina de login, todos os usuarios sao deslogados automaticamente
  ngOnInit(): void {
    logado = false;
    id = '';
  }

  gotoCadastro(){
    this.router.navigate(['/cadastro']);
  }
  gotoHome(login:any){
    id = login;
    this.router.navigate(['/home']);
  }
  //função de onsubmit, que envia os dados do login e senha para a api, para realizar a verificação do login no banco
  async onSubmit(login:any, senha:any): Promise<any>{
    await this._api.postTypeRequest('', login, senha).subscribe((res: any) => {
        if(res==-1){
          swal("Senha inválida, tente novamente").then((value) => {
            document.getElementById('senha')?.focus();
          });
        }
        //se estiver tudo certo, usuario é logado e enviado para a home
        else if(res==0){
          logado = true;
          this.gotoHome(login);
        }
        else if(res==-2){
          swal("Usuário ou senha invalidos, tente novamente").then((value) => {
            document.getElementById('login')?.focus();
          });
        }
    }, err => {
      console.log(err)
    });
  }
  
}
