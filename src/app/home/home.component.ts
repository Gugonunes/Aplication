import { Component, OnInit } from '@angular/core';
import { logado } from '../login/login.component';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  public Usuario: String;
  constructor(private router: Router) { }

  ngOnInit(): void {
    if(logado == true){
      this.Usuario = 'Gustavo';
    }
    else{
      this.router.navigate(['']);
    }
    
  }

}
