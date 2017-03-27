import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {AuthService} from "../services/auth.service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
    selector: 'ui-login',
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
    private loginForm: FormGroup;
    private isError: boolean = false;
    private isShow: boolean = false;
    private key: any;
    private message: any;

    constructor(private fb: FormBuilder,
                private auth: AuthService,
                private activ: ActivatedRoute,
                private route: Router) {
        this.activ.params.subscribe(
            () => {
                if (localStorage.getItem('qwerty')) {
                    //noinspection JSIgnoredPromiseFromCall
                    route.navigate(['']);
                }
            }
        );
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
        let u = data['username'];
        let p = data['password'];

        this.isShow = true;
        this.auth.cobaLogin(u, p).subscribe(
            (body) => {
                this.isError = false;

                localStorage.setItem('qwerty', body['token']);
                localStorage.setItem('user', body['name']);
                localStorage.setItem('super', body['isSuper']);
                //noinspection JSIgnoredPromiseFromCall
                this.route.navigate(['']);
                this.isShow = false;
            },

            err => {
                this.isError = true;
                this.isShow = false;
                this.key = Object.keys(err);
                this.message = err;
            }
        );
    }
}
