import * as Raven from 'raven-js';
import {BrowserModule} from '@angular/platform-browser';
import {ErrorHandler, NgModule} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';
import {ReactiveFormsModule} from '@angular/forms';
import {route} from './app.route';
import {MyDatePickerModule} from 'mydatepicker';

import {AppComponent} from './app.component';
import {HeaderComponent} from './header/header.component';
import {MunculiniDirective} from "./directives/munculini.directive";
import {MunculituDirective} from "./directives/munculitu.directive";
import {AnginComponent} from './angin/angin.component';
import {SpinnerComponent} from './spinner/spinner.component';
import {WindroseComponent} from './windrose/windrose.component';
import {RmsComponent} from './rms/rms.component';
import {WaterfallComponent} from './waterfall/waterfall.component';
import {PdfComponent} from './pdf/pdf.component';
import {LoginComponent} from './login/login.component';
import {GuardService} from "./services/guard.service";
import {AuthService} from "./services/auth.service";

Raven
  .config('https://5206a016bc224509a447da0d7f00f35f@sentry.io/232316')
  .install();

export class RavenErrorHandler implements ErrorHandler {
  handleError(err:any) : void {
    Raven.captureException(err);
  }
}

@NgModule({
    declarations: [
        AppComponent,
        MunculiniDirective,
        MunculituDirective,
        HeaderComponent,
        AnginComponent,
        SpinnerComponent,
        WindroseComponent,
        RmsComponent,
        WaterfallComponent,
        PdfComponent,
        LoginComponent
    ],
    imports: [
        BrowserModule,
        FormsModule,
        ReactiveFormsModule,
        HttpModule,
        route,
        MyDatePickerModule
    ],
    providers: [
        { provide: ErrorHandler, useClass: RavenErrorHandler },
        AuthService,
        GuardService
    ],
    bootstrap: [AppComponent]
})
export class AppModule {
}
