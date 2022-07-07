import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms'
import { logado } from '../login/login.component';
@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.css']
})

export class CadastroComponent implements OnInit {

  formCadastro = new FormGroup({
    nomeCompleto: new FormControl(''),
    email: new FormControl(''),
    pais: new FormControl(''),
    estado: new FormControl(''),
    municipio: new FormControl(''),
    CEP: new FormControl(''),
    Rua: new FormControl(''),
    Numero: new FormControl(''),
    Complemento: new FormControl(''),
    CPF: new FormControl(''),
    PIS: new FormControl(''),
    senha: new FormControl('')
  });

  constructor() { }

  ngOnInit(): void {
    if(logado){
      this.formCadastro.patchValue({nomeCompleto: 'gustavo'});
    }
  }

  onSubmit(): void{
    alert('Cadastro realizado com sucesso');
  }
}
