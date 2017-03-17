import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';
import {ReactiveFormsModule} from '@angular/forms';
import {route} from './app.route';

import {AppComponent} from './app.component';
import {HeaderComponent} from './header/header.component';
import {MunculiniDirective} from "./directives/munculini.directive";
import {MunculituDirective} from "./directives/munculitu.directive";
import { AnginComponent } from './angin/angin.component';
import { SpinnerComponent } from './spinner/spinner.component';

@NgModule({
    declarations: [
        AppComponent,
        MunculiniDirective,
        MunculituDirective,
        HeaderComponent,
        AnginComponent,
        SpinnerComponent
    ],
    imports: [
        BrowserModule,
        FormsModule,
        ReactiveFormsModule,
        HttpModule,
        route
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule {
}
