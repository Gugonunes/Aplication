import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {ApiService} from '../services/api.service'

export let logado = false; 
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
  }

  gotoCadastro(){
    this.router.navigate(['/cadastro']);
  }

  async onSubmit(login:any): Promise<any>{
    let b = login;
    console.log(b)
    await this._api.postTypeRequest('', b).subscribe((res: any) => {
        console.log(res);
        debugger;
    }, err => {
      console.log(err)
    });

    if(this.login == "gugonunes@hotmail.com"){
      // validarSenha
      // logado = true;
    }
    else{
      alert("email incorreto");
    }
  }
  
}
