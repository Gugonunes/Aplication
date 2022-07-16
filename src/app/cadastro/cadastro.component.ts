import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms'
import { logado, id } from '../login/login.component';
import {ApiService} from '../services/api.service'
import { Router } from '@angular/router';
import swal from 'sweetalert';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.css']
})

export class CadastroComponent implements OnInit {

  public islogado = logado;
  public CPF: String;

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

  constructor(
    private router: Router,
    private _api : ApiService,
  ) { }

  async ngOnInit(): Promise<any> {
    if(logado){
      await this._api.getDados(id).subscribe((res: any) => {
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
      await this._api.updateDados(data, logado).subscribe((res: any) => {
        if(res == -1){
          swal("Email já existe, informe outro!").then((value) => {
            document.getElementById('campoEmail')?.focus();
          });
        }
        else if(res == -2){
          swal("CPF já existe, informe outro!").then((value) => {
            document.getElementById('campoCPF')?.focus();
          });
        }
        else if(res == -3){
          swal("PIS já existe, informe outro!").then((value) => {
            document.getElementById('campoPIS')?.focus();
          });
        }
        else if(res == 1){
          swal("Usuário criado com sucesso, realize o login").then((value) => {
            this.router.navigate(["/"]);
          });
        }
        else if(res == 0){
          swal("Dados atualizados com sucesso").then((value) => {
            this.router.navigate(["/home"]);
          });
        }
      });
    } 

  async onDelete(CPF: any, logado : any){
    await this._api.deleteUsuario(CPF, logado).subscribe((res: any) => {
        if(res==0){
          this.islogado = false;
          swal("Usuário excluido com sucesso").then((value) => {
            this.router.navigate([""]);
          });
        }
    });
  }
}
