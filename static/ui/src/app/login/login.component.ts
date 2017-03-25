import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";

@Component({
    selector: 'ui-login',
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
    private loginForm: FormGroup;

    constructor(private fb: FormBuilder) {
    }

    ngOnInit() {
        this.createFormLogin();
    }

    createFormLogin() {

        this.loginForm = this.fb.group({
            username: this.fb.control('', Validators.compose([Validators.required])),
            password: this.fb.control('', Validators.compose([Validators.required])),
        });
    }

    onLoginSubmit(data) {
        console.log(data);
    }
}
