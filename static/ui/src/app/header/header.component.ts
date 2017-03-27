import {Component, OnInit} from '@angular/core';
import {NavigationEnd, Router} from "@angular/router";

@Component({
    selector: 'app-header',
    templateUrl: './header.component.html',
    styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
    private status: boolean;
    private isAuth: boolean;

    constructor(private route: Router) {
        this.route.events.subscribe(
            val => {
                if (val instanceof NavigationEnd) {
                    let qwerty = localStorage.getItem('qwerty');

                    this.isAuth = !!qwerty;
                }
            }
        );
    }

    ngOnInit() {
    }

    onStatusClicked(status) {
        this.status = status;
    }

    onClicked(e) {
        this.isAuth = false;
        localStorage.setItem('qwerty', '');
        localStorage.setItem('user', '');
        localStorage.setItem('super', '');
        //noinspection JSIgnoredPromiseFromCall
        this.route.navigate(['login']);

        e.preventDefault();
    }
}
