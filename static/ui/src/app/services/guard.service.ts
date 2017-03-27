import {Injectable} from '@angular/core';
import {CanActivate, Router} from "@angular/router";
import {AuthService} from "./auth.service";

@Injectable()
export class GuardService implements CanActivate {
    constructor(private auth: AuthService, private router: Router) {
    }

    canActivate() {
        return this.checkValidSimple();
    }

    checkValid() {
        return this.auth.isValid()
            .map(
                res => {
                    if (!res) {
                        //noinspection JSIgnoredPromiseFromCall
                        this.router.navigate(['login']);
                        return false
                    }
                    return res
                }
            );
    }

    checkValidSimple() {
        let qwerty = localStorage.getItem('qwerty');

        if (qwerty) {
            return true;
        }
        else {
            //noinspection JSIgnoredPromiseFromCall
            this.router.navigate(['login']);
            return false
        }
    }
}
