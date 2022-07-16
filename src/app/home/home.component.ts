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

  async ngOnInit(): Promise<any> {
    if(logado == true){
      await this._api.getNome(id).subscribe((res: any) => {
        this.Usuario = res;
    });
    }
    else{
      this.router.navigate(['']);
    }
    
  }

}
