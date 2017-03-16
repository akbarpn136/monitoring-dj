import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';
import {route} from './app.route';

import {AppComponent} from './app.component';
import {HeaderComponent} from './header/header.component';
import {MunculiniDirective} from "./directives/munculini.directive";
import {MunculituDirective} from "./directives/munculitu.directive";
import { AnginComponent } from './angin/angin.component';

@NgModule({
    declarations: [
        AppComponent,
        MunculiniDirective,
        MunculituDirective,
        HeaderComponent,
        AnginComponent
    ],
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        route
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule {
}
