import {Injectable} from '@angular/core';
import {Headers, Http, RequestOptions, Response} from "@angular/http";

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import {Observable} from "rxjs";

@Injectable()
export class AuthService {
    private URL_VALID = 'http://localhost:8000/v1/monitor/token_check/';
    private TOKEN_URL = 'http://localhost:8000/v1/monitor/token_auth/';

    constructor(private http: Http) {
    }

    isValid() {
        let qwerty = localStorage.getItem('qwerty');
        if(!qwerty) {qwerty = 'a'}

        let headers = new Headers;
        headers.set('Content-Type', 'application/json');
        let options = new RequestOptions({headers: headers});

        return this.http.get(`${this.URL_VALID}${qwerty}`, options)
            .map(
                (res: Response) => {
                    let body = res.json();
                    return body['exist'];
                }
            )
            .catch(
                (err: Response | any) => {
                    if (err instanceof Response) {
                        return Observable.throw(err.json());
                    }
                    else {
                        return err.messages;
                    }
                }
            );
    }

    cobaLogin(user, pass) {
        let body = {
            'username': user,
            'password': pass
        };

        let headers = new Headers();
        headers.set('Content-Type', 'application/json');

        let option = new RequestOptions({headers: headers});

        return this.http.post(this.TOKEN_URL, body, option)
            .map((res: Response) => {
                return res.json();
            })
            .catch((err: Response | any) => {
                if (err instanceof Response) {
                    let body = err.json();

                    return Observable.throw(body);
                }
                else {
                    return err.message;
                }
            });
    }
}
