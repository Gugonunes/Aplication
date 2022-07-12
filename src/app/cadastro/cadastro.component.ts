import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms'
import { logado, id } from '../login/login.component';
import {ApiService} from '../services/api.service'
@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.css']
})

export class CadastroComponent implements OnInit {

  formCadastro = new FormGroup({
    NomeCompleto: new FormControl(''),
    Email: new FormControl(''),
    Pais: new FormControl(''),
    Estado: new FormControl(''),
    Municipio: new FormControl(''),
    CEP: new FormControl(''),
    Rua: new FormControl(''),
    Numero: new FormControl(''),
    Complemento: new FormControl(''),
    CPF: new FormControl(''),
    PIS: new FormControl(''),
    Senha: new FormControl('')
  });

  constructor(private _api : ApiService,) { }

  async ngOnInit(): Promise<any> {
    if(logado){
      //this.formCadastro.patchValue({nomeCompleto: 'gustavo'});
      await this._api.getDados(id).subscribe((res: any) => {
        console.log(res);
        this.formCadastro.patchValue({
          NomeCompleto: res[0],
          Senha:res[1],
          Email:res[2],
          Pais:res[3],
          Estado:res[4],
          Municipio:res[5],
          CEP:res[6],
          Rua:res[7],
          Numero:res[8],
          Complemento:res[9],
          CPF:res[10],
          PIS:res[11],
        });
          
      });
    }
  }

  async onSubmit(data: any): Promise<void>{
    await this._api.updateDados(data).subscribe((res: any) => {
      console.log(data);
    });
    
  }
}
