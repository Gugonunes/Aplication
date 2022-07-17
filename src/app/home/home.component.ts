import { Component, OnInit } from '@angular/core';
import { logado, id } from '../login/login.component';
import { Router } from '@angular/router';
import {ApiService} from '../services/api.service'

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  public Usuario: String;
  constructor(
    private router: Router,
    private _api : ApiService,
  ) { }

  //a pagina home de forma simples possui apenas dois botoes, entao na função oninit foi colocada a chamada da api para retornar o nome do usuario logado
  async ngOnInit(): Promise<any> {
    if(logado == true){
      await this._api.getNome(id).subscribe((res: any) => {
        this.Usuario = res;
    });
    }
    //validação: se o usuario nao estiver logado ele é enviado novamente para o login
    else{
      this.router.navigate(['']);
    }
    
  }

}
