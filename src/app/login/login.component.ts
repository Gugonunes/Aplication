import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

export let logado = false; 
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})


export class LoginComponent implements OnInit {

  public login: String;
  public senha: String;
  constructor(private router: Router) { }

  gotoCadastro(){
    this.router.navigate(['/cadastro']);
  }

  onSubmit(): any{
    if(this.login == "gugonunes@hotmail.com"){
      //validarSenha
      logado = true;
      this.router.navigate(['home']);
    }
    else{
      alert("email incorreto");
    }
  }
  ngOnInit(): void {
    logado = false;
  }

}
