/**
 * Created by USER on 2/20/2017.
 */
import {Route, RouterModule} from '@angular/router';
import {AnginComponent} from "./angin/angin.component";
import {WindroseComponent} from "./windrose/windrose.component";
import {RmsComponent} from "./rms/rms.component";
import {WaterfallComponent} from "./waterfall/waterfall.component";
import {PdfComponent} from "./pdf/pdf.component";
import {LoginComponent} from "./login/login.component";
import {GuardService} from "./services/guard.service";

const APP_ROUTES: Route[] = [
    {path: 'rms', component: RmsComponent, canActivate: [GuardService]},
    {path: 'waterfall', component: WaterfallComponent, canActivate: [GuardService]},
    {path: 'pdf', component: PdfComponent, canActivate: [GuardService]},
    {path: 'windrose', component: WindroseComponent, canActivate: [GuardService]},
    {path: 'angin', component: AnginComponent, canActivate: [GuardService]},
    {path: 'login', component: LoginComponent},
    {path: '', component: AnginComponent, canActivate: [GuardService]},
    {path: '**', redirectTo:'', pathMatch:'full'},
];

export const route = RouterModule.forRoot(APP_ROUTES);
