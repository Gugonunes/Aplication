import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {ApiService} from '../services/api.service'

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

  async onSubmit(login:any, senha:any): Promise<any>{
    await this._api.postTypeRequest('', login, senha).subscribe((res: any) => {
        if(res==-1){
          alert("Senha inválida, tente novamente");
        }
        else if(res==0){
          console.log("Senha correta");
          logado = true;
          this.gotoHome(login);
        }
        else if(res==-2){
          alert("Usuário ou senha invalidos");
        }
    }, err => {
      console.log(err)
    });
  }
  
}
